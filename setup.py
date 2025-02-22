from setuptools import find_packages, setup
import os
import shutil

#<--BUILD FILE-->

base_dir = os.path.dirname(os.path.abspath(__file__))
object_detection_dir = os.path.join(base_dir, 'object_detection')
os.makedirs(object_detection_dir, exist_ok=True)

files_to_copy = []
for subdir, dirs, files in os.walk(base_dir):
    files_to_copy.extend(
            os.path.join(subdir, file)
            for file in files
        )
        

total_files = len(files_to_copy)

for index, src_path in enumerate(files_to_copy):
    dst_path = os.path.join(object_detection_dir, os.path.relpath(src_path, base_dir))
    
    try:
        if os.path.exists(dst_path):
            os.remove(dst_path)

        os.makedirs(os.path.dirname(dst_path), exist_ok=True)

        
        shutil.copy2(src_path, dst_path)
        

    except Exception as e:
        continue
    
setuppt =  os.path.join(base_dir, 'object_detection', "setup.py")
build = os.path.join(base_dir, 'object_detection', "build")
build2 = os.path.join(base_dir, 'object_detection', "kientf_object_detection.egg-info")
build3 = os.path.join(base_dir,'object_detection','object_detection')

if os.path.exists(setuppt) and os.path.isfile(setuppt):
    os.remove(setuppt)

for folder in ["build", "build2", "build3"]:
    if os.path.exists(folder) and os.path.isdir(folder):
        for root, dirs, files in os.walk(folder, topdown=False):
            for file in files:
                try:
                    os.remove(os.path.join(root, file))
                except Exception as e:
                    continue
            for d in dirs:
                try:
                    os.rmdir(os.path.join(root, d))
                except Exception as e:
                    continue
        try:
            os.rmdir(folder)
        except Exception as e:
            continue

#<--SETUP-->

REQUIRED_PACKAGES = [
    'tensorflow>=2.0,<2.12',
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
    'tf-models-official>=2.5',
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
        find_packages(where=os.path.join('.', 'slim'))),
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
    python_requires='>3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
