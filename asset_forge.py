import argparse
import os
import sys

# Import local modules
try:
    from background_remover import process_background_removal
    from svg_converter import process_svg_conversion
    from webp_converter import process_webp_conversion
except ImportError:
    # Support for dev mode execution without installation
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from background_remover import process_background_removal
    from svg_converter import process_svg_conversion
    from webp_converter import process_webp_conversion

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

    # Command: webp
    parser_webp = subparsers.add_parser('webp', help='Generate WebP versions (1x, 2x, 3x) for Apps/Web')
    parser_webp.add_argument('path', nargs='?', default='.', help='Folder or file to process (Default: current)')

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
