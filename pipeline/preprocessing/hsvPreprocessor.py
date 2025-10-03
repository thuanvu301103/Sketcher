import cv2

def preprocess(img):
    """
    Preprocess an input image by converting it
    from BGR color space (default in OpenCV) to HSV color space.

    Parameters:
        img (numpy.ndarray): Input image in BGR format.

    Returns:
        hsv_img (numpy.ndarray): Output image in HSV format.
            - Channel 0 (Hue): range [0, 179], represents the color type
              (e.g., red, green, blue).
            - Channel 1 (Saturation): range [0, 255], represents how "pure" or intense the color is.
            - Channel 2 (Value): range [0, 255], represents brightness (lightness/darkness).
    """
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # Convert BGR → HSV
    return hsv_img

