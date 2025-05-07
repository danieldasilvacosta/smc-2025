import numpy as np
from PIL import Image, ImageDraw

# Daniel
from resize_image import resize_image

def resize_gt_dim(instance, gt_source, source_type='attr', source_key=None):

    img = Image.open(instance.file_path)
    img_np = np.array(img)
    original_height, original_width = img_np.shape[0], img_np.shape[1]

    # resizing the original image
    resized_img = resize_image(img)

    # First step # ResNet50_Weights.IMAGENET1K_V2: https://pytorch.org/vision/main/models/generated/torchvision.models.resnet50.html
    first_height = 232
    first_width = 232

    # Checking image position to set new dimensions
    if original_width/original_height < 1: # portrait position images
        first_height = int(original_height * first_width / original_width)
    else: # landscape position images
        first_width = int(original_width * first_height / original_height)

    img_copy = img.copy()
    img_copy = img_copy.resize((first_width, first_height), resample=Image.BILINEAR)

    width_scale = first_width / original_width
    height_scale = first_height / original_height

    # each box is a list of coordinates [x1, y1, x2, y2]
    # scale the bounding box according to the scale factors
    height_center = int(first_height/2)
    width_center = int(first_width/2)

    resized_w, resized_h = resized_img.size
    diff_h = (first_height - resized_h) / 2
    diff_w = (first_width - resized_w) / 2

    # print(f'gt_source: {gt_source}')
    # print(f'source_key: {source_key}')
    ground_truth = None
    if source_type == 'attr':
        ground_truth = instance.get(gt_source)
    elif source_type == 'dict':
        ground_truth = instance.get(gt_source)[source_key]
        
    xmin = (ground_truth[0] * width_scale ) - diff_w
    ymin = (ground_truth[1] * height_scale ) - diff_h
    xmax = (ground_truth[2] * width_scale ) - diff_w
    ymax = (ground_truth[3] * height_scale ) - diff_h

    # Remove values less than zero to the calculation of Weighted Jaccard.
    xmin = 0 if xmin < 0 else xmin
    ymin = 0 if ymin < 0 else ymin
    xmax = 0 if xmax < 0 else xmax
    ymax = 0 if ymax < 0 else ymax

    # Second step # ResNet50_Weights.IMAGENET1K_V2: https://pytorch.org/vision/main/models/generated/torchvision.models.resnet50.html
    # Remove values greater than the dimensions of ResNet50 format to the calculation of Weighted Jaccard.
    second_height = second_width = 224
    xmin = second_height if xmin > second_height else xmin
    ymin = second_height if ymin > second_height else ymin
    xmax = second_height if xmax > second_height else xmax
    ymax = second_height if ymax > second_height else ymax

    resized_gt = [
        round(xmin),
        round(ymin),
        round(xmax),
        round(ymax)
    ]

    # Show original image and original ground-truth.
    # print()
    draw = ImageDraw.Draw(img)
    draw.rectangle(ground_truth,
                   fill=None,
                   outline='blue',
                   width=2)
    # display(img)

    # Show resized image and resized ground-truth.
    resized_img_with_gt = resized_img.copy()
    draw = ImageDraw.Draw(resized_img_with_gt)
    draw.rectangle(resized_gt,
                   fill=None,
                   # outline='green',
                   outline='blue',
                   width=2)

    return resized_gt, resized_img, resized_img_with_gt