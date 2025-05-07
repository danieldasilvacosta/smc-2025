import matplotlib.pyplot as plt

def show_raw_heatmap(activation_map):
    plt.figure(figsize=(2, 2) )
    plt.imshow(activation_map[0].squeeze(0).numpy());
    plt.axis('off');
    plt.show()