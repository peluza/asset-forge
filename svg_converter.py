import os
from vtracer import convert_image_to_svg_py

def process_svg_conversion(input_folder, output_folder=None):
    """
    Convierte imágenes en 'input_folder' a SVG en 'output_folder' usando vtracer.
    """
    if output_folder is None:
        output_folder = os.path.join(input_folder, "output_svg")

    valid_extensions = ('.png', '.jpg', '.jpeg', '.bmp')

    print(f"--- Iniciando conversión a SVG en: {input_folder} ---")
    print(f"--- Salida: {output_folder} ---")

    count = 0
    errors = 0

    for root, dirs, files in os.walk(input_folder):
        if os.path.abspath(output_folder) in os.path.abspath(root):
            continue

        rel_path = os.path.relpath(root, input_folder)
        if rel_path == ".":
            target_dir = output_folder
        else:
            target_dir = os.path.join(output_folder, rel_path)

        if not os.path.exists(target_dir):
            os.makedirs(target_dir, exist_ok=True)

        for filename in files:
            if filename.lower().endswith(valid_extensions):
                input_path = os.path.join(root, filename)
                name_base = os.path.splitext(filename)[0]
                output_path = os.path.join(target_dir, f"{name_base}.svg")

                print(f"Convirtiendo: {filename}")

                try:
                    convert_image_to_svg_py(
                        input_path,
                        output_path,
                        colormode='color',
                        hierarchical='stacked',
                        mode='spline',
                        filter_speckle=2,
                        color_precision=8,
                        layer_difference=10,
                        corner_threshold=60,
                        length_threshold=10,
                        max_iterations=10,
                        splice_threshold=45,
                        path_precision=8
                    )
                    count += 1
                except Exception as e:
                    print(f" [ERROR] {filename}: {e}")
                    errors += 1

    print(f"--- Finalizado. SVG creados: {count}, Errores: {errors} ---")
