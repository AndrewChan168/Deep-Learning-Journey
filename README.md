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
- [Graph Deep Learning](#graph-deep-learning)
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

# Graph Deep Learning
Graph Deep Learning is designed to process data structured as graphs which are <b><i>non-Euclidean</i></b>. While other deep learning excels on Euclidean data.<br>
[Foundation Concepts](Graph-Deep-Learning/README.md)

## Graph Neural Network (GNN)
Like traditional neural network, <b>GNN</b> is shallow stack of layers. <b>GNN</b>captures the dependencies bewteen nodes through a process called <b><i>message passing</i></b>. In each layer, every node aggregates feature information from its immediate neighbors to update its own representation.<br>
[GNN](Graph-Deep-Learning/GNN/README.md)

## Graph Attention Network (GAT)
<b>GAT</b> improve basic GNNs by incorporating <b><i>attention mechanisms</i></b>. In standard GNN, neighbors are often weighted equally or based on the graph degree. <b>GAT</b> allows the model to learn to assign different levels of weights (importance) to different nodes in a neighborhood.<br>

[GAT](Graph-Deep-Learning/GAT/README.md)

## GraphSAGE 
<b>GraphSAGE</b> is an inductive framework designed to scale <b>GNN</b>s to massive graph. Traditional GNNs often require the entire graph structure to be present during training. 

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
Mainly focus on how to reuse pre-trained on **Hugging Face** repository [Usage of Hugging Face](Large-Language-Models/Pretrained-Models/README.md). It also includes how to fine tuning on pre-trained model for domain adaption.

## Large Language Model Applications
This section focus on frameworks for building LLM applications [Frameworks for LLM Application](Large-Langhage-Models/LLM-Application-Frameworks/README.md) and protocol of tools for LLM application (MCP) [Model Context Protocol (MCP)](Large-Language-Models/Model-Context-Protocol/README.md) <br>
<br>
We are going through the cutting-edge LLM application <b>AI Agents</b>. 
