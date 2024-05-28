import pyImageFunctions as pyy
import os

nDim = (500, 500)

origem = os.path.dirname(os.path.abspath(__file__))
origem = os.path.join(origem, 'data', 'input')


print(origem + '\n')

# Verifica se o caminho existe
if os.path.exists(origem):
    print("A origem existe.")
else:
    print("A origem não existe.")

# Verifica se a origem é um diretório válido
if os.path.isdir(origem):
    print("A origem é um diretório válido.")
else:
    print("A origem não é um diretório válido.")

# Verifica se a origem não é válida
if not os.path.exists(origem):
    print("A origem não existe.")
elif not os.path.isdir(origem):
    print("A origem não é um diretório válido.")
else:
    print("A origem existe e é um diretório válido.")


pyy.main(origem, nDim)
