import warnings
import os
import sys
import shutil
import importlib

#Dis Warn Spam
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)

site_packages_path = os.path.join(sys.prefix, 'Lib', 'site-packages')

augment_file_path = os.path.join(site_packages_path, 'official', 'vision', 'image_classification', 'augment.py')

global haveModule 

try:
    from tensorflow.keras.preprocessing import image as image_ops # type: ignore
    print("Module tensorflow.keras.preprocessing is available.")
    haveModule = True
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

try:
    from tensorflow.python.keras.layers.preprocessing import image_preprocessing as image_ops # type: ignore
    print("Module tensorflow.python.keras.layers.preprocessing is available.")
except ModuleNotFoundError:
    if not haveModule:
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

#<--Delete File-->
spec = importlib.util.find_spec("object_detection")
if spec and spec.origin:
    package_path = os.path.dirname(spec.origin)

if not package_path:
    print(f"Package 'object_detection' not found.")
else:
    target_path = os.path.join(package_path, "object_detection")
    if os.path.exists(target_path) and os.path.isdir(target_path):
        shutil.rmtree(target_path)
        print(f"Deleted: {target_path}")



