import numpy as np
from PIL import Image

# pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
from torchvision.transforms.functional import to_pil_image

# Daniel
from show_superimposed import show_superimposed

def apply_method(model, method, torchcam_model, instances):
    print(f'method: {method}')

    with torchcam_model as cam_extractor:

        for instance in instances:
    
            # Preprocess your data and feed it to the model
            out = model(instance.batch)
    
            # Retrieve the CAM by passing the class index and the model output
            activation_map = cam_extractor(out.squeeze(0).argmax().item(), out)
            instance.activation_map[method] = activation_map
    
            # Resizing the heatmap
            heatmap_tensor = instance.activation_map[method][0].squeeze(0)
            heatmap_pil = to_pil_image(heatmap_tensor)
            w = instance.batch[0].shape[1]
            h = instance.batch[0].shape[2]
            heatmap_pil_resized = heatmap_pil.resize((w, h), resample=Image.BICUBIC)
    
            resized_img = instance.batch_numpy
    
            show_superimposed(resized_img, heatmap_tensor, heatmap_pil_resized)
            
            # Normalisation based on https://www.statology.org/numpy-normalize-between-0-and-1/
            heatmap_np_resized = np.array(heatmap_pil_resized)
            heatmap_np_resized = (heatmap_np_resized - np.min(heatmap_np_resized))/(np.max(heatmap_np_resized) - np.min(heatmap_np_resized))
            instance.heatmap_resized[method] = heatmap_np_resized
    
            print()

    print()
    print('==============================================')
    print()