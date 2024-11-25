from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QScrollArea

from Questionnare import Questionnaire


class DynamicFormAppScroll(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_area.setWidget(self.scroll_widget)
        self.layout.addWidget(self.scroll_area)
        self.add_button = QPushButton("Добавить анкету", self)
        self.add_button.clicked.connect(self.add_questionnaire)
        self.layout.addWidget(self.add_button)
        self.questionnaires = []

    def add_questionnaire(self):
        questionnaire = Questionnaire(self.scroll_widget)
        self.questionnaires.append(questionnaire)
        self.scroll_layout.addWidget(questionnaire)

if __name__ == "__main__":
    app = QApplication([])
    window = DynamicFormAppScroll()
    window.show()
    app.exec_() 