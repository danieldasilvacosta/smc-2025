from PIL import ImageDraw
from intersection_over_union import intersection_over_union
from weighted_jaccard import weighted_jaccard
import numpy as np
from scipy.stats import wasserstein_distance

# Daniel
from settings import SETTINGS

def apply_metrics(method, instances, show_logs = True):

    for instance in instances:
    
        # load the image
        img = instance.imagenet_resized_img.copy()
    
        # draw the ground-truth bounding box along with the predicted bounding box
        resized_gt = instance.imagenet_resized_gt
        draw = ImageDraw.Draw(img)
        draw.rectangle(resized_gt,
                       fill=None,
                       outline='blue',
                       width=2)
    
        # Draw one rectangle for each heatmap.
        if show_logs:
            print(f'instance.file_name: {instance.file_name}')

        # Intersection Over Union
        instance.metrics['imagenet']['jaccard'][method] = {'thresholds': {}}
        for count, threshold in enumerate(SETTINGS['thresholds']):
            threshold = str(threshold)
            img_copy = img.copy()
            draw = ImageDraw.Draw(img_copy)
            heatmap_bbox = instance.heatmap_bbox[method]['thresholds'][threshold]
            draw.rectangle(heatmap_bbox,
                           fill=None,
                           outline='red',
                           width=2)

            instance.metrics['imagenet']['jaccard'][method]['thresholds'][threshold] = intersection_over_union(resized_gt, heatmap_bbox)
        
            heatmap_resized = instance.heatmap_resized[method]
            height = heatmap_resized.shape[0]
            width = heatmap_resized.shape[1]
        
            gt_xmin = instance.imagenet_resized_gt[0]
            gt_ymin = instance.imagenet_resized_gt[1]
            gt_xmax = instance.imagenet_resized_gt[2]
            gt_ymax = instance.imagenet_resized_gt[3]
            img_sized_gt = np.zeros((height, width))
            img_sized_gt[gt_ymin : gt_ymax, gt_xmin : gt_xmax] = 1

            if show_logs:
                print()
                print(f'Explainability method: {method}')
                print(f"IoU: {instance.metrics['imagenet']['jaccard'][method]['thresholds'][threshold]:.4f}")
                print(f'Threshold: {threshold}')
                display(img_copy)

        # WJaccard
        instance.metrics['imagenet']['wjaccard'][method] = weighted_jaccard(heatmap_resized, img_sized_gt)

        # Wasserstein
        instance.metrics['imagenet']['wasserstein'][method] = wasserstein_distance(heatmap_resized.flatten(), img_sized_gt.flatten())

        if show_logs:
            print()
            print('=========================================')
            print()