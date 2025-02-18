import os
import shutil

# Đường dẫn thư mục gốc chứa setup.py
base_dir = os.path.dirname(os.path.abspath(__file__))
object_detection_dir = os.path.join(base_dir, 'object_detection')

# Nếu thư mục object_detection đã tồn tại, xóa đi
if os.path.exists(object_detection_dir):
    shutil.rmtree(object_detection_dir)

# Tạo thư mục object_detection mới
os.makedirs(object_detection_dir)

# Duyệt qua tất cả các thư mục con và file trong thư mục gốc
for subdir, dirs, files in os.walk(base_dir):
    # Loại trừ thư mục gốc
    if subdir == base_dir:
        continue
    
    # Kiểm tra xem thư mục có chứa file Python (.py) không
    if any(file.endswith('.py') for file in files):
        for file in files:
            if file != 'setup.py':
                src_path = os.path.join(subdir, file)
                dst_path = os.path.join(object_detection_dir, os.path.relpath(src_path, base_dir))
                
                try:
                    # Tạo thư mục đích nếu chưa có
                    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
                    
                    # Sao chép file vào thư mục đích
                    shutil.copy(src_path, dst_path)
                except Exception as e:
                    # Nếu có lỗi, bỏ qua file này
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
