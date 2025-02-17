#Modded By KienTF (KCD Dev) 
import os
from setuptools import find_packages, setup

REQUIRED_PACKAGES = [
    # Required for Apache Beam with Python 3
    'tensorflow>=2.0,<2.13',
    'pyyaml>=6.0.0',
    'avro-python3',
    'apache-beam',
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

# Dynamically finding all modules in the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))
module_directory = os.path.join(current_directory, 'object_detection')

setup(
    name='kientf_object_detection',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    include_package_data=True,
    packages=find_packages(where=current_directory),  # Automatically find all packages
    package_dir={  # Directory mapping for specific folders
        'datasets': os.path.join('slim', 'datasets'),
        'nets': os.path.join('slim', 'nets'),
        'preprocessing': os.path.join('slim', 'preprocessing'),
        'deployment': os.path.join('slim', 'deployment'),
        'scripts': os.path.join('slim', 'scripts'),
    },
    description='TensorFlow Object Detection Library With Modded By Kien',
    python_requires='>3.6',
)
