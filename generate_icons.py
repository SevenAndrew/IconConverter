import os
import json
from tkinter import Tk, Button, Label, filedialog
from PIL import Image

ICON_SIZES = [
    (16, "1x"), (16, "2x"),
    (32, "1x"), (32, "2x"),
    (128, "1x"), (128, "2x"),
    (256, "1x"), (256, "2x"),
    (512, "1x"), (512, "2x"),
]

def generate_appiconset(input_file, output_folder):
    appiconset_folder = os.path.join(output_folder, "AppIcon.appiconset")
    if not os.path.exists(appiconset_folder):
        os.makedirs(appiconset_folder)

    contents = {
        "images": [],
        "info": {
            "version": 1,
            "author": "xcode"
        }
    }

    with Image.open(input_file) as img:
        for size, scale in ICON_SIZES:
            pixel_size = size * (2 if scale == "2x" else 1)
            resized_img = img.resize((pixel_size, pixel_size), Image.Resampling.LANCZOS)
            filename = f"icon_{size}x{size}@{scale}.png"
            output_path = os.path.join(appiconset_folder, filename)
            resized_img.save(output_path, "PNG")
            contents["images"].append({
                "size": f"{size}x{size}",
                "idiom": "mac",
                "filename": filename,
                "scale": scale
            })

    # Write Contents.json
    contents_path = os.path.join(appiconset_folder, "Contents.json")
    with open(contents_path, "w") as f:
        json.dump(contents, f, indent=4)

    print(f"AppIcon.appiconset created in {appiconset_folder}")

def select_input_file():
    input_file = filedialog.askopenfilename(title="Select Input Icon", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if input_file:
        input_label.config(text=f"Input File: {input_file}")
        app_data["input_file"] = input_file

def select_output_folder():
    output_folder = filedialog.askdirectory(title="Select Output Folder")
    if output_folder:
        output_label.config(text=f"Output Folder: {output_folder}")
        app_data["output_folder"] = output_folder

def generate_icons():
    input_file = app_data.get("input_file")
    output_folder = app_data.get("output_folder")
    if input_file and output_folder:
        generate_appiconset(input_file, output_folder)
    else:
        print("Please select both input file and output folder")

app_data = {}

root = Tk()
root.title("Icon Converter")

input_label = Label(root, text="Input File: Not selected")
input_label.pack()

input_button = Button(root, text="Select Input File", command=select_input_file)
input_button.pack()

output_label = Label(root, text="Output Folder: Not selected")
output_label.pack()

output_button = Button(root, text="Select Output Folder", command=select_output_folder)
output_button.pack()

generate_button = Button(root, text="Generate Icons", command=generate_icons)
generate_button.pack()

exit_button = Button(root, text="Exit", command=root.quit)
exit_button.pack()

root.mainloop()