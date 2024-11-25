from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog
import json

from HobbyList import HobbyList
from PersonInfo import PersonInfo
from PhotoAlbum import PhotoAlbum


class Questionnaire(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.person_info = PersonInfo(self)
        self.layout.addWidget(self.person_info)
        self.hobby_list = HobbyList(self)
        self.layout.addWidget(self.hobby_list)
        self.photo_album = PhotoAlbum(self)
        self.layout.addWidget(self.photo_album)
        self.save_button = QPushButton("Сохранить", self)
        self.save_button.clicked.connect(self.save_to_json)
        self.layout.addWidget(self.save_button)
        self.load_button = QPushButton("Загрузить", self)
        self.load_button.clicked.connect(self.load_from_json)
        self.layout.addWidget(self.load_button)

    def save_to_json(self):
        data = {
            "person_info": self.person_info.to_json(),
            "hobbies": self.hobby_list.to_json(),
            "photos": self.photo_album.to_json()
        }
        file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "JSON Files (*.json)")
        if file_path:
            with open(file_path, 'w') as file:
                json.dump(data, file)

    def load_from_json(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "JSON Files (*.json)")
        if file_path:
            with open(file_path, 'r') as file:
                data = json.load(file)
                self.person_info.from_json(data["person_info"])
                self.hobby_list.from_json(data["hobbies"])
                self.photo_album.from_json(data["photos"])