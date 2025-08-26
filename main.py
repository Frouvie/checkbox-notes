import sys
from PyQt6.QtWidgets import QApplication
from app import MainWindow
        
app = QApplication(sys.argv)
window = MainWindow()


def main():
    window.show()
    app.exec()


if __name__ == "__main__":
    main()