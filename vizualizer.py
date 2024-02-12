from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QPushButton, QFileDialog, QWidget
import sys

class FileViewerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

        # Load file content automatically when the application starts
        self.load_file()

    def init_ui(self):
        # Create widgets
        self.text_edit = QTextEdit(self)

        self.close_button = QPushButton('Close', self)
        self.close_button.clicked.connect(self.close)

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.close_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Set window properties
        self.setWindowTitle('File Viewer')
        self.setGeometry(100, 100, 800, 600)

    def load_file(self):
        # Open file dialog to select a text file
        
        file_path = r'C:\Users\Shiv\dev\InfoVeiwer-Final_Year_Project-\received\sample.txt'

        if file_path:
            # Read the content of the selected file
            with open(file_path, 'r') as file:
                file_content = file.read()

            # Display the content in the QTextEdit widget
            self.text_edit.setPlainText(file_content)

def main():
    app = QApplication(sys.argv)
    main_win = FileViewerApp()
    main_win.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
