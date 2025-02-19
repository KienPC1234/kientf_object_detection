import warnings
import os
import sys
import shutil
import importlib

warnings.filterwarnings("ignore", category=DeprecationWarning)


site_packages_path = os.path.join(sys.prefix, 'Lib', 'site-packages')

augment_file_path = os.path.join(site_packages_path, 'official', 'vision', 'image_classification', 'augment.py')

try:
    from tensorflow.python.keras.layers.preprocessing import image_preprocessing as image_ops # type: ignore
    print("Module tensorflow.python.keras.layers.preprocessing is available.")
except ModuleNotFoundError:
    print("Module not found. Proceeding to modify augment.py...")

    if os.path.exists(augment_file_path):
        with open(augment_file_path, 'r') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if "from tensorflow.python.keras.layers.preprocessing import image_preprocessing as image_ops" in line:
                lines[i] = line.replace(
                    "from tensorflow.python.keras.layers.preprocessing import image_preprocessing as image_ops",
                    "from tensorflow.keras.preprocessing import image as image_ops"
                )
                print(f"Modified line {i + 1}: {lines[i].strip()}")
                break

        with open(augment_file_path, 'w') as file:
            file.writelines(lines)
        
        print(f"Modification completed in {augment_file_path}")
    else:
        print(f"File {augment_file_path} not found.")

try:
    from tensorflow.keras.preprocessing import image as image_ops # type: ignore
    print("Module tensorflow.keras.preprocessing is available.")
except ModuleNotFoundError:
    print("Module not found. Proceeding to modify augment.py...")

    if os.path.exists(augment_file_path):
        with open(augment_file_path, 'r') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if "tensorflow.keras.preprocessing" in line:
                lines[i] = line.replace(
                    "from tensorflow.keras.preprocessing import image as image_ops",
                    "from tensorflow.python.keras.layers.preprocessing import image_preprocessing as image_ops"
                )
                print(f"Modified line {i + 1}: {lines[i].strip()}")
                break

        with open(augment_file_path, 'w') as file:
            file.writelines(lines)
        
        print(f"Modification completed in {augment_file_path}")
    else:
        print(f"File {augment_file_path} not found.")


def get_package_path(package_name):
    spec = importlib.util.find_spec(package_name)
    if spec and spec.origin:
        return os.path.dirname(spec.origin)
    return None

def delete_object_detection(package_name):
    package_path = get_package_path(package_name)
    if not package_path:
        print(f"Package '{package_name}' not found.")
        return
    
    target_path = os.path.join(package_path, "object_detection")
    if os.path.exists(target_path) and os.path.isdir(target_path):
        shutil.rmtree(target_path)
        print(f"Deleted: {target_path}")

delete_object_detection("object_detection")

