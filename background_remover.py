import os
import io
from rembg import remove
from PIL import Image

def process_background_removal(input_folder, output_folder=None):
    """
    Recorre una carpeta, quita el fondo de las imágenes y las guarda en output_folder.
    """
    if output_folder is None:
        output_folder = os.path.join(input_folder, "output_sin_fondo")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Carpeta creada: {output_folder}")

    valid_extensions = ('.jpg', '.jpeg', '.png')
    
    print(f"--- Iniciando eliminación de fondo en: {input_folder} ---")

    count = 0
    errors = 0

    for root, dirs, files in os.walk(input_folder):
        # Evitar procesar la carpeta de salida
        if os.path.abspath(output_folder) in os.path.abspath(root):
            continue

        for filename in files:
            if filename.lower().endswith(valid_extensions):
                input_path = os.path.join(root, filename)
                
                # Calcular ruta relativa para mantener estructura si se desea, 
                # o simplemente aplanarlo en output.
                # En este script original, parecía plano en 'output'.
                # Vamos a mantener la lógica simple por ahora o mejorarla.
                # Mejor mejora: Replicar estructura relativa.
                rel_path = os.path.relpath(root, input_folder)
                if rel_path == ".":
                    target_dir = output_folder
                else:
                    target_dir = os.path.join(output_folder, rel_path)
                
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir, exist_ok=True)

                print(f"Procesando: {filename}...")

                try:
                    with open(input_path, 'rb') as i:
                        input_image = i.read()

                    output_image = remove(input_image)
                    img = Image.open(io.BytesIO(output_image))

                    name_without_ext = os.path.splitext(filename)[0]
                    output_filename = f"{name_without_ext}_sin_fondo.png"
                    output_path = os.path.join(target_dir, output_filename)

                    img.save(output_path)
                    print(f" -> Guardado: {output_filename}")
                    count += 1

                except Exception as e:
                    print(f"Error procesando {filename}: {e}")
                    errors += 1

    print(f"--- Proceso completado. Procesados: {count}, Errores: {errors} ---")
