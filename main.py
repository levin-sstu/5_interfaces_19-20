import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from Questionnare import Questionnaire


os.environ['QT_PLUGIN_PATH'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.venv', 'Lib', 'site-packages', 'PyQt5', 'Qt5', 'plugins')


class DynamicFormApp(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.add_button = QPushButton("Добавить анкету", self)
        self.add_button.clicked.connect(self.add_questionnaire)
        self.layout.addWidget(self.add_button)
        self.questionnaires = []

    def add_questionnaire(self):
        questionnaire = Questionnaire(self)
        self.questionnaires.append(questionnaire)
        self.layout.addWidget(questionnaire)

if __name__ == "__main__":
    app = QApplication([])
    window = DynamicFormApp()
    window.show()
    app.exec_()