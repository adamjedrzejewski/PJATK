from fastbook import *
from fastai.vision.widgets import *

import coremltools as ct

import pathlib
from pathlib import Path

temp = pathlib.PosixPath
#pathlib.PosixPath = pathlib.WindowsPath # I'm running this script on a Mac

path = Path('dataset_x2')

classes = 'cat', 'dog'

data = DataBlock(
    blocks=(ImageBlock, CategoryBlock),
    get_items=get_image_files,
    splitter=RandomSplitter(valid_pct=0.2,seed=42),
    get_y=parent_label,
    item_tfms=Resize(256) # resize to 256px
)

data = data.new(
    item_tfms=RandomResizedCrop(256, min_scale=0.5), # random resized crop at 256px
    batch_tfms=aug_transforms(xtra_tfms=None)) # default augmentation?

dls = data.dataloaders(path, bs = 32)

learn = cnn_learner(dls, resnet34, metrics=error_rate) # 34 is less than 152

learn.fit_one_cycle(5)
learn.export(fname="model.pkl")


