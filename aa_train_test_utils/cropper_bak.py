from os import listdir, makedirs
from os.path import join, isfile, exists
from PIL import Image

input_folder = "crop_input_folder"
output_folder = "crop_output_folder"
new_size = (512, 512)

if not exists(output_folder):
    makedirs(output_folder)
if not exists(input_folder):
    makedirs(input_folder)

files = [f for f in listdir(input_folder) if isfile(join(input_folder, f))]

for f in files:
    try:
        img = Image.open(join(input_folder, f))
        img.thumbnail(new_size)
        width, height = img.size
        left = (width - new_size[0]) / 2
        top = (height - new_size[1]) / 2
        right = (width + new_size[0]) / 2
        bottom = (height + new_size[1]) / 2
        img = img.crop((left, top, right, bottom))
        img.save(join(output_folder, f))
    except Exception as e:
        print(f"Error processing file {f}: {e}")
