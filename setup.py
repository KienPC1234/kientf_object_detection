import os
from setuptools import find_packages, setup

REQUIRED_PACKAGES = [
    # Required for apache-beam with PY3
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


setup(
    name='kientf_object_detection',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    include_package_data=True,
    packages=find_packages(where="."),  
    package_dir={
        'object_detection': 'object_detection',
        'datasets': os.path.join('slim', 'datasets'),
        'nets': os.path.join('slim', 'nets'),
        'preprocessing': os.path.join('slim', 'preprocessing'),
        'deployment': os.path.join('slim', 'deployment'),
        'scripts': os.path.join('slim', 'scripts')
    },
    description='TensorFlow Object Detection Library With Modded By Kien',
    long_description='This package is a modified version of TensorFlow\'s Object Detection Library, developed by KienTF for custom implementations and improvements.',
    long_description_content_type='text/markdown',
    python_requires='>3.6',
)
