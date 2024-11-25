from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QListWidget, QLabel

class HobbyList(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.label = QLabel("Хобби", self)
        self.layout.addWidget(self.label)
        self.list_widget = QListWidget(self)
        self.layout.addWidget(self.list_widget)
        self.line_edit = QLineEdit(self)
        self.line_edit.returnPressed.connect(self.add_hobby)
        self.layout.addWidget(self.line_edit)

    def add_hobby(self):
        hobby = self.line_edit.text()
        if hobby:
            self.list_widget.addItem(hobby)
            self.line_edit.clear()

    def to_json(self):
        return [self.list_widget.item(i).text() for i in range(self.list_widget.count())]

    def from_json(self, data):
        self.list_widget.clear()
        for hobby in data:
            self.list_widget.addItem(hobby)
