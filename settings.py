import pickle

SETTINGS = {
    'experiment_id': '20250104-1042',
    'imagenet_class_id': 'n02085620', # Chihuahua
    'images_folder': 'C:/dev/doutorado/imagenet-object-localization-challenge/ILSVRC/Data/CLS-LOC/train/',
    'annotations_imagenet_folder': 'C:/dev/doutorado/imagenet-object-localization-challenge/ILSVRC/Annotations/CLS-LOC/train/',
    'total_images_to_show': 20,
    # 'selected_images': ['n02085620_1312.JPEG', 'n02085620_242.JPEG'],
    # 'methods': ['gradcam', 'smoothgradcampp'],
    'selected_images': ['n02085620_1312.JPEG', 'n02085620_242.JPEG', 'n02085620_3078.JPEG', 'n02085620_11143.JPEG', \
                        'n02085620_2163.JPEG', 'n02085620_199.JPEG', 'n02085620_1994.JPEG', 'n02085620_1558.JPEG', \
                        'n02085620_7243.JPEG', 'n02085620_27480.JPEG', 'n02085620_7234.JPEG', 'n02085620_5002.JPEG', \
                        'n02085620_5071.JPEG', 'n02085620_44901.JPEG', 'n02085620_8174.JPEG', 'n02085620_5096.JPEG', \
                        'n02085620_5542.JPEG', 'n02085620_5629.JPEG', 'n02085620_7697.JPEG', 'n02085620_400.JPEG'],
    # 'methods': ['gradcam', 'gradcampp', 'smoothgradcampp', 'xgradcam', 'layercam', \
    #              'cam', 'scorecam', 'sscam', 'iscam'],
    'methods': ['gradcam', 'gradcampp', 'smoothgradcampp', 'xgradcam', 'layercam', \
                 'cam', 'scorecam', 'sscam', 'iscam'],
    'thresholds': [.0, .1, .2, .3, .4, .5, .6, .7, .8, .9],
    # 'instances_pkl_file_name': 'instances.pkl',
    # 'annotations_imagenet_pkl_file_name': 'annotations_imagenet.pkl',
    'methods_pkl_file_name': 'methods.pkl',
    'show_logs': True,
    # 'text_style': {
    #     'PURPLE': '\033[95m',
    #     'CYAN': '\033[96m',
    #     'DARKCYAN': '\033[36m',
    #     'BLUE': '\033[94m',
    #     'GREEN': '\033[92m',
    #     'YELLOW': '\033[93m',
    #     'RED': '\033[91m',
    #     'BOLD': '\033[1m',
    #     'UNDERLINE': '\033[4m',
    #     'END': '\033[0m',
    # }
}
SETTINGS['images_folder'] = SETTINGS['images_folder'] + SETTINGS['imagenet_class_id']
SETTINGS['annotations_imagenet_folder'] = SETTINGS['annotations_imagenet_folder'] + SETTINGS['imagenet_class_id']

# instances_pkl_file_name_split = SETTINGS['instances_pkl_file_name'].split('.')
# SETTINGS['instances_pkl_file_name'] = instances_pkl_file_name_split[0] + '--' + SETTINGS['experiment_id'] + '.pkl'

# annotations_imagenet_pkl_file_name_split = SETTINGS['annotations_imagenet_pkl_file_name'].split('.')
# SETTINGS['annotations_imagenet_pkl_file_name'] = annotations_imagenet_pkl_file_name_split[0] + '--' + SETTINGS['experiment_id'] + '.pkl'

# methods_pkl_file_name_split = SETTINGS['methods_pkl_file_name'].split('.')
# SETTINGS['methods_pkl_file_name'] = methods_pkl_file_name_split[0] + '--' + SETTINGS['experiment_id'] + '.pkl'

with open(SETTINGS['methods_pkl_file_name'], 'wb') as f:
    pickle.dump(SETTINGS['methods'], f)

print('SETTINGS:')
for key in SETTINGS:
    print()
    print(f'{key}: {SETTINGS[key]}')