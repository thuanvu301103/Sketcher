import cv2
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
IMAGE_DIR = os.path.join(BASE_DIR, "images")

def show_image(img, window_name="Image"):
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.imshow(window_name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def load_image(filename):
    path = os.path.join(IMAGE_DIR, filename)
    img = cv2.imread(path)

    if img is None:
        raise FileNotFoundError(f"Cannot find file: {path}")

    return img
