import numpy as np
import sys
import tensorflow as tf 
import json
from distutils.version import StrictVersion
from PIL import Image
import six
# This is needed since the notebook is stored in the object_detection folder.
sys.path.append("..")
from object_detection.utils import ops as utils_ops

if StrictVersion(tf.__version__) < StrictVersion('1.12.0'):
  raise ImportError('Please upgrade your TensorFlow installation to v1.12.*.')

from utils import label_map_util
# from utils import visualization_utils as vis_util



MODEL_NAME = 'object_detection/ssd_mobilenet_v1_coco_2018_01_28/'
PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'
PATH_TO_FROZEN_GRAPH = MODEL_NAME + '/frozen_inference_graph.pb'
PATH_TO_LABELS = 'object_detection/data/mscoco_label_map.pbtxt'
NUM_CLASSES = 90
IMAGE_NAME = sys.argv[1]
IMAGE_FILE_NAME = IMAGE_NAME.split(".")[0]

detection_graph = tf.compat.v2.Graph()
with detection_graph.as_default():
  od_graph_def = tf.compat.v1.GraphDef()
  with tf.compat.v1.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
    serialized_graph = fid.read()
    od_graph_def.ParseFromString(serialized_graph)
    tf.import_graph_def(od_graph_def, name='')


label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)


def load_image_into_numpy_array(image):
  (im_width, im_height) = image.size
  # print((im_width, im_height))
  return np.array(image.getdata()).reshape(
      (im_height, im_width, 3)).astype(np.uint8)


def run_inference_for_single_image(image, graph):
  with graph.as_default():
    with tf.compat.v1.Session() as sess:
    # Get handles to input and output tensors
      ops = tf.compat.v1.get_default_graph().get_operations()
      all_tensor_names = {output.name for op in ops for output in op.outputs}
      tensor_dict = {}
      for key in [
          'num_detections', 'detection_boxes', 'detection_scores',
          'detection_classes', 'detection_masks'
     ]:
        tensor_name = key + ':0'
        if tensor_name in all_tensor_names:
          tensor_dict[key] = tf.compat.v1.get_default_graph().get_tensor_by_name(
            tensor_name)
      if 'detection_masks' in tensor_dict:
        # The following processing is only for single image
        detection_boxes = tf.squeeze(tensor_dict['detection_boxes'], [0])
        detection_masks = tf.squeeze(tensor_dict['detection_masks'], [0])
        # Reframe is required to translate mask from box coordinates to image coordinates and fit the image size.
        real_num_detection = tf.cast(tensor_dict['num_detections'][0], tf.int32)
        detection_boxes = tf.slice(detection_boxes, [0, 0], [real_num_detection, -1])
        detection_masks = tf.slice(detection_masks, [0, 0, 0], [real_num_detection, -1, -1])
        detection_masks_reframed = utils_ops.reframe_box_masks_to_image_masks(
            detection_masks, detection_boxes, image.shape[1], image.shape[2])
        detection_masks_reframed = tf.cast(
            tf.greater(detection_masks_reframed, 0.5), tf.uint8)
        # Follow the convention by adding back the batch dimension
        tensor_dict['detection_masks'] = tf.expand_dims(
            detection_masks_reframed, 0)
      image_tensor = tf.compat.v1.get_default_graph().get_tensor_by_name('image_tensor:0')

      # Run inference
      output_dict = sess.run(tensor_dict,
                             feed_dict={image_tensor: image})

      # all outputs are float32 numpy arrays, so convert types as appropriate
      output_dict['num_detections'] = int(output_dict['num_detections'][0])
      output_dict['detection_classes'] = output_dict[
          'detection_classes'][0].astype(np.int64)
      output_dict['detection_boxes'] = output_dict['detection_boxes'][0]
      output_dict['detection_scores'] = output_dict['detection_scores'][0]
      if 'detection_masks' in output_dict:
        output_dict['detection_masks'] = output_dict['detection_masks'][0]
  return output_dict



image_file = 'upload/' + IMAGE_NAME
print(image_file)

image = Image.open(image_file)
image = image.rotate(0, expand=True)

# image.show()
image_np = load_image_into_numpy_array(image)
image_np_expanded = np.expand_dims(image_np, axis=0)
output_dict = run_inference_for_single_image(image_np_expanded, detection_graph)
max_boxes_to_draw = output_dict['detection_boxes'].shape[0]

labels = []
scores = []
coordinates = []

for i in range(min(max_boxes_to_draw, output_dict['detection_boxes'].shape[0])):
  if output_dict['detection_scores'] is None or output_dict['detection_scores'][i] > .5:
    display_str = ''
    if output_dict['detection_classes'][i] in six.viewkeys(category_index):
      class_name = category_index[output_dict['detection_classes'][i]]['name']
    else:
      class_name = 'N/A'
    display_str = str(class_name)
    labels.append(display_str)
    display_str = int(100*output_dict['detection_scores'][i])
    scores.append(display_str)
    coordinates.append(list(output_dict['detection_boxes'][i]))



im_width, im_height = image.size


import base64

list_image = []
for i in range(0,len(labels)):
    temp = Image.open(image_file)
    ymin = coordinates[i][0]
    xmin = coordinates[i][1]
    ymax = coordinates[i][2]
    xmax = coordinates[i][3]
    (left, right, top, bottom) = (xmin * im_width, xmax * im_width,
                                  ymin * im_height, ymax * im_height)
    img = temp.crop((left, top, right, bottom))
    img.save("temp.png")
    with open("temp.png",'rb') as image_crop:
      my_string = base64.b64encode(image_crop.read())
    image_base64 = my_string.decode("utf-8")
    list_image.append(image_base64)

retJson = []
for i in range(0,len(labels)):
  obj = {
    "label" : labels[i],
    "scores" : scores[i],
    "image" : list_image[i]
  }
  retJson.append(obj)


with open("assets/"+ IMAGE_FILE_NAME + ".txt",'w') as f: 
  json.dump(retJson,f)
