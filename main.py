import sys
from PySide2.QtWidgets import QApplication
from data_handler import initialize_files
from main_window import MainWindow

if __name__ == "__main__":
    initialize_files()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())