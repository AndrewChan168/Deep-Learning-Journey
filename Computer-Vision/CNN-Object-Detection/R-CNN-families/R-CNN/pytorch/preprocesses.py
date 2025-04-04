import numpy as np
import selectivesearch


def extract_candidate_boxes(img_arr):
    _, regions = selectivesearch.selective_search(img_arr, scale=200, min_size=100)
    img_area = np.prod(img_arr.shape[:2])
    candidate_boxes = []
    for reg in regions:
        if reg['rect'] in candidate_boxes:
            continue
        if reg['size'] < (0.05 * img_area):
            continue
        if reg['size'] > (1.0 * img_area):
            continue
        candidate_boxes.append(reg['rect'])
    return candidate_boxes


def iou_score(boxA, boxB, epsilon=1e-5):
    x1 = max(boxA[0], boxB[0])
    y1 = max(boxA[1], boxB[1])
    x2 = min(boxA[2], boxB[2])
    y2 = min(boxA[3], boxB[3])
    width = (x2 - x1)
    height = (y2 - y1)
    if (width<0) or (height <0):
        return np.float64(0.0)
    area_overlap = width * height
    area_a = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
    area_b = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])
    area_combined = area_a + area_b - area_overlap
    iou = area_overlap / (area_combined+epsilon)
    return iou