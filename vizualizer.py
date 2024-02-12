from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QPushButton, QFileDialog, QWidget, QSizePolicy
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
        self.close_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.close_button.setFixedWidth = 50

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

        # Apply styles
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QTextEdit {
                background-color: white;
                border: 1px solid #ddd;
                padding: 8px;
                font-size: 14px;
                color: #333;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 8px 16px;
                font-size: 14px;
                border: none;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)



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
