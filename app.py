from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QLineEdit, QCheckBox, QListWidget, QWidget
from data import load_data, save_data, get_data, update_data

class NoteWindow(QMainWindow):
    def __init__(self, title, content):
        super().__init__()

        self.setWindowTitle(title)
        self.resize(400, 300)

        layout = QVBoxLayout()
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setLayout(layout)
        
        self.notes = {}

        for item, value in content.items():
            checkbox = QCheckBox(text=item)
            checkbox.setChecked(value == "True")
            layout.addWidget(checkbox)
            self.notes[item] = checkbox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Checkbox Notes")
        self.resize(400, 300)

        layout = QVBoxLayout()
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setLayout(layout)

        self.notes_windows = []
        self.data = get_data()
        self.line_widget = QLineEdit()
        self.list_widget = QListWidget()

        for note in self.notes_windows:
            note.show()

        for key in self.data.keys():
            self.list_widget.addItem(key)

        self.list_widget.itemClicked.connect(self.open_list)

        layout.addWidget(QLabel("Checkbox Notes"))
        layout.addWidget(self.line_widget)
        layout.addWidget(self.list_widget)
    
    def open_list(self, item):
        title = item.text()
        content = self.data[title]
        note = NoteWindow(title, content)
        note.show()
        self.notes_windows.append(note)