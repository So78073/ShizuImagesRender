from PIL import Image
import os
import shutil

def renderImage(input_path, output_path, newdimension): # redimensiona imagem
    try:
        imagem = Image.open(input_path)
        imagem_redimensionada = imagem.resize(newdimension)
        imagem_redimensionada.save(output_path)
        print(f'Imagem redimensionada com sucesso para {newdimension}')
    except Exception as e:
        print(f'Erro ao redimensionar imagem: {e}')


def pathExist(path) : # verifica se o arquivo existe
    return True if os.path.exists(path) else False


def pathCopyInstructions(diretorio): # pega todos as imagens de todos os arquivos
    pathCopyInstruc = []

    for root, dir, files in os.walk(diretorio):
       pathCopyInstruc.append(root)
    
    pathCopyInstruc.pop(0)
    return pathCopyInstruc


def copyFolder(): # reseta a pasta output para criar novos diretorios e arquivos 
    outputFolder = 'C:\\Users\\Shizu ^^\\Desktop\\PyImageProject\\data\\output'

    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)

    else:
        shutil.rmtree(outputFolder)
        os.makedirs(outputFolder)



def createArrayDirOntheOutput(files): #Cria um novo diretorio direcionado ao output
    newPath = []
    for itens in files:
            newPath.append(itens.replace('input', 'output'))
    return newPath


def forDir(newPath):
    for dir in newPath:
        if os.path.isdir:
            os.makedirs(dir)
            
def forImg(oldPath, newDimensionIMG):

    for dir in oldPath:
        diretorio = os.listdir(dir)

        for img in diretorio:
            item = os.path.join(dir, img)    
            if os.path.isfile(item):
                newDimension = newDimensionIMG
                renderImage(item, item.replace('input', 'output'), newDimension)


def createImagensOnNewpath(newPath, oldPath, newDimensionIMG):

    forDir(newPath)
    forImg(oldPath, newDimensionIMG)

# main function #

def main(origem, newDimensionIMG):
    if os.path.exists(origem):

        copyFolder()

        oldPath = pathCopyInstructions(origem)
        
        newPath = createArrayDirOntheOutput(oldPath)

        createArrayDirOntheOutput(newPath)

        createImagensOnNewpath(newPath, oldPath, newDimensionIMG)

    else:                                                                        
        print('O caminho do arquivo não é válido.')
    

