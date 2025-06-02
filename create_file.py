import os
import re

folder_name_pascal_case = input("Folder name: ")

def pascal_to_snake_case(name):
    s1 = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

file_base_name = pascal_to_snake_case(folder_name_pascal_case)

file_extension = "py"
file_full_name = f"{file_base_name}.{file_extension}"

full_file_path = os.path.join(folder_name_pascal_case, file_full_name)

try:
    os.makedirs(folder_name_pascal_case, exist_ok=True)

    try:
        with open(full_file_path, 'a') as f:
            pass 

    except IOError as e: 
        print(f"Error al crear/tocar el archivo '{file_full_name}': {e}")

except OSError as e: 
    print(f"Error al crear el directorio '{folder_name_pascal_case}': {e}")


if os.path.exists(full_file_path):
    print(f"Verificación: El archivo '{full_file_path}' existe en el sistema de archivos.")
else:
    print(f"Verificación: El archivo '{full_file_path}' NO existe en el sistema de archivos.")