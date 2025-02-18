import warnings
import os
import sys

warnings.filterwarnings("ignore", category=DeprecationWarning)


site_packages_path = os.path.join(sys.prefix, 'Lib', 'site-packages')

augment_file_path = os.path.join(site_packages_path, 'official', 'vision', 'image_classification', 'augment.py')

try:
    from tensorflow.python.keras.layers.preprocessing import image_preprocessing as image_ops
    print("Module tensorflow.python.keras.layers.preprocessing is available.")
except ModuleNotFoundError:
    print("Module not found. Proceeding to modify augment.py...")

    # Kiểm tra nếu file augment.py tồn tại
    if os.path.exists(augment_file_path):
        with open(augment_file_path, 'r') as file:
            lines = file.readlines()

        # Tìm và thay thế dòng có lỗi
        for i, line in enumerate(lines):
            if "from tensorflow.python.keras.layers.preprocessing import image_preprocessing as image_ops" in line:
                lines[i] = line.replace(
                    "from tensorflow.python.keras.layers.preprocessing import image_preprocessing as image_ops",
                    "from tensorflow.keras.preprocessing import image as image_ops"
                )
                print(f"Modified line {i + 1}: {lines[i].strip()}")
                break

        # Ghi lại các thay đổi vào file
        with open(augment_file_path, 'w') as file:
            file.writelines(lines)
        
        print(f"Modification completed in {augment_file_path}")
    else:
        print(f"File {augment_file_path} not found.")
