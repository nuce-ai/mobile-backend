import subprocess
import json
proc = subprocess.Popen("python object_detection/main.py --image_file= 'samsung-neon.jpg'", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
ret  = proc.communicate()[0]
proc.wait()

with open("result.txt") as f:
    etJson = json.load(f)
print(etJson)