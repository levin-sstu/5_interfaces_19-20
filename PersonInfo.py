from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QDateEdit
from PyQt5.QtCore import QDate

class PersonInfo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.name_edit = QLineEdit(self)
        self.layout.addWidget(QLabel("ФИО"))
        self.layout.addWidget(self.name_edit)
        self.birth_date_edit = QDateEdit(self)
        self.birth_date_edit.setDate(QDate.currentDate())
        self.layout.addWidget(QLabel("Дата рождения"))
        self.layout.addWidget(self.birth_date_edit)
        self.citizenship_edit = QLineEdit(self)
        self.layout.addWidget(QLabel("Гражданство"))
        self.layout.addWidget(self.citizenship_edit)

    def to_json(self):
        return {
            "name": self.name_edit.text(),
            "birth_date": self.birth_date_edit.date().toString("dd.MM.yyyy"),
            "citizenship": self.citizenship_edit.text()
        }

    def from_json(self, data):
        self.name_edit.setText(data["name"])
        self.birth_date_edit.setDate(QDate.fromString(data["birth_date"], "dd.MM.yyyy"))
        self.citizenship_edit.setText(data["citizenship"])