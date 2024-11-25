from PyQt5.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QPushButton, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap
import os

class PhotoAlbum(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_area.setWidget(self.scroll_widget)
        self.layout.addWidget(self.scroll_area)
        self.add_photo_button = QPushButton("Добавить фото", self)
        self.add_photo_button.clicked.connect(self.add_photo)
        self.layout.addWidget(self.add_photo_button)
        self.photos = []  # Хранит пути к фото

    def add_photo(self):
        photo_path, _ = QFileDialog.getOpenFileName(self, "Выбрать фото", "", "Images (*.png *.xpm *.jpg *.jpeg *.bmp)")
        if photo_path:
            pixmap = QPixmap(photo_path)
            if pixmap.isNull():
                return  # Если изображение не загружено
            label = QLabel(self)
            label.setPixmap(pixmap.scaled(200, 200, aspectRatioMode=1))  # Сжимаем для отображения
            self.scroll_layout.addWidget(label)
            self.photos.append(photo_path)  # Сохраняем путь

    def to_json(self):
        return self.photos

    def from_json(self, data):
        self.photos = data
        for photo_path in self.photos:
            if os.path.exists(photo_path):
                pixmap = QPixmap(photo_path)
                label = QLabel(self)
                label.setPixmap(pixmap.scaled(200, 200, aspectRatioMode=1))  # Сжимаем для отображения
                self.scroll_layout.addWidget(label)
