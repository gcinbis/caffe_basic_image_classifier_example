---
title: Caffe Basic Image Classifier
description: A Basic Image Classifier Fine-tuning and Image Classification Example in Caffe
---

# Introduction

This is a basic image classification example in Caffe (under Linux), using C++. The example is provided for instructional purposes.

The main code is minimalistic, and requires only basic linux utilities and the development environment
necessary to compile the Caffe library.

# Install Caffe

Compile Caffe under some directory (`CAFFEROOT`) following the instructions in
http://caffe.berkeleyvision.org/installation.html

Note that you don't need root priviledges to perform this step. `CAFFEROOT` can be something like `~/caffe`.
Also, you don't need a full-fledged installation. For instance, the GPU support and the python interface
are not crucial.

Add the following line to your `~/.bashrc` (or `~/.profile`, depending on your system settings):
```
export CAFFEROOT="/path/to/your/caffe/installation"
```
When you open a new terminal, `echo $CAFFEROOT` should print the Caffe path properly.

Beware that compilation may not be trivial, especially if you are unfamiliar with the Linux environment.
If you encounter any issues, search about it in Caffe forums, stackoverflow, etc: it is likely that other people
have encountered similar issues.

Finally, execute the following to download the ImageNet statistics that are needed for using the pre-trained
Caffe model:
```
cd $CAFFEROOT/data/ilsvrc12
./get_ilsvrc_aux.sh
```

# Build a training and a validation set
Fill in classnames.txt, train.txt and val.txt following the instructions provided in the template files.

# Train (fine-tune) the Caffe model using your training set
Replace `CAFFEROOT` entries in `train_val.prototxt` with the actual path of the caffe installation.

Use the following command to start the training procedure.
```
$CAFFEROOT/build/tools/caffe train -solver solver.prototxt \
    -weights $CAFFEROOT/models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel -gpu 0
```
Since we initialize our model parameteres using `bvlc_reference_caffenet.caffemodel`, this procedure is known
as fine-tuning. During training, caffe will occasionally print performance estimations made on 
validation set samples. You can tune the architecture details and/or optimization hyper-parameters 
based on the validation set performance.

# Apply the classifier to novel images
In order to apply your classifier to a test image (ie. an image that is not included in the train or the
validation set), use the following commands:
```
test_image_path=/path/to/test/file.jpg
model_file=/path/to/the/model/file # example models/my_finetuned_model_iter_10000.caffemodel
$CAFFEROOT/build/examples/cpp_classification/classification.bin \
	deploy.prototxt \
	$CAFFEROOT/data/ilsvrc12/imagenet_mean.binaryproto \
	classnames.txt \
	$test_image_path
```
deploy.prototxt basically contains a simplified, test-only version of the `train_val.prototxt` (just
diff two files to understand the deploy.prototxt contents). Therefore, if you make any 
architectural changes in `train_val.prototxt` (before training), update `deploy.prototxt`
accordingly.

# References

This example is based on the example codes and models provided at http://caffe.berkeleyvision.org and in the 
original Caffe source code.


