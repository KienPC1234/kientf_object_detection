# 🎨 KienTF Object Detection  
**A refined and bug-fixed version of TensorFlow's Object Detection API**  

![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=flat&logo=tensorflow)  
![Python](https://img.shields.io/badge/Python-3.7%2B-blue?style=flat&logo=python)  
![License](https://img.shields.io/badge/License-Apache%202.0-green?style=flat)  

---

## 📌 Overview  
**kientf_object_detection** is an improved version of the original **TensorFlow Object Detection API**, focusing on:  
✅ Fixing critical bugs that impact model training and inference.  
✅ Enhancing performance and stability for real-world object detection tasks.  
✅ Ensuring compatibility with TensorFlow 2.x (up to 2.12) for smoother workflows.  

If you're tired of running into frustrating errors in the original **object_detection**, this repository provides a **cleaner, more reliable** solution!  

---

## 🚀 Key Features & Fixes  
🔧 **Bug Fixes:**  
- Resolved major issues in model training, inference, and evaluation.  
- Fixed deprecated functions and compatibility errors with TensorFlow 2.x.  

⚡ **Performance Enhancements:**  
- Optimized data processing & augmentation pipelines.  
- Improved model stability and efficiency in large-scale datasets.  

📊 **Better Evaluation Metrics:**  
- Fixed inconsistencies in mAP calculations.  
- More accurate and reliable benchmarking tools.  

🔄 **Easy Integration:**  
- Maintains full compatibility with existing **TensorFlow Object Detection API** models.  
- Plug-and-play support for both **custom datasets** and pre-trained models.  

---

## 👥 Installation  
You can install this repository directly via **pip**:  
```bash
pip install git+https://github.com/KienPC1234/kientf_object_detection.git
```

### 🔹 Dependencies  
Ensure you have **TensorFlow 2.x** installed (version **≤2.12**):  
```bash
pip install "tensorflow<=2.12"
```

---

## 🔧 Usage  
### 🔹 1. Train a Model  
Modify the pipeline config file and run:  
```bash
python model_main_tf2.py --pipeline_config_path=configs/my_model.config --model_dir=training/
```

### 🔹 2. Export Trained Model  
```bash
python exporter_main_v2.py --input_type image_tensor --pipeline_config_path=configs/my_model.config --trained_checkpoint_dir=training/ --output_directory=exported_model/
```

### 🔹 3. Run Inference  
```python
from object_detection.utils import visualization_utils as viz_utils
from object_detection.builders import model_builder

# Load the model and run inference
```

---

## 📂 Project Structure  
```
kientf_object_detection/
│── configs/              # Configuration files for different models  
│── data/                 # Training and validation datasets  
│── models/               # Pre-trained models  
│── training/             # Checkpoints and logs  
│── scripts/              # Utility scripts for data processing  
│── object_detection/     # Core detection module (fixed version)  
│── README.md             # Project documentation  
```

---

## 🤝 Contributing  
Contributions are welcome! Feel free to open an issue or submit a pull request.  

💡 **Have a bug to report?** Open an issue!  
🚀 **Want to improve the repo?** Submit a PR!  

---

## 📝 License  
This project is licensed under the **Apache 2.0 License**. See [LICENSE](LICENSE) for details.  

---

## 📩 Contact  
For any questions or collaborations, reach out via:  
📧 **Email:** kienpc872009@gmail.com


🔥 **Happy coding & object detecting!** 🔥

