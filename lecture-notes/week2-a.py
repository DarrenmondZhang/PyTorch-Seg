'''
@Author: your name
@Date: 2020-05-05 17:17:08
@LastEditTime: 2020-05-05 17:54:45
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /PyTorch-Seg/lecture-notes/doc/week2-a.py
'''
import sys
sys.path.append('../')

import numpy as np
import pandas as pd
from glob import glob
import base64
from matplotlib import pyplot as plt
import cv2

import torch

from dataset.dataset_unet import mask2data
# from utils.mask_functions import rle2mask

mask_data = mask2data()
print(mask2data)
