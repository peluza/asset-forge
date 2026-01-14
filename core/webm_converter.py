import os
import imageio
from concurrent.futures import ThreadPoolExecutor

def convert_to_webm(file_path):
    """
    Convierte un archivo de video a formato WebM usando imageio.
    """
    try:
        filename, _ = os.path.splitext(file_path)
        output_path = f"{filename}.webm"
        
        # Evitar re-procesar si ya existe
        if os.path.exists(output_path):
            print(f"[SKIP] Ya existe: {output_path}")
            return

        print(f"[PROCESANDO] {file_path} -> .webm")
        
        # Leemos el video y lo guardamos comprimido en webm
        reader = imageio.get_reader(file_path)
        fps = reader.get_meta_data()['fps']
        writer = imageio.get_writer(output_path, fps=fps, codec='libvpx-vp9', quality=None, bitrate=None)

        for frame in reader:
            writer.append_data(frame)
        
        writer.close()
        print(f"[EXITO] Generado: {output_path}")

    except Exception as e:
        print(f"[ERROR] Falló {file_path}: {e}")

def process_webm_conversion(input_path):
    """
    Recorre el directorio o archivo y convierte videos a WebM.
    """
    video_extensions = ('.mp4', '.mov', '.avi', '.mkv')
    tasks = []

    if os.path.isfile(input_path):
        if input_path.lower().endswith(video_extensions):
            convert_to_webm(input_path)
        else:
            print("[INFO] El archivo no es un video compatible (.mp4, .mov, .avi, .mkv)")
        return

    # Si es directorio
    with ThreadPoolExecutor() as executor:
        for root, _, files in os.walk(input_path):
            for file in files:
                if file.lower().endswith(video_extensions):
                    full_path = os.path.join(root, file)
                    tasks.append(executor.submit(convert_to_webm, full_path))

    if not tasks:
        print("[INFO] No se encontraron videos en la ruta.")
    else:
        # Esperar a que terminen
        for task in tasks:
            task.result()
