# Black & White Image Colorizer 🎨🖼️

![PyQt6](https://img.shields.io/badge/PyQt6-GUI-blue.svg) ![Python](https://img.shields.io/badge/Python-3.8%2B-brightgreen.svg) ![Torch](https://img.shields.io/badge/Torch-DeepLearning-red.svg) ![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A deep learning-based application that colorizes black and white images using **PyQt6** for GUI and a pre-trained **SIGGRAPH17** colorization model.

## 🚀 Features

- Upload black & white images
- Automatically colorizes images using a deep learning model
- Preview the colorized image before saving
- Save the colorized image in **PNG, JPG, JPEG** formats
- Smooth and modern UI using **PyQt6**
- **PyInstaller** support for creating standalone executables

## 🖥️ Tech Stack

- **Python**
- **PyQt6** (For Gui)
- **Torch** (Deep Learning Model)
- **scikit-image**
- **numpy**
- **matplotlib**
- **Pillow** (Image Processing)
- **torchvision**
- **PyInstaller** (For packaging)

## 📂 Installation

### Step 1: Download Ai Model (git-bash or terminal)
```sh
mkdir -p ~/.cache/torch/hub/checkpoints
curl -o ~/.cache/torch/hub/checkpoints/siggraph17-df00044c.pth "https://colorizers.s3.us-east-2.amazonaws.com/siggraph17-df00044c.pth"
```

### Step 2: Clone the Repository
```sh
git clone https://github.com/mrorko840/black-white-colorizer.git
cd black-white-colorizer
```

### Step 3: Create a Virtual Environment (Recommended)
```sh
python -m venv venv
```

#### On Windows, use (git bash):
```sh 
source venv/Scripts/activate
```
**or**
#### On MacOs, use (terminal):
```sh
source venv/bin/activate
```

### Step 4: Install Dependencies
```sh
pip install -r requirements.txt
```

## 🏃‍♂️ Usage

Run the application using:
```sh
python app.py
```

### To Make Application (Optional)
To create a standalone executable **.exe** using **PyInstaller** (windows):
```sh
pyinstaller --onefile --noconsole --icon=icon.ico --add-data "assets/dummy.jpg;assets" app.py
```

To create a standalone executable **.app** using **PyInstaller** (mac):
```sh
pyinstaller --windowed --name "ImageColorize" --icon=icon.ico --add-data="assets/dummy.jpg:assets" app.py
```

## 🖼️ Screenshots

| Upload B&W Image                                                       | Colorized Output                                                       |
|------------------------------------------------------------------------|------------------------------------------------------------------------|
| <img style="max-width:250px;" src="https://i.imgur.com/pJA8rjf.png" /> | <img style="max-width:250px;" src="https://i.imgur.com/8R95mQ2.png" /> |

## 🛠️ Troubleshooting

- **Issue:** Application not running after `pyinstaller` build?  
  **Solution:** Use `--add-data` flag properly to include assets.
  
- **Issue:** Model not found error?  
  **Solution:** Ensure `colorizers` module and pretrained models are properly installed.

## 🏆 Contributors

- **হিমেল** - [Facebook](https://facebook.com/mr.orko.10)

## 📜 License

This project is licensed under the **MIT License**. Feel free to use and modify.

---

⭐ **If you like this project, don't forget to star the repository!**

