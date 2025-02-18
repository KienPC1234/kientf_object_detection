import os
import shutil

base_dir = os.path.dirname(os.path.abspath(__file__))
object_detection_dir = os.path.join(base_dir, 'object_detection')

if os.path.exists(object_detection_dir):
    shutil.rmtree(object_detection_dir)

os.makedirs(object_detection_dir)

for subdir, dirs, files in os.walk(base_dir):
    if subdir == base_dir:
        continue
    
    if any(file.endswith('.py') for file in files):
        for file in files:
            if file != 'setup.py':
                src_path = os.path.join(subdir, file)
                dst_path = os.path.join(object_detection_dir, os.path.relpath(src_path, base_dir))
                
                try:

                    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
                    
                    shutil.copy(src_path, dst_path)
                except Exception as e:
                    print(f"Could not copy file {src_path}. Error: {e}")
                    continue
            
#Setup

from setuptools import find_packages, setup

REQUIRED_PACKAGES = [
    'tensorflow>=2.0,<2.13',
    'pyyaml>=6.0.0',
    'avro-python3',
    'apache-beam<=2.50',
    'pillow',
    'lxml',
    'matplotlib',
    'cython',
    'contextlib2',
    'tf-slim',
    'six',
    'pycocotools',
    'lvis',
    'scipy',
    'pandas',
    'tf-models-official>=2.7',
    'tensorflow_io',
    'keras',
    'protobuf==3.*',
    'pyparsing==2.4.7',  # TODO(b/204103388)
    'sacrebleu<=2.2.0'  # https://github.com/mjpost/sacrebleu/issues/209
]

setup(
    name='kientf_object_detection',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    include_package_data=True,
    packages=(
        [p for p in find_packages() if p.startswith('object_detection')] +
        find_packages(where=os.path.join('.', 'slim'))
    ),
    package_dir={
        'datasets': os.path.join('slim', 'datasets'),
        'nets': os.path.join('slim', 'nets'),
        'preprocessing': os.path.join('slim', 'preprocessing'),
        'deployment': os.path.join('slim', 'deployment'),
        'scripts': os.path.join('slim', 'scripts'),
    },
    description='TensorFlow Object Detection Library With Modded By Kien',
    long_description='This package is a modified version of TensorFlow\'s Object Detection Library, developed by KienTF for custom implementations and improvements.',
    long_description_content_type='text/markdown',
    python_requires='>3.6'
)
