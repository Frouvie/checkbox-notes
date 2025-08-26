import sys
from PyQt6.QtWidgets import QApplication
from app import Application
        
app = QApplication(sys.argv)
window = Application()


def main():
    window.show()
    app.exec()


if __name__ == "__main__":
    main()