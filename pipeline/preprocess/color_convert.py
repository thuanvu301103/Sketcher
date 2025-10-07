import cv2

def convert(img, in_color, out_color):
    """
    Convert an input image from one color space to another.
    
    Parameters:
        img (numpy.ndarray): Input image (commonly in BGR format).
        in_color (str): Input color space ('BGR' or 'RGB').
        out_color (str): Output color space ('GRAY' or 'HSV').

    Returns:
        converted_img (numpy.ndarray): The converted image.
    """
    if in_color == "BGR" and out_color == "GRAY":
        code = cv2.COLOR_BGR2GRAY
    elif in_color == "RGB" and out_color == "GRAY":
        code = cv2.COLOR_RGB2GRAY
    elif in_color == "BGR" and out_color == "HSV":
        code = cv2.COLOR_BGR2HSV
    elif in_color == "RGB" and out_color == "HSV":
        code = cv2.COLOR_RGB2HSV
    else:
        raise ValueError(f"Unsupported conversion: {in_color} → {out_color}")

    converted_img = cv2.cvtColor(img, code)
    return converted_img
