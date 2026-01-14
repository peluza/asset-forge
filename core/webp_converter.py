import os
from PIL import Image

def process_webp_conversion(input_folder, output_folder=None, quality=90):
    """
    Genera versiones WebP (1x, 2x, 3x) de las imágenes en input_folder.
    Asume que la entrada es 3.0x (alta resolución).
    """
    if output_folder is None:
        output_folder = os.path.join(input_folder, "output_webp")

    valid_extensions = ('.png', '.jpg', '.jpeg')

    print(f"--- Generando WebP (1x, 2x, 3x) desde: {input_folder} ---")
    
    count = 0
    
    for root, dirs, files in os.walk(input_folder):
        # Evitar procesar carpeta de salida, aunque sea recursivo
        if os.path.abspath(output_folder) in os.path.abspath(root):
            continue

        for filename in files:
            if filename.lower().endswith(valid_extensions):
                input_path = os.path.join(root, filename)
                name_sin_ext = os.path.splitext(filename)[0]

                rel_path = os.path.relpath(root, input_folder)
                
                if rel_path == ".":
                    base_dir = output_folder
                else:
                    base_dir = os.path.join(output_folder, rel_path)

                dir_2x = os.path.join(base_dir, '2.0x')
                dir_3x = os.path.join(base_dir, '3.0x')

                os.makedirs(base_dir, exist_ok=True)
                os.makedirs(dir_2x, exist_ok=True)
                os.makedirs(dir_3x, exist_ok=True)

                print(f"Procesando: {filename} ... ", end="", flush=True)

                try:
                    with Image.open(input_path) as img:
                        w, h = img.size
                        
                        # 3.0x (Original)
                        ruta_3x = os.path.join(dir_3x, f"{name_sin_ext}.webp")
                        img.save(ruta_3x, 'WEBP', quality=quality, method=6)

                        # 2.0x (2/3)
                        w_2x, h_2x = int(w * 0.666), int(h * 0.666)
                        if w_2x > 0 and h_2x > 0:
                            img_2x = img.resize((w_2x, h_2x), Image.Resampling.LANCZOS)
                            ruta_2x = os.path.join(dir_2x, f"{name_sin_ext}.webp")
                            img_2x.save(ruta_2x, 'WEBP', quality=quality, method=6)

                        # 1.0x (1/3)
                        w_1x, h_1x = int(w * 0.333), int(h * 0.333)
                        if w_1x > 0 and h_1x > 0:
                            img_1x = img.resize((w_1x, h_1x), Image.Resampling.LANCZOS)
                            ruta_1x = os.path.join(base_dir, f"{name_sin_ext}.webp")
                            img_1x.save(ruta_1x, 'WEBP', quality=quality, method=6)
                    
                    count += 1
                    print("OK")
                except Exception as e:
                    print(f"ERROR: {e}")

    print(f"--- Listo. Se generaron sets para {count} imágenes. ---")
