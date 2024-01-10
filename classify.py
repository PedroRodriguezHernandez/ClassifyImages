import os
import random
import shutil
from resize import resize_images

def move_resize_images(source_folder, destination_folder, percentage, new_size):
    os.makedirs(destination_folder, exist_ok=True)

    # List all images in the source folder
    all_images = os.listdir(source_folder)
    total_images = 316 #There are 316 or more images in the original dataset

    # Calculate the number of images to move
    num_images_to_move = int(total_images * percentage)

    # Select random images
    images_to_move = random.sample(all_images, num_images_to_move)

    # Move selected images to destination directory
    for image in images_to_move:
        source_path = os.path.join(source_folder, image)
        destination_path = os.path.join(destination_folder, image)
        resize_images(source_path, new_size).save(destination_path)
        os.remove(source_path)


