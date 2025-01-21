- [1. Introduction](#1-introduction)
- [2. Overall workflow of Object Detection](#2-overall-workflow-of-object-detection)
- [3. Non-maximum suppression (NMS)](#3-non-maximum-suppression-nms)
    - [3.1 Overall workflow for NMS](#31-overall-workflow-for-nms)
- [4. Detection Speed](#4-detection-speed)
- [5. Metrics in used](#5-metrics-in-used)
    - [5.1 Intersection of Unions (IoU)](#51-intersection-of-unions-iou)
    - [5.2 Precision-Recall Curve \& mean Average Precision (mAP)](#52-precision-recall-curve--mean-average-precision-map)
- [6. Object Detection Frameworks included](#6-object-detection-frameworks-included)
- [7. Reference books:](#7-reference-books)

Object Detection rely on transfer learning. Study [TODO: transfer learnings] before dive into object detection.

# 1. Introduction
Object Detection is a computer vision task that involves two tasks: 
  1. localizes one or more objects within an image
  2. classifies each object in image
This is done by drawing a bounding box around the identified object with its predicted class. In order to draw the bounding box, object detection needs to predict boxes coordinates (<b><i>x, y, w, h</i></b>) and class probability. Notes that  (<b><i>x, y</i></b>) are the coordinates of the bounding-box center point, and (<b><i>w, h</i></b>) are the width and height of the box.

# 2. Overall workflow of Object Detection
Nearly all object detection frameworks would follow below four steps:
  1. <b>Region Proposal</b>: <u>Regions of interest</u> (RoIs) are generated to be further processed. RoIs are candidates that might contain an object. There would be a large number of RoIs boxes output in this step.
  2. <b>Prediction</b>: Predict whether the RoI in which object are presented.
  3. <b>Non-maximum suppressions (NMS)</b>: The previous steps may generate multiple bounding boxes for the same object. This step is to avoid repeated detection of the same instance by combining overlapping boxes into a single bounding box for each object. This step involves <u>intersection over union (IoU)</u>.
  4. <b>Evaluation Metrics</b>: Object Detection has metrics ro evaluate their detection performance. Most popular metrics are <u>mean average precision (mAP)</u>, <u>precision-recall curve (PR curve)</u>, <u>intersection over union (IoU)</u>

# 3. Non-maximum suppression (NMS)
### 3.1 Overall workflow for NMS
1. Discard all bounding boxes that have predictions that are less than <b>confidence threshold</b> (tunable).
2. Select the bounding box with the highest probability
3. Calculate the overlap of the selected bounding box to remaining boxes that have the same class prediction. The bounding boxes that have overlap with selected box with higher overlap score (<b>IoU</b>) would be averaged together
4. Retain bounding boxes that has an <b>IoU</b> value smaller than <b>NMS threshold</b> would be retained, and start over step-2. The selected and merged bounding box would be kept but exclude from start-over step-2.
5. Until no more bounding boxes are pending to be proceeded.

# 4. Detection Speed
The number of frames per second (<b><u>FPS</u></b>) is the metric for measuring detection speed. 

# 5. Metrics in used
### 5.1 Intersection of Unions (IoU)
IoU is applied in Non-maximum suppression (NMS) and evaluation metric. It evaluates the overlap between two bounding boxes. In NMS cases, the two boudning boxes are selected bounding box and remaining bounding box. In evaluation cases, the two bounding boxes are ground truth bounding box and predicted bounding box.

### 5.2 Precision-Recall Curve & mean Average Precision (mAP)
We have to calculate <b>Precision</b> and <b>Recall</b> for each classes in the image. The area under PR curve (AUC) would then be subjected to mAP as the average of the AUC for all the classes.


# 6. Object Detection Frameworks included
   1. [R-CNN](R-CNN-families/R-CNN/README.md)
   2. Fast R-CNN
   3. Faster R-CNN
   4. YOLO (You Only Look Once)
   5. [SSD (Single Shot Detector)](Single-Shot-Detector/README.md)


# 7. Reference books:
1. 