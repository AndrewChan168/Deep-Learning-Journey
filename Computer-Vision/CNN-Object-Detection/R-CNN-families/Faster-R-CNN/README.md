- [Overall steps for Faster R-CNN](#overall-steps-for-faster-r-cnn)
- [Anchor boxes](#anchor-boxes)
- [Region Proposal](#region-proposal)
- [Classification and Regression](#classification-and-regression)

# Overall steps for Faster R-CNN
    1. Slide anchor boxes of different aspect ratios and sizes across the image to <u>fetch crops of an image</u>
    2. Calculate the **IoU** between <u>ground-truth bounding boxes</u> of objects and crops from previous step
    3. object threshold & background threshold: 
       1. if **IoU** is greater than object threshold, that anchor box is kept as object
       2. if **IoU** is less than background threshold, that anchor box is kept as background
       3. if **IoU** is between object threshold and background threshold, the anchoer is ignored
    4. Pre-trained model to identify if archoer box contains an object
    5. Non-Max Suppression (NMS) to identify the candidate that has the highest probability of containing an object, and remove other candidates that overlap the highest probability candidates

# Anchor boxes

# Region Proposal 

# Classification and Regression