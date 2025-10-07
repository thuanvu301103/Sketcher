import cv2

def detect(image, threshold1, threshold2):
    edges = cv2.Canny(image, threshold1=threshold1, threshold2=threshold2)
    return edges
