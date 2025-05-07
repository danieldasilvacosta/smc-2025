import matplotlib.pyplot as plt

# pip install torchcam
from torchcam.utils import overlay_mask

# pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
from torchvision.transforms.functional import to_pil_image

def show_superimposed(resized_img, heatmap_tensor, heatmap_pil_resized):
    superimposed_img = overlay_mask(to_pil_image(resized_img),
                                to_pil_image(heatmap_tensor, mode='F'),
                                colormap='hot_r',
                                alpha=0.7)
    
    fig, axes = plt.subplots(1, 3, figsize=(5, 5))
    axes[0].set_title('Resized Image')
    axes[0].imshow(resized_img)
    axes[0].set_axis_off()
    axes[1].set_title('Heatmap')
    axes[1].imshow(heatmap_pil_resized, cmap='gray')
    axes[1].set_axis_off()
    axes[2].set_title('Superimposed Image')
    axes[2].imshow(superimposed_img)
    axes[2].set_axis_off()
    plt.subplots_adjust(bottom=0.5, right=1.5, top=0.9)
    plt.show()