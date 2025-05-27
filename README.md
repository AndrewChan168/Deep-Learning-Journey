- [Full Connected Neural Network](#full-connected-neural-network)
  - [Mathematics of Neural Network](#mathematics-of-neural-network)
  - [Use Deep Learning Frameworks to build Neural Network](#use-deep-learning-frameworks-to-build-neural-network)
  - [More on training Deep Neural Network](#more-on-training-deep-neural-network)
- [Computer Vision](#computer-vision)
  - [Applying CNN on image classification](#applying-cnn-on-image-classification)
  - [Transfer Learning with CNN](#transfer-learning-with-cnn)
  - [Object Detection with CNN](#object-detection-with-cnn)
  - [Semantic Segmentation with CNN](#semantic-segmentation-with-cnn)
  - [Image Caption](#image-caption)
  - [Pose Estimation](#pose-estimation)
  - [Visual Embeddings](#visual-embeddings)
  - [Generative Adversarial Network (GAN)](#generative-adversarial-network-gan)
  - [Neual Style Transfer](#neual-style-transfer)
- [Graph Neural Networks](#graph-neural-networks)
- [Deep Learning on Sequential Data](#deep-learning-on-sequential-data)
- [Transformers Architecture](#transformers-architecture)
- [Large Language Model](#large-language-model)
  - [Pretrained Models](#pretrained-models)

# Full Connected Neural Network

## Mathematics of Neural Network

## Use Deep Learning Frameworks to build Neural Network

## More on training Deep Neural Network

# Computer Vision
By leveraging deep neural networks, particularly Convolutional Neural Networks (CNNs), computers can now perform complex visual tasks such as image classification, object detection, segmentation, and facial recognition. <br>
<br>
The key advantage of deep learning in computer vision lies in its ability to automatically learn hierarchical feature representations from raw pixel data. Unlike traditional computer vision approaches that relied heavily on hand-crafted features, deep learning models can discover intricate patterns and representations through training on large datasets.<br>
<br>

## Applying CNN on image classification
When applying neural networks to image classification tasks, we often encounter the challenge of handling an enormous number of parameters. To address this issue, convolutional layers are used instead of fully connected layers. This is because convolutional layers take advantage of two key properties: <b><i>locality</i></b> and <b><i>translation invariance</i></b>. <br>
[CNN-Image-Classification](Computer-Vision/CNN-Image-Classification/README.md)

## Transfer Learning with CNN
A pre-trained model, typically trained on a large dataset, is adapted to new but related task, instead of training a CNN from scratch. This is called <b><i>transfer learning</i></b>. <br>
[Transfer-Learning](Computer-Vision/Transfer-Learning/README.md)

## Object Detection with CNN
Object detection involves identifying and localizing objects within an image. Object detection, unlike image classification which assigns a single label to an entire image, classifies object and determines their positions using bounding boxes.
[CNN-Object-Detection](Computer-Vision/CNN-Object-Detection/README.md)

## Semantic Segmentation with CNN

## Image Caption
[Image Caption](Computer-Vision/Image-Caption/README.md)

## Pose Estimation

## Visual Embeddings

## Generative Adversarial Network (GAN)

## Neual Style Transfer

# Graph Neural Networks

# Deep Learning on Sequential Data

# Transformers Architecture
**Transformer** architectures could be classified as three families
- <i>Autoencoders</i>
- <i>Autoregressive Language Models</i>
- <i>Encoder-Decoders</i>
[Transformers Architectures](Transformer-Architecture/README.md)

# Large Language Model
A **large language model (LLM)** is built on transformer architecture and is trained on massive datasets of text to learn statistical patterns and contextual relationships in language. **LLM** uses <u>self-attention</u> mechanisms to process and generate sequences.

## Pretrained Models
Mainly focus on how to reuse pre-trained on **Hugging Face** repository
[Usage of Hugging Face](Large-Language-Models/Pretrained-Models/README.md)