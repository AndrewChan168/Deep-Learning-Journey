import os
import glob
import torch
import pickle
import numpy as np
import pandas as pd
from PIL import Image
from torch_snippets import find
from torch.utils.data import Dataset

def preprocess_image(img, device):
    img = torch.tensor(img).permute(2,0,1)
    return img.to(device).float()

class ImageLabelDataset(Dataset):
    W, H = 224, 224
    def __init__(self, labels_df, image_root_dir, class2label_dict, device='cpu'):
        self.image_dir = image_root_dir
        self.files = glob.glob(self.image_dir+'/*')
        self.df = labels_df
        self.image_infos = labels_df.ImageID.unique()
        self.class2label = class2label_dict
        self.label2class = {cls:lbl for lbl,cls in class2label_dict.items() }
        self.device = device

    def __getitem__(self, ix):
        # load image
        image_id = self.image_infos[ix]
        img_path = find(image_id, self.files)
        img = Image.open(img_path).convert("RGB")
        # transform image as np array
        # size of image is resized to align with labels
        img = np.array(img.resize((self.W, self.H), resample=Image.BILINEAR))/255.
        # process labels
        df = self.df.copy()
        labels = df[df['ImageID'] == image_id]['LabelName'].values.tolist()
        true_bboxes = df[df['ImageID'] == image_id][['XMin','YMin','XMax','YMax']].values
        true_bboxes[:,[0,2]] *= self.W
        true_bboxes[:,[1,3]] *= self.H
        true_bboxes = true_bboxes.astype(np.uint32).tolist() # convert to absolute coordinates
        # combine labels and true bounding boxes to dictionary
        target_dict = {}
        target_dict['boxes'] = torch.Tensor(true_bboxes).float()
        target_dict['labels'] = torch.Tensor([self.class2label[lbl] for lbl in labels]).long()
        img = preprocess_image(img, self.device)
        return img, target_dict

    def __len__(self):
        return len(self.image_infos)