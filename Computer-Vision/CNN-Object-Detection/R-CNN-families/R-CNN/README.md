- [Components of **R-CNN** model](#components-of-r-cnn-model)

# Components of **R-CNN** model
1. **Candidate regions of interest**: Apply <u>selective search</u> algorithm scans the input image to find regions that contain blobs, and propses the regions as <u>RoIs</u> to be processed by next modules
2. **Feature extraction**: Run a <u>pretrained convolutional network</u> on the <i>RoIs</i> to extract features from candidate <i>RoIs</i>.
3. **Classification module**: classifier (SVM) to classify candidates based on extracted features
4. **Localization module**: Known as bounding-box regressor. It predict the location and size of the bounding box that surrounds the object as tuple: (**x, y, w, h**)

<i>......adding graph</i>