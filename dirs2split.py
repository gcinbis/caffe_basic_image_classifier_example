'''
A simple script for automatically generating train.txt and val.txt files.
This script assumes that the images are stored under `<IMAGE_ROOT>/<classname>/<imagename>`
Before running this script, prepare the classnames.txt file.
Replace the IMAGE_ROOT and TRAIN_RATIO constants below with proper contents.
'''

import params
import os, os.path
import math
import random

IMAGE_ROOT = "/path/to/the/directory/containing/the/images"
TRAIN_RATIO = 0.5 # ratio of images to be used in training over all images

# read list
with open("classnames.txt") as f:
    subdirnames = f.readlines()

# define train/val set for each class
trainfiles = {}
valfiles = {}
for c in xrange(len(subdirnames)):
    curdirname = subdirnames[c].strip()
    subdir = IMAGE_ROOT + "/" + curdirname
    curfiles = [os.path.join(subdir,name) for name in os.listdir(subdir) if os.path.isfile(os.path.join(subdir, name))]
    curntrain = int(math.ceil(len(curfiles) * TRAIN_RATIO))
    trainfiles[c] = curfiles[:curntrain]
    valfiles[c] = curfiles[curntrain:]


def write_list_file(filename,files):
    # merge to an array
    tmplist = []
    for c in xrange(len(files)):
        for x in files[c]:
            tmplist.append(x + " " + str(c) + "\n")

    # shuffle files
    random.shuffle(tmplist)

    # write to disk
    with open(filename,'w') as f:
        for x in tmplist:
            f.write(x)


# print to file
write_list_file("splits/train_ratio" + TRAIN_RATIO + "/train.txt",trainfiles)
write_list_file("splits/train_ratio" + TRAIN_RATIO + "/val.txt",valfiles)

