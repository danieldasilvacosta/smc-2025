import numpy as np
from PIL import Image, ImageDraw

def resize_image(img):

    img_copy = img.copy()
    # img_copy_np = np.array(img_copy)
    # print(f'img_copy_np.shape: {img_copy_np.shape}')

    # First step # ResNet50_Weights.IMAGENET1K_V2: https://pytorch.org/vision/main/models/generated/torchvision.models.resnet50.html
    first_height = 232
    first_width = 232

    # Checking image position to set new dimensions
    original_width, original_height = img_copy.size
    if original_width/original_height < 1: # portrait position images
        first_height = int(original_height * first_width / original_width)
    else: # landscape position images
        first_width = int(original_width * first_height / original_height)

    # print(f'img_copy.size: {img_copy.size}')
    # img_copy.thumbnail((first_width, first_height), resample=Image.BILINEAR)
    img_copy = img_copy.resize((first_width, first_height), resample=Image.BILINEAR)
    # print(f'img_copy.size: {img_copy.size}')

    # Second step # ResNet50_Weights.IMAGENET1K_V2: https://pytorch.org/vision/main/models/generated/torchvision.models.resnet50.html
    second_height = 224
    second_width = 224

    # Centralizing
    img_copy_np = np.array(img_copy)
    height_center = int(first_height/2)
    width_center = int(first_width/2)
    resized_img_np = img_copy_np[height_center - int(second_height/2) : height_center + int(second_height/2),
                        width_center - int(second_width/2) : width_center + int(second_width/2)]

    # https://stackoverflow.com/questions/10965417/how-to-convert-a-numpy-array-to-pil-image-applying-matplotlib-colormap
    # resized_img = Image.fromarray(np.uint8(resized_img_np)).convert('RGB')
    resized_img = Image.fromarray(resized_img_np.astype('uint8'), 'RGB')

    return resized_img