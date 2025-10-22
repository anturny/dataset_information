# Dataset Characterization

This repository is created for the purpose of characterizing four datasets that are commonly associated with machine learning models. It is more so about the data itself rather than how it is used in machine learning.

## Table of Contents
* [Requirements](#requirements)
* [Implementation](#implementation)
* [Dataset Introduction](#dataset-introduction)
* [References](#references)


## Requirements

This repository only requires reading.

## Implementation

This repository is strictly a read only repository. There is no need for code execution unless it is an example which may already be shown in the [media folder](/media/). The explicit documentation for each of the four datasets are found within the [doc folder](/doc/).

## Dataset Introduction

This section of the repository is dedicated to giving a synopsis of each dataset.

### [Iris Dataset](/doc/iris_dataset.md)

The Iris dataset is a fundamental dataset that is widely used in teaching and benchmarking classification and discriminant analysis methods because of its simple yet instructive structure. With 150 samples at 50 samples per class, 4 numeric features, and 3 Iris specieis, it offers a clear demonstration of how feature measurements can distinguish biological categories. The _Iris setosa_ specieis is fairly well separated while _Iris virginica_ and _Iris versicolor_ overlap. These observations illustrate limitations of linear separability and the need for careful analysis of the class's geometry. While this dataset is highly convenient and popular, users should be aware that its small size, simplicity, and version inconsistencies can impact results if it is used as a benchmark for advanced tasks. 

![alt text](/media/picIRIS/IrisDatasetPic.png)

### [MNIST](/doc/MNIST.md)

The models implementation consists of an input of the MNIST dataset that involves a collection of 70,000 handwritten digits (0-9), with each image being 28x28 pixels. The purpose of training this model is to teach the neural network to identify and correctly classify handwritten digits based on pixel intensity patterns. The model is trained using 25 epochs, meaning it is passed through 25 times, with a validation split of 0.2 to prevent overfitting. This dataset is used widely for educational puroposes in deep learning and computer vision research.

![alt_text](/media/picMNIST/MNIST_dataset_examplePic.png)

### [FashionMNIST](/doc/FashionMNIST.md)

The fashionMNIST was made by Han Xiao, Kashif Rasul, and Roland Vollgraf at Zalando Research in 2017 to have the same concept as the MNIST handwritten dataset with same image sizing of 28 x 28, same train + testing splits w/ 60,000 training and 10,0000 testing spread across 10 classes. The difference is the content in which the FashionMNIST is classifying fashion items instead of digits. This was also made to help idenitfy and test the classification of complex images. The images of the clothing comes from clothing at Zalando, a European retailer. The original image sizings were processed and resized + converted to fit a 28 x 28 greyscale image formating with labeling. The formatting matched MNIST for easy reusage of code written for MNIST. 

![alt_text](/media/picFashionMNIST/Sample-images-from-Fashion-MNIST-dataset.png)

### [CIFAR-10](/doc/CIFAR-10.md)

CIFAR-10 remains a fundamental benchmark moderate in size and simple enough to work with quickly. It comes from the "_80 Million Tiny Images_" dataset, but it is hand-labeled and filtered to be cleaner to read. The point of creating this subset was to select a manageable, well-labeled subset of small color images (32 x 32) that covered a limited number of object categories which is later used to facilitate benchmarks in image classification. The results include a clean, 10 fixed object classes dataset that covers a variety of categories in small image resolutions. Over time, CIFAR-10 became one of the most known benchmarks used for computer vision and deep learning in research, teaching, and evaluation. The small resolution size and accessibility helps it be the middle man for toy datasets and larger high resolution datasets.In raw pixel space, classes are not linearly separable. These separations must rely on learned nonlinear transformations or embeddings. The dataset's balance and formatting makes it convenient, but it has known duplicates, label noise, and low resolution that limits how representative is is of real world tasks. When using CIFAR-10, it is good as a benchmark but the user should be mindful that the performance may easily saturate. When working with this dataset, one must distinguish whether the code is evaluating generalization or overfitting to the dataset. 

![alt_text](/media/picCIFAR10/Cifar10ClassPic.png)

## References

The references are native to each respective document inside their deep dive folder.

- [Iris Dataset](/doc/iris_dataset.md)
- [MNIST Dataset](/doc/MNIST.md)
- [Fashion MNIST Dataset](/doc/FashionMNIST.md)
- [CIFAR-10 Dataset](/doc/CIFAR-10.md)

