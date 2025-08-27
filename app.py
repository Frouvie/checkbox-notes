from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QPushButton, QLineEdit, QCheckBox, QListWidget, QWidget
from data import get_data, update_data

class NoteWindow(QMainWindow):
    def __init__(self, title, content):
        super().__init__()

        self.setWindowTitle(title)
        self.resize(400, 300)

        layout = QVBoxLayout()
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setLayout(layout)
        
        self.line = QLineEdit()
        self.button = QPushButton("Create note")
        self.notes = {}

        layout.addWidget(self.line)
        layout.addWidget(self.button)

        self.button.clicked.connect(self.create_note)

        for item, value in content.items():
            checkbox = QCheckBox(text=item)
            checkbox.setChecked(value)
            self.notes[item] = checkbox
            checkbox.checkStateChanged.connect(self.state_changed)
            layout.addWidget(checkbox)

    def create_note(self):
        text = self.line.text()
        if len(text) == 0:
            return
        data = get_data()
        data[self.windowTitle()][text] = False
        update_data(data)

        checkbox = QCheckBox(text)
        checkbox.setChecked(False)
        self.notes[text] = checkbox

        checkbox.checkStateChanged.connect(self.state_changed)

        self.centralWidget().layout().addWidget(checkbox)
        self.line.clear()

    def state_changed(self):
        data = get_data()
        title_window = self.windowTitle()
        title_note = self.sender().text()
        data[title_window][title_note] = not bool(data[title_window][title_note])
        update_data(data)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Checkbox Notes")
        self.resize(400, 300)

        layout = QVBoxLayout()
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setLayout(layout)

        self.line = QLineEdit()
        self.button = QPushButton("Create list")
        self.list = QListWidget()
        self.notes = []
        self.data = get_data()

        for note in self.notes:
            note.show()

        for key in self.data.keys():
            self.list.addItem(key)

        self.button.clicked.connect(self.create_list)
        self.list.itemClicked.connect(self.open_list)

        layout.addWidget(QLabel("Checkbox Notes"))
        layout.addWidget(self.line)
        layout.addWidget(self.button)
        layout.addWidget(self.list)

    def create_list(self):
        text = self.line.text()
        if len(text) == 0:
            return
        data = get_data()
        data[text] = {}
        update_data(data)

        self.list.addItem(text)
        
        self.line.clear()
    
    def open_list(self, item):
        title = item.text()
        content = self.data[title]
        note = NoteWindow(title, content)
        note.show()
        self.notes.append(note)