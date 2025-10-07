import cv2
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_IMAGE_DIR = os.path.join(BASE_DIR, "images/input")
OUTPUT_IMAGE_DIR = os.path.join(BASE_DIR, "images/output")

def show_image(img, window_name="Image"):
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.imshow(window_name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def load_image(filename):
    path = os.path.join(INPUT_IMAGE_DIR, filename)
    img = cv2.imread(path)

    if img is None:
        raise FileNotFoundError(f"Cannot find file: {path}")

    return img

def save_image(image, filename):
    path = os.path.join(OUTPUT_IMAGE_DIR, filename)
    cv2.imwrite(path, image)