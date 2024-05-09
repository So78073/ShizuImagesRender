import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon, QFont
from PIL import Image
import pyImageFunctions as pyy

class ImageResizeApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Redimensionar Imagem')

        # Definir o valor padrão para file_path_input
        self.default_file_path = 'caminho/para/sua/imagem.jpg'
        self.file_path_label = QLabel('Caminho do Arquivo:')
        self.file_path_input = QLineEdit(self.default_file_path)
        self.file_path_input.setReadOnly(True) 
        self.file_browse_button = QPushButton(QIcon('icons/open.png'), '')
        self.file_browse_button.setToolTip('Selecionar Arquivo')
        self.file_browse_button.clicked.connect(self.browse_file)


        self.dimension_layout = QHBoxLayout()
        self.width_label = QLabel('Largura:')
        self.width_input = QLineEdit()
        self.dimension_layout.addWidget(self.width_label)
        self.dimension_layout.addWidget(self.width_input)

        self.height_label = QLabel('Altura:')
        self.height_input = QLineEdit()
        self.dimension_layout.addWidget(self.height_label)
        self.dimension_layout.addWidget(self.height_input)

        self.resize_button = QPushButton(QIcon('icons/resize.png'), '')
        self.resize_button.setToolTip('Redimensionar')
        self.resize_button.clicked.connect(self.resize_image)

        layout = QVBoxLayout()
        layout.addWidget(self.file_path_label)
        layout.addWidget(self.file_path_input)
        layout.addWidget(self.file_browse_button)
        layout.addLayout(self.dimension_layout)
        layout.addWidget(self.resize_button)

        self.setLayout(layout)

        # Estilizar a interface
        self.setStyleSheet('''
            QLabel {
                font-size: 16px;
                font-weight: bold;
            }
            QLineEdit, QPushButton {
                font-size: 14px;
                padding: 6px;
                border: 2px solid #ccc;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #f0f0f0;
            }
        ''')

    def browse_file(self):
        file_dialog = QFileDialog()
        file_path = file_dialog.getOpenFileName(self, 'Selecionar Arquivo')[0]
        if file_path:
            self.file_path_input.setText(file_path)

    def resize_image(self):
        file_path = self.file_path_input.text()
        width = int(self.width_input.text())
        height = int(self.height_input.text())

        origin = file_path
        newDimensionIMG = (width, height) 

        pyy.main(origin, newDimensionIMG)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Definir o ícone da aplicação
    app.setWindowIcon(QIcon('icons/app_icon.png'))

    # Definir a fonte padrão para toda a aplicação
    app.setFont(QFont('Arial', 12))

    resize_app = ImageResizeApp()
    resize_app.show()
    sys.exit(app.exec_())


    
        
