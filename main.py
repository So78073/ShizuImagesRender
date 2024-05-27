import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QFileDialog,
                             QMessageBox)
from PyQt5.QtGui import QIcon, QFont
import os
import pyImageFunctions as pyy

pathDir = os.path.dirname(os.path.abspath(__file__))
pathDir = os.path.join(pathDir, 'data', 'input')

class ImageResizeApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Shizu ResizeImagePy')
        app.setWindowIcon(QIcon('assets/blackhat.jpg'))

        # Definir o valor padrão para file_path_input
        self.default_file_path = pathDir
        self.default_WH = '500'
 

        self.file_path_label = QLabel('Caminho do Arquivo:')
        self.file_path_input = QLineEdit(self.default_file_path)
        self.file_path_input.setReadOnly(True) 
        self.file_browse_button = QPushButton('Selecionar Arquivo')
        self.file_browse_button.setToolTip('Clique para selecionar um arquivo')
        self.file_browse_button.clicked.connect(self.browse_file)

        self.dimension_layout = QHBoxLayout()
        self.width_label = QLabel('Largura:')
        self.width_input = QLineEdit(self.default_WH )
        self.dimension_layout.addWidget(self.width_label)
        self.dimension_layout.addWidget(self.width_input)

        self.height_label = QLabel('Altura:')
        self.height_input = QLineEdit(self.default_WH )
        self.dimension_layout.addWidget(self.height_label)
        self.dimension_layout.addWidget(self.height_input)

        self.resize_button = QPushButton('Redimensionar')
        self.resize_button.setToolTip('Clique para redimensionar a imagem')
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

        # Definir tamanho fixo da janela
        self.setFixedSize(400, 200)  # Ajuste o tamanho conforme necessário

    def browse_file(self):
        file_dialog = QFileDialog()
        file_path = file_dialog.getOpenFileName(self, 'Selecionar Arquivo')[0]
        if file_path:
            self.file_path_input.setText(file_path)

    def resize_image(self):
        file_path = self.file_path_input.text()

        if not file_path or not os.path.isfile(file_path):
            QMessageBox.critical(self, 'Erro', 'Caminho do arquivo inválido.')
            return

        try:
            width = int(self.width_input.text())
            height = int(self.height_input.text())
        except ValueError:
            QMessageBox.critical(self, 'Erro', 'Largura e Altura devem ser números inteiros.')
            return

        if width <= 0 or height <= 0:
            QMessageBox.critical(self, 'Erro', 'Largura e Altura devem ser valores positivos.')
            return

        try:
            origin = file_path
            newDimensionIMG = (width, height)
            pyy.main(origin, newDimensionIMG)
            QMessageBox.information(self, 'Sucesso', 'Imagem redimensionada com sucesso.')
        except Exception as e:
            QMessageBox.critical(self, 'Erro', f'Erro ao redimensionar a imagem: {e}')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Definir o ícone da aplicação
    app.setWindowIcon(QIcon('icons/app_icon.png'))

    # Definir a fonte padrão para toda a aplicação
    app.setFont(QFont('Arial', 12))

    resize_app = ImageResizeApp()
    resize_app.show()
    sys.exit(app.exec_())
