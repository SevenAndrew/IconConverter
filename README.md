feat: Add Python script for App Icon generation

Description:
- Introduced a Python script (`generate_icons.py`) to automate the creation of macOS app icons in required resolutions.
- The script supports generating `.appiconset` for Xcode, including properly scaled PNG files and a `Contents.json` configuration file.

Features:
1. Generates icons for multiple resolutions (16x16 to 512x512 @1x and @2x).
2. Automatically creates an `.appiconset` folder with a valid `Contents.json` for Xcode.
3. Supports high-resolution input images and ensures high-quality scaling.

Usage:
- Run `generate_icons.py` with a high-resolution input file and specify the output folder.
- The generated `.appiconset` can be directly added to `Assets.xcassets` in Xcode.

Next Steps:
- Add support for other platforms (e.g., iOS, Android) in the icon generator.
- Implement additional error handling for invalid inputs or file formats.
