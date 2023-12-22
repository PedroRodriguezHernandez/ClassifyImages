from PIL import Image


def resize_images(image_path, new_size):
    img = Image.open(image_path)

    # Resize the image
    img_resized = img.resize(new_size)

    # Make sure it is RGB type
    if img_resized.mode == 'RGBA':
        img_resized = img_resized.convert('RGB')

    return img_resized
