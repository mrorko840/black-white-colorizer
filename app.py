import os
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog, QVBoxLayout, QMessageBox, QGraphicsOpacityEffect
from PyQt6.QtGui import QPixmap, QImage, QIcon
from PyQt6.QtCore import Qt
import matplotlib.pyplot as plt
from colorizers import *


# Opacity Effect তৈরি করুন
half_opacity_effect = QGraphicsOpacityEffect()
half_opacity_effect.setOpacity(0.5)  # 50% transparency

full_opacity_effect = QGraphicsOpacityEffect()
full_opacity_effect.setOpacity(1)  # 50% transparency

# Opacity Effect তৈরি করুন
half_opacity_effect2 = QGraphicsOpacityEffect()
half_opacity_effect2.setOpacity(0.5)  # 50% transparency

full_opacity_effect2 = QGraphicsOpacityEffect()
full_opacity_effect2.setOpacity(1)  # 50% transparency

def get_resource_path(relative_path):
    """ PyInstaller build করার পর assets ফাইলের path ঠিকমতো পেতে সাহায্য করবে """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class ColorizeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.img_path = None
        self.default_pixmap = QPixmap("assets/dummy.jpg").scaledToHeight(400, Qt.TransformationMode.SmoothTransformation)
        self.default_pixmap = QPixmap(get_resource_path("assets/dummy.jpg")).scaledToHeight(400, Qt.TransformationMode.SmoothTransformation)
        self.img_label.setPixmap(self.default_pixmap)

    def initUI(self):
        self.setWindowTitle("Black & White Image Colorizer")
        icon_path = os.path.join(os.path.dirname(__file__), "icon.ico")
        self.setWindowIcon(QIcon(icon_path))
        self.setGeometry(100, 100, 400, 550)
        self.setStyleSheet("background-color: #282c36; color: white;")

        self.label = QLabel("Upload an image", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("font-size: 18px; text-align: center; font-weight: bold; color: #ffcc00;")

        self.img_label = QLabel(self)
        self.img_label.setFixedHeight(400)
        self.img_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.img_label.setStyleSheet("background-color: gray; border: 2px solid gray; border-radius: 5px;")

        self.upload_btn = QPushButton("Select Image", self)
        self.upload_btn.setStyleSheet("""
            QPushButton {
            background-color: gray; 
            color: white; 
            font-size: 16px; 
            padding: 10px; 
            border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #5f5f5f; /* Hover হলে রঙ পরিবর্তন */
                color: white; /* টেক্সটের রঙ পরিবর্তন */
            }
        """)
        self.upload_btn.clicked.connect(self.upload_image)
        self.colorize_btn = QPushButton("Colorize", self)
        self.colorize_btn.setGraphicsEffect(half_opacity_effect)  # Effect প্রয়োগ করুন
        self.colorize_btn.setStyleSheet("""
            QPushButton {
                background-color: #04aa6d; 
                color: white; 
                font-size: 16px; 
                padding: 10px; 
                border-radius: 5px;
                opacity: 50%;
            }
            QPushButton:hover {
                background-color: #018152; /* Hover হলে রঙ পরিবর্তন */
                color: white; /* টেক্সটের রঙ পরিবর্তন */
            }
        """)
        self.colorize_btn.setEnabled(False)
        self.colorize_btn.clicked.connect(self.colorize_image)

        self.save_btn = QPushButton("Save Image", self)
        self.save_btn.setStyleSheet("""
            QPushButton {
                background-color: #ffba00; 
                color: #0E0E1E; 
                font-size: 16px; 
                padding: 10px; 
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #d99e00; /* Hover হলে রঙ পরিবর্তন */
                color: white; /* টেক্সটের রঙ পরিবর্তন */
            }
        """)
        self.save_btn.setEnabled(False)
        self.save_btn.setGraphicsEffect(half_opacity_effect2)  # Effect প্রয়োগ করুন
        self.save_btn.clicked.connect(self.save_image)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.img_label, alignment=Qt.AlignmentFlag.AlignHCenter)
        vbox.addWidget(self.upload_btn)
        vbox.addWidget(self.colorize_btn)
        vbox.addWidget(self.save_btn)

        self.setLayout(vbox)

    def upload_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg)")
        if file_name:
            self.img_path = file_name
            pixmap = QPixmap(file_name)
            scaled_pixmap = pixmap.scaledToHeight(400, Qt.TransformationMode.SmoothTransformation)
            self.img_label.setPixmap(scaled_pixmap)
            self.img_label.setFixedWidth(scaled_pixmap.width())
            self.img_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            self.colorize_btn.setEnabled(True)
            self.colorize_btn.setGraphicsEffect(full_opacity_effect)  # Effect প্রয়োগ করুন

    def colorize_image(self):
        if not self.img_path:
            QMessageBox.warning(self, "Warning", "Please upload an image first!")
            return

        # Load models
        colorizer = siggraph17(pretrained=True).eval()
        img = load_img(self.img_path)
        (tens_l_orig, tens_l_rs) = preprocess_img(img, HW=(256, 256))

        out_img = postprocess_tens(tens_l_orig, colorizer(tens_l_rs).cpu())

        # Convert numpy image to QImage with higher resolution
        out_img = (out_img * 255).astype(np.uint8)
        height, width, channel = out_img.shape
        q_img = QImage(out_img.data, width, height, 3 * width, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(q_img)

        scaled_pixmap = pixmap.scaledToHeight(400, Qt.TransformationMode.SmoothTransformation)
        self.img_label.setPixmap(scaled_pixmap)
        self.img_label.setFixedWidth(scaled_pixmap.width())
        self.img_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.colorized_image = out_img
        self.save_btn.setEnabled(True)
        self.save_btn.setGraphicsEffect(full_opacity_effect2)  # Effect প্রয়োগ করুন


    def save_image(self):
        if hasattr(self, 'colorized_image'):
            file_name, _ = QFileDialog.getSaveFileName(self, "Save Image", "colorized.jpg",
                                                       "Images (*.png *.jpg *.jpeg)")
            if file_name:
                plt.imsave(file_name, self.colorized_image)
                QMessageBox.information(self, "Saved", "Image saved successfully!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ColorizeApp()
    window.show()
    sys.exit(app.exec())
