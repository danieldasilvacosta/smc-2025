class Instance:

    def __init__(self, tensor_img, img_pil, file_name, file_path, annotation_file_path):
        self.tensor_img = tensor_img
        self.img_pil = img_pil
        self.file_name = file_name
        self.file_path = file_path
        self.annotation_file_path = annotation_file_path
        self.batch = None
        self.prediction = None
        self.classification = {
            'resnet50': {
                'category_name': '',
                'score': 0.0
            }
        }
        self.batch_numpy = None
        self.activation_map = {}
        self.heatmap_resized = {}
        self.ground_truth_imagenet = None
        self.heatmap_threshold = {}
        self.thresholds_dataframes = {}
        self.threshold_lefts_columns = {}
        self.threshold_rights_columns = {}
        self.threshold_tops_rows = {}
        self.threshold_bottoms_rows = {}
        self.threshold_preds_xmins = {}
        self.threshold_preds_ymins = {}
        self.threshold_preds_xmaxs = {}
        self.threshold_preds_ymaxs = {}
        self.imagenet_resized_gt = None
        self.imagenet_resized_img = None
        self.imagenet_resized_img_with_gt = None
        self.heatmap_bbox = {}
        self.metrics = {
            'imagenet': {
                'jaccard': {'thresholds': []},
                'wjaccard': {},
                'wasserstein': {},
            },
            'appen_intersection': {
                'jaccard': {'thresholds': []},
                'wjaccard': {},
                'wasserstein': {},
            },
            'appen_union': {
                'jaccard': {'thresholds': []},
                'wjaccard': {},
                'wasserstein': {},
            },
            'appen_heatmap': {
                'jaccard': {'thresholds': []},
                'wjaccard': {},
                'wasserstein': {},
            },
        }
        self.gt_appen_bbox = []
        self.gt_appen_bbox_coordinate = []
        self.appen_coord_bbox_intersection = ()
        self.appen_coord_bbox_union = ()
        self.gt_appen_bbox_coordinate_filtered = []
        self.appen_resized_gt_intersection = []
        self.appen_resized_gt_union = []
        self.appen_resized_img_intersection = []
        self.appen_resized_img_union = []
        self.appen_resized_img_with_gt_intersection = []
        self.appen_resized_img_with_gt_union = []
        self.appen_coord_bbox_heatmap_worker = {}
        self.appen_resized_gt_heatmap_worker = {}
        self.appen_resized_img_heatmap_worker = {}
        self.appen_bbox_aggregated_heatmap = []

        
    def __repr__(self): # to human readbility.
        return f'file_name: {self.file_name}'

    def get(self, attr):
        return getattr(self, attr)

    # def __setitem__(self, key, value):
    #     self.__dict__[key] = value 