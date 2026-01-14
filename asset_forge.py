import argparse
import os
import sys

# Import local modules
try:
    from core.background_remover import process_background_removal
    from core.svg_converter import process_svg_conversion
    from core.webp_converter import process_webp_conversion
    from core.webm_converter import process_webm_conversion
    from core.web_optimizer import process_web_optimization
except ImportError:
    # Support for dev mode execution without installation
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from core.background_remover import process_background_removal
    from core.svg_converter import process_svg_conversion
    from core.webp_converter import process_webp_conversion
    from core.webm_converter import process_webm_conversion
    from core.web_optimizer import process_web_optimization

def main():
    parser = argparse.ArgumentParser(
        description="AssetForge: Professional Image Processing Tool.",
        epilog="Examples:\n  assetforge remove-bg .\n  assetforge webp ./assets\n  assetforge svg image.png",
        formatter_class=argparse.RawTextHelpFormatter
    )

    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Command: remove-bg
    parser_bg = subparsers.add_parser('remove-bg', help='Remove background from images (PNG/JPG)')
    parser_bg.add_argument('path', nargs='?', default='.', help='Folder or file to process (Default: current)')
    
    # Command: svg
    parser_svg = subparsers.add_parser('svg', help='Convert images to vectorized SVG')
    parser_svg.add_argument('path', nargs='?', default='.', help='Folder or file to process (Default: current)')

    # Command: webp (images)
    parser_webp = subparsers.add_parser('webp', help='Generate WebP versions (1x, 2x, 3x) for Apps/Web')
    parser_webp.add_argument('path', nargs='?', default='.', help='Folder or file to process (Default: current)')

    # Command: webm (video)
    parser_webm = subparsers.add_parser('webm', help='Convert videos (mp4/mov/avi) to WebM')
    parser_webm.add_argument('path', nargs='?', default='.', help='Folder or file to process (Default: current)')

    # Command: web (Aggressive Optimization)
    parser_web = subparsers.add_parser('web', help='Aggressive Optimization: Convert Images->WebP, Video->WebM, Backup & Delete Originals')
    parser_web.add_argument('path', nargs='?', default='.', help='Folder or file to process (Default: current)')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    
    # Normalize path (use getcwd if '.', else expand)
    if args.path == '.':
        target_path = os.getcwd()
    else:
        target_path = os.path.abspath(args.path)

    # print_banner removed as requested
    
    print(f"Target: {target_path}")

    if not os.path.exists(target_path):
        print(f"[ERROR] Path does not exist: {target_path}")
        sys.exit(1)

    try:
        if args.command == 'remove-bg':
            process_background_removal(target_path)
        elif args.command == 'svg':
            process_svg_conversion(target_path)
        elif args.command == 'webp':
            process_webp_conversion(target_path)
        elif args.command == 'webm':
            process_webm_conversion(target_path)
        elif args.command == 'web':
            process_web_optimization(target_path)
        else:
            parser.print_help()

    except KeyboardInterrupt:
        print("\n[!] Operation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n[FATAL ERROR] An unexpected error occurred: {e}")
        print("Please report this bug on the repository.")
        sys.exit(1)

if __name__ == "__main__":
    main()
