# PlacesCNN to predict the scene category, attribute, and class activation map in a single pass
# by Bolei Zhou, sep 2, 2017

import torch
from torch.autograd import Variable as V
import torchvision.models as models
from torchvision import transforms as trn
from torch.nn import functional as F
import os
import numpy as np
import cv2
from PIL import Image
from .wideresnet import resnet18
from functools import partial
import pdb

def load_labels():
    # prepare all the labels
    # scene category relevant
    file_name_category = 'categories_places365.txt'
    if not os.access(file_name_category, os.W_OK):
        synset_url = 'https://raw.githubusercontent.com/csailvision/places365/master/categories_places365.txt'
        os.system('wget ' + synset_url)
    classes = list()
    with open(file_name_category) as class_file:
        for line in class_file:
            classes.append(line.strip().split(' ')[0][3:])
    classes = tuple(classes)

    # indoor and outdoor relevant
    file_name_IO = 'IO_places365.txt'
    if not os.access(file_name_IO, os.W_OK):
        synset_url = 'https://raw.githubusercontent.com/csailvision/places365/master/IO_places365.txt'
        os.system('wget ' + synset_url)
    with open(file_name_IO) as f:
        lines = f.readlines()
        labels_IO = []
        for line in lines:
            items = line.rstrip().split()
            labels_IO.append(int(items[-1]) -1) # 0 is indoor, 1 is outdoor
    labels_IO = np.array(labels_IO)

    # scene attribute relevant
    file_name_attribute = 'labels_sunattribute.txt'
    if not os.access(file_name_attribute, os.W_OK):
        synset_url = 'https://raw.githubusercontent.com/csailvision/places365/master/labels_sunattribute.txt'
        os.system('wget ' + synset_url)
    with open(file_name_attribute) as f:
        lines = f.readlines()
        labels_attribute = [item.rstrip() for item in lines]
    file_name_W = 'W_sceneattribute_wideresnet18.npy'
    if not os.access(file_name_W, os.W_OK):
        synset_url = 'http://places2.csail.mit.edu/models_places365/W_sceneattribute_wideresnet18.npy'
        os.system('wget ' + synset_url)
    W_attribute = np.load(file_name_W)

    return classes, labels_IO, labels_attribute, W_attribute

def hook_feature(module, input, output, avgpool_out):
    avgpool_out[0] = np.squeeze(output.data.cpu().numpy())


def returnTF():
# load the image transformer
    tf = trn.Compose([
        trn.Resize((224,224)),
        trn.ToTensor(),
        trn.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    return tf


def load_model(avgpool_out):
    # this model has a last conv feature map as 14x14

    model_file = 'wideresnet18_places365.pth.tar'
    if not os.access(model_file, os.W_OK):
        os.system('wget http://places2.csail.mit.edu/models_places365/' + model_file)

    model = resnet18(num_classes=365)
    checkpoint = torch.load(model_file, map_location=lambda storage, loc: storage)
    state_dict = {str.replace(k,'module.',''): v for k,v in checkpoint['state_dict'].items()}
    model.load_state_dict(state_dict)
    model.eval()

    features_names = ['avgpool']
    for name in features_names:
        model._modules.get(name).register_forward_hook(partial(hook_feature, avgpool_out=avgpool_out))
    return model

class SceneDetector:
    def __init__(self):
        self.avgpool_out = [None]
        self.model = load_model(self.avgpool_out).cuda()
        self.classes, self.labels_IO, self.labels_attribute, self.W_attribute = load_labels()
        self.tf = returnTF()

    def predict(self, img):
        input_img = V(self.tf(img).unsqueeze(0)).cuda()
        
        result = {}

        # forward pass
        logit = self.model.forward(input_img)
        h_x = F.softmax(logit, 1).data.squeeze()
        probs, idx = h_x.sort(0, True)
        probs = probs.cpu().numpy()
        idx = idx.cpu().numpy()

        # output the IO prediction
        io_image = np.mean(self.labels_IO[idx[:10]]) # vote for the indoor or outdoor
        result['type_of_env'] = 'indoor' if (io_image < 0.5) else 'outdoor'

        # output the prediction of scene category
        result['scene_categories'] = {}
        for i in range(0, 5):
            result['scene_categories'][self.classes[idx[i]]] = float(probs[i])

        # output the scene attributes
        responses_attribute = self.W_attribute.dot(self.avgpool_out[0])
        idx_a = np.argsort(responses_attribute)
        scene_attrs = [self.labels_attribute[idx_a[i]] for i in range(-1,-10,-1)]
        result['scene_attributes'] = scene_attrs

        self.avgpool_out[0] = None

        return result

    def predict_from_path(self, path):
        return self.predict(Image.open(path))

