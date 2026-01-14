import os
import shutil
import time
from PIL import Image
import imageio

def get_backup_folder(target_path):
    """
    Creates a backup folder with a timestamp.
    Example: target_path/../backup_YYYYMMDD_HHMMSS
    """
    parent_dir = os.path.dirname(os.path.abspath(target_path))
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    backup_dir = os.path.join(parent_dir, f"backup_{timestamp}")
    return backup_dir

def optimize_image(input_path, backup_root, target_root):
    """
    Converts image to WebP, backs up original, and deletes original.
    """
    try:
        # 1. Setup paths
        filename = os.path.basename(input_path)
        name_no_ext, _ = os.path.splitext(filename)
        dir_path = os.path.dirname(input_path)
        
        # Calculate relative path for backup structure
        rel_path = os.path.relpath(dir_path, target_root)
        if rel_path == ".":
            backup_dir = backup_root
        else:
            backup_dir = os.path.join(backup_root, rel_path)
            
        backup_path = os.path.join(backup_dir, filename)
        output_path = os.path.join(dir_path, f"{name_no_ext}.webp")

        # 2. Backup
        os.makedirs(backup_dir, exist_ok=True)
        shutil.copy2(input_path, backup_path)
        
        # 3. Convert
        with Image.open(input_path) as img:
            img.save(output_path, 'WEBP', quality=90, method=6)
            
        # 4. Verify & Delete
        if os.path.exists(output_path) and os.path.getsize(output_path) > 0:
            os.remove(input_path)
            print(f"[IMG] Converted & Deleted: {filename} -> .webp")
            return True
        else:
            print(f"[ERR] Conversion failed for {filename}, keeping original.")
            return False

    except Exception as e:
        print(f"[ERR] Error processing image {input_path}: {e}")
        return False

def optimize_video(input_path, backup_root, target_root):
    """
    Converts video to WebM, backs up original, and deletes original.
    """
    try:
        # 1. Setup paths
        filename = os.path.basename(input_path)
        name_no_ext, _ = os.path.splitext(filename)
        dir_path = os.path.dirname(input_path)
        
        # Calculate relative path for backup structure
        rel_path = os.path.relpath(dir_path, target_root)
        if rel_path == ".":
            backup_dir = backup_root
        else:
            backup_dir = os.path.join(backup_root, rel_path)
            
        backup_path = os.path.join(backup_dir, filename)
        output_path = os.path.join(dir_path, f"{name_no_ext}.webm")

        # Skip if output already exists (avoid loops if re-running)
        if os.path.exists(output_path):
             # It might be a previous run, check if original is still there
             pass

        # 2. Backup
        os.makedirs(backup_dir, exist_ok=True)
        shutil.copy2(input_path, backup_path)

        # 3. Convert
        # Using imageio with libvpx-vp9 for WebM
        reader = imageio.get_reader(input_path)
        fps = reader.get_meta_data()['fps']
        writer = imageio.get_writer(output_path, fps=fps, codec='libvpx-vp9')

        for frame in reader:
            writer.append_data(frame)
        writer.close()
        reader.close() # Ensure close

        # 4. Verify & Delete
        if os.path.exists(output_path) and os.path.getsize(output_path) > 0:
            os.remove(input_path)
            print(f"[VID] Converted & Deleted: {filename} -> .webm")
            return True
        else:
            print(f"[ERR] Conversion failed for {filename}, keeping original.")
            return False

    except Exception as e:
        print(f"[ERR] Error processing video {input_path}: {e}")
        return False

def process_web_optimization(target_path):
    """
    Main entry point for web optimization command.
    """
    abs_target = os.path.abspath(target_path)
    
    # Define extensions
    img_exts = ('.png', '.jpg', '.jpeg')
    vid_exts = ('.mp4', '.mov', '.avi', '.mkv')
    
    # Create backup root
    backup_root = get_backup_folder(abs_target)
    print(f"--- AssetForge Web Optimizer ---")
    print(f"Target: {abs_target}")
    print(f"Backup Location: {backup_root}")
    print("--------------------------------")

    files_processed = 0
    
    # Walk and process
    for root, dirs, files in os.walk(abs_target):
        # Avoid processing backup folder if it somehow ends up inside target (shouldn't if using ../)
        # But if user target is root 'C:/', backup might be neighbor.
        
        for file in files:
            full_path = os.path.join(root, file)
            
            if file.lower().endswith(img_exts):
                if optimize_image(full_path, backup_root, abs_target):
                    files_processed += 1
            elif file.lower().endswith(vid_exts):
                if optimize_video(full_path, backup_root, abs_target):
                    files_processed += 1
                    
    if files_processed == 0:
        print("\nNo matching files found to optimize.")
        # Optional: Remove empty backup dir if nothing was done
        if os.path.exists(backup_root) and not os.listdir(backup_root):
            os.rmdir(backup_root)
            print("(Cleaned up empty backup folder)")
    else:
        print(f"\n--- Done. Optimized {files_processed} files. ---")
        print(f"Originals backed up at: {backup_root}")
