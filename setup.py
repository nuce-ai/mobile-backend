"""Setup script for object_detection."""

from setuptools import find_packages
from setuptools import setup


setup(
    name='object_detection',
    version='0.1',
    include_package_data=True,
    packages=[p for p in find_packages() if p.startswith('object_detection')],
    description='Tensorflow Object Detection Library',
)