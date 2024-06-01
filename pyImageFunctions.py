import os
from PIL import Image

def resize_image(origin, output, new_dimensions):
    # Verifica permissões de leitura para o arquivo de origem
    if not os.access(origin, os.R_OK):
        raise PermissionError(f"Cannot read file: {origin}")
    
    # Verifica permissões de escrita para o diretório de saída
    output_dir = os.path.dirname(output)
    if not os.access(output_dir, os.W_OK):
        raise PermissionError(f"Cannot write to directory: {output_dir}")

    image = Image.open(origin)
    resized_image = image.resize(new_dimensions, Image.LANCZOS)
    resized_image.save(output)

def main(origin_paths, output_paths, new_dimensions):
    for origin, output in zip(origin_paths, output_paths):
        resize_image(origin, output, new_dimensions)
