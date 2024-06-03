import os
from PIL import Image



# Renderização de imagem ==========================================================================

def resize_image(origin, output, new_dimensions):
    # Verifica permissões de leitura para o arquivo de origem
    if not os.access(origin, os.R_OK):
        raise PermissionError(f"Cannot read file: {origin}")
    
    # Verifica permissões de escrita para o diretório de saída
    output_dir = os.path.dirname(output)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    elif not os.access(output_dir, os.W_OK):
        raise PermissionError(f"Cannot write to directory: {output_dir}")

    image = Image.open(origin)
    resized_image = image.resize(new_dimensions, Image.LANCZOS)

    resized_image.save(output)


    


# Vascolhamento e verificação de arquivo massivo ==================================================

def is_image_file(filename):
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')
    return filename.lower().endswith(image_extensions)

def process_image_file(input_path, output_path, new_dimensions):
    resize_image(input_path, output_path, new_dimensions)

def removeNandSpace(texto):
    caracteres_permitidos = [c for c in texto if not c.isdigit() and not c.isspace()]
    novo_texto = ''.join(caracteres_permitidos)
    return novo_texto

def process_directory(input_dir, output_dir, new_dimensions):
    for root, dirs, files in os.walk(input_dir):
        c = 0
        for file in files:
            if is_image_file(file):
                c +=1
                

                input_path = os.path.join(root, file)
                input_path = input_path.replace('\\', '/')

                
                
                relative_path = os.path.relpath(input_path, input_dir)
                print(removeNandSpace(relative_path).replace('.', f'_{c}_{new_dimensions[0]}x{new_dimensions[1]}.'))
                output_path = os.path.join(output_dir, relative_path)
                
                process_image_file(input_path, output_path, new_dimensions)

                
            else:
                print((f"Arquivo encontrado (nao e imagem): {os.path.join(root, file)}").replace('\\', '/'))
                
        for dir in dirs:
            dirpath = os.path.join(root, dir)
            print((f"Diretorio encontrado: {dirpath}".replace('\\', '/')))

# =================================================================================================

def main(origin_paths, output_paths, new_dimensions):
    process_directory(origin_paths, output_paths, new_dimensions)

    
if __name__ == "__main__":
    origin = "c:/Users/Shizu ^^/Desktop/ShizuImagesRender/ShizuImagesRender/data/input"
    output = origin.replace('input', 'output')
    Nd = (500, 500)
    process_directory(origin, output, Nd)

  