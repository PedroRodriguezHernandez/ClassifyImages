from PIL import Image


def resize_images(image_path, new_size):
    try:
        img = Image.open(image_path)

        # Resize the image
        img_resized = img.resize(new_size)

        # Make sure it is RGB type
        img_resized = img_resized.convert('RGB')

        return img_resized
    except Exception as e:
        print(f"Error processing image: {e} ")
        return None

