from PIL import Image
import os


def convert_to_jpg(image_path):
    image = Image.open(image_path)
    new_image_path = os.path.splitext(image_path)[0] + ".jpg"
    image.convert("RGB").save(new_image_path, "JPEG")
    image.close()
    os.remove(image_path)


def convert_images_to_jpg(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file.lower().endswith((".jpg", ".jpeg")):
                print(f"Skipping {file_path} (already a JPG)")
                continue
            try:
                convert_to_jpg(file_path)
                print(f"Converted {file_path} to JPG")
            except Exception as e:
                print(f"Error converting {file_path}: {e}")


# Usage example
convert_images_to_jpg("webp_input")
