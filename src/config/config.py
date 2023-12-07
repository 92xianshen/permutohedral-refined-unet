"""
Experimental configuration.

Experiments
    1. Hyperparameter test.
        1.1 theta_beta = 0.03125 with theta_alpha = 120.0 (4), 80.0 (1), 40.0 (2), 10.0 (3). 
        1.2 theta_alpha = 80.0 with theta_beta = 0.03125 (1), 0.0625 (2), 0.125 (3), 0.25 (4).
    2. Exploration of multi-spectral features.
        2.1 self.img_channel_list, self.vis_channel_list = [4, 3, 2], None # RGB, acquired.
        2.2 self.img_channel_list, self.vis_channel_list = list(range(self.n_bands)), [4, 3, 2] # Seven-band.
    3. Ablation study with respect to the CRF and the bilateral message-passing step.
        3.1 run ablation.py
"""

class Config:
    def __init__(self) -> None:
        # - Hyperparameters
        self.theta_alpha, self.theta_beta, self.theta_gamma = 80.0, 0.03125, 3.0 # critical hyperparameters
        self.img_channel_list, self.vis_channel_list = [4, 3, 2], None # bilateral features for CRF, RGB now

        # - Input and output
        self.data_path = "../test_case/"
        # self.save_path = "../output/a={}, b={}, r={}".format(self.theta_alpha, self.theta_beta, self.theta_gamma) # Perm. RFN. UNet
        self.save_path = "../output_wobilateral/a={}, b={}, r={}".format(self.theta_alpha, self.theta_beta, self.theta_gamma) # Perm. RFN. UNet w/o bilateral message-passing step
        self.save_info_fname = "rfn.csv"

        # - Model parameters
        self.n_bands = 7 # number of inputs of UNet
        self.n_classes = 4 # number of classes of UNet output
        self.model_path = "unary_model/"
        self.crop_height = 512
        self.crop_width = 512
        self.bilateral_compat = 10.0
        self.spatial_compat = 3.0
        self.n_iterations = 10
