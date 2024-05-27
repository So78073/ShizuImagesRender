from PIL import Image
import os
import shutil

def renderImage(input_path, output_path, newdimension): 
    try:
        imagem = Image.open(input_path)
        imagem_redimensionada = imagem.resize(newdimension)
        imagem_redimensionada.save(output_path)
        print(f'Imagem redimensionada com sucesso para {newdimension}')
    except Exception as e:
        print(f'Erro ao redimensionar imagem: {e}')

def pathExist(path) : 
    return os.path.exists(path)

def main(origem, output, newDimensionIMG):
    if os.path.exists(origem):
        try:
            renderImage(origem, output, newDimensionIMG)
        except Exception as e:
            print(f'Erro ao redimensionar imagem: {e}')
    else:                                                                        
        print('O caminho do arquivo não é válido.')
