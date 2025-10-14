## CIFAR-10 Dataset

### Background

The CIFAR-10 dataset was introduced by Alex Krizhevsky, Vinod Nair, and Geoffrey Hinton in their 2009 paper "_Learning Multiple Layers of Features from Tiny Images_" at the University of Toronto. It is actually labeled as a subset from the much larger "_80 Million Tiny Images_" dataset from 2008 as released by Torralba, Fergus, and Freeman. The point of creating this subset was to select a manageable, well-labeled subset of small color images (32 x 32) that covered a limited number of object categories which is later used to facilitate benchmarks in image classification.

The creators manualled curated labels rather than utilizing the labels that already exist from the _Tiny Images_ dataset. The results include a clean, 10 fixed object classes dataset that covers a variety of categories in small image resolutions. 

Over time, CIFAR-10 became one of the most known benchmarks used for computer vision and deep learning in research, teaching, and evaluation. The small resolution size and accessibility helps it be the middle man for toy datasets and larger high resolution datasets.

### Dataset Structure

CIFAR-10 consists of 60,000 color images of size 32 x 32 pixels with three color channels (RGB). There are 10 classes with each class containing 6,000 images. The dataset is typically split into a training set of 50,000 images and a test set of 10,000 images.

The test set is organized so that there are exactly 1,000 images per class. The training set is typically divided into 5 batches of 10,000 images each for convenience in provided formats. Of the 5 training batches, each class is represented by 5,000 images so the training set is balanced across all classes. The training batches are randomized, so the individual batches may not be perfectly balanced.

In most software frameworks such as Keras or Pytorch, the images are stored as 8-bit unsigned integers ranging from 0-255 per channel with the labels as integers ranging 0-9 indicating the class. The names of these class in order are:
```
airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck
```

Because of the fixed size and data format, many libraries provide built-in loaders
```
tf.keras.datasets.cifar10

or

torchvision.datasets.CIFAR10
```

Due to how small the CIFAR-10 images are and their relative low detail, there is a limit to how fine distinctions can be made visually. Classes like airplane, truck, and ship may be harder to distinguish.

## Data Trends, Seperability, Overlap, Center of Mass

Image datasets like CIFAR-10 live in high dimensional pixel space (32 x 32 x 3 = 3,072 dimensions). In that space, linear separability between arbitrary classes is unlikely unless features, or learned projections, collapse the dimension. In raw pixel space, the different classes overlap heavily. For example, the pixel distributions for cat and dog may share a lot of statistical structure such as backgrounds, textures, and colors. The classes are not linearly separable in raw input space.

Instead, we can look at centroids (mean image per class) in pixel space. The centroid for each class is the mean over images in that class and typically reveal a blurry class prototype. For example, one may see the wings of an airplane under the airplane class or a long neck for the horse class. The intercentroid distances (distance in pixel space) reflect how far apart the classes are on average. However, the variation around a centroid 