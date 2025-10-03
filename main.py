from pipeline.loading.loader import show_image, load_image
from pipeline.preprocessing import hsvPreprocessor

if __name__ == "__main__":
    image = load_image("image.jpg")
    hsv_image = hsvPreprocessor.preprocess(image)
