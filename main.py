import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QFileDialog,
                             QMessageBox, QProgressBar)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import os
import pyImageFunctions as pyy

pathDir = os.path.dirname(os.path.abspath(__file__))
pathDir = os.path.join(pathDir, 'data', 'input')
pathOut = pathDir.replace('input', 'output')

class ResizeThread(QThread):
    progress = pyqtSignal(int)

    def __init__(self, origin_paths, output_paths, new_dimensions):
        super().__init__()
        self.origin_paths = origin_paths
        self.output_paths = output_paths
        self.new_dimensions = new_dimensions

    def run(self):
        total = len(self.origin_paths)
        for i, (origin, output) in enumerate(zip(self.origin_paths, self.output_paths)):
            pyy.resize_image(origin, output, self.new_dimensions)
            self.progress.emit(int((i + 1) / total * 100))

class ImageResizeApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Shizu ResizeImagePy')
        self.setWindowIcon(QIcon('assets/logo/blackhat.jpg'))
        
        self.default_file_path = pathDir
        self.default_WH = '500'

        self.file_path_label = QLabel('Caminho dos Arquivos:')
        self.file_path_input = QLineEdit(self.default_file_path)
        self.file_path_input.setReadOnly(True)
        self.file_browse_button = QPushButton('Selecionar Arquivos')
        self.file_browse_button.setToolTip('Clique para selecionar arquivos')
        self.file_browse_button.clicked.connect(self.browse_files)

        self.output_path_label = QLabel('Caminho de Saída:')
        self.output_path_input = QLineEdit()
        self.output_path_input.setReadOnly(True)
        self.output_browse_button = QPushButton('Selecionar Caminho de Saída')
        self.output_browse_button.setToolTip('Clique para selecionar um caminho de saída')
        self.output_browse_button.clicked.connect(self.browse_output_folder)

        self.dimension_layout = QHBoxLayout()
        self.width_label = QLabel('Largura:')
        self.width_input = QLineEdit(self.default_WH)
        self.dimension_layout.addWidget(self.width_label)
        self.dimension_layout.addWidget(self.width_input)

        self.height_label = QLabel('Altura:')
        self.height_input = QLineEdit(self.default_WH)
        self.dimension_layout.addWidget(self.height_label)
        self.dimension_layout.addWidget(self.height_input)

        self.resize_button = QPushButton('Redimensionar')
        self.resize_button.setToolTip('Clique para redimensionar as imagens')
        self.resize_button.clicked.connect(self.resize_images)

        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.progress_bar.setAlignment(Qt.AlignCenter)
        self.progress_bar.setVisible(False)  # Esconder a barra de progresso inicialmente

        layout = QVBoxLayout()
        layout.addWidget(self.file_path_label)
        layout.addWidget(self.file_path_input)
        layout.addWidget(self.file_browse_button)
        layout.addWidget(self.output_path_label)
        layout.addWidget(self.output_path_input)
        layout.addWidget(self.output_browse_button)
        layout.addLayout(self.dimension_layout)
        layout.addWidget(self.resize_button)
        layout.addWidget(self.progress_bar)

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

        self.setFixedSize(400, 400)

    def browse_files(self):
        file_dialog = QFileDialog()
        file_paths, _ = file_dialog.getOpenFileNames(self, 'Selecionar Arquivos')
        if file_paths:
            self.file_path_input.setText("; ".join(file_paths))
            self.file_paths = file_paths

    def browse_output_folder(self):
        folder_dialog = QFileDialog()
        folder_path = folder_dialog.getExistingDirectory(self, 'Selecionar Caminho de Saída')
        if folder_path:
            self.output_path_input.setText(folder_path)

    def resize_images(self):
        if not hasattr(self, 'file_paths') or not self.file_paths:
            QMessageBox.critical(self, 'Erro', 'Caminho dos arquivos inválido.')
            return

        output_path = self.output_path_input.text()

        if not output_path or not os.path.isdir(output_path):
            QMessageBox.critical(self, 'Erro', 'Caminho de saída inválido.')
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
            origin_paths = self.file_paths
            output_paths = [os.path.join(output_path, os.path.basename(fp)) for fp in origin_paths]
            newDimensionIMG = (width, height)
            
            self.progress_bar.setMaximum(100)
            self.progress_bar.setValue(0)
            self.progress_bar.setVisible(True)

            self.thread = ResizeThread(origin_paths, output_paths, newDimensionIMG)
            self.thread.progress.connect(self.progress_bar.setValue)
            self.thread.finished.connect(self.on_resize_complete)
            self.thread.start()
            
        except PermissionError as e:
            QMessageBox.critical(self, 'Erro', f'Erro de permissão: {e}')
        except Exception as e:
            QMessageBox.critical(self, 'Erro', f'Erro ao redimensionar as imagens: {e}')

    def on_resize_complete(self):
        QMessageBox.information(self, 'Sucesso', 'Imagens redimensionadas com sucesso.')
        self.progress_bar.setVisible(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('icons/app_icon.png'))
    app.setFont(QFont('Arial', 12))

    resize_app = ImageResizeApp()
    resize_app.show()
    sys.exit(app.exec_())
