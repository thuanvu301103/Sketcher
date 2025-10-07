from pipeline.loader import show_image, load_image, save_image
from pipeline.preprocess import color_convert, gaussian_blur
from pipeline.feature_detect import edge_detect, contour_detect
from pipeline.postprocess  import approximate_polygon
import cv2

## Adjust the parameters

# 1. File name
INPUT_FILE = 'image.jpg'

# 2 Color convert
FROM_COLOR = 'RGB'
TO_COLOR = 'GRAY'

# 3. Blur Filter
KERNAL_SIZE = 13
SIGMA = 2

# 4. Edge Detect
THRESHOLD_1 = 5
THRESHOLD_2 = 10

# 5. Contour Detect
CONTOUR_MODE = 'EXTERNAL'
CONTOUR_METHOD = 'SIMPLE'

# Approximate Polygon
ESPILON_FACT = 0.02

if __name__ == "__main__":
    
    ## 1. Load image
    image = load_image(INPUT_FILE)
    save_image(image, '01_origin.jpg')

    ## 2. Preprocess image    
    # 2.1. Color convert
    gray_image = color_convert.convert(image, FROM_COLOR, TO_COLOR)
    save_image(gray_image, '02_gray_scale.jpg')
    # 2.2. Noise reduce
    blured_image = gaussian_blur.apply_filter(gray_image, kernel_size=(KERNAL_SIZE,KERNAL_SIZE), sigma=SIGMA)
    save_image(blured_image, '03_blured.jpg')
    
    ## 3. Edge Detect
    edges = edge_detect.detect(blured_image, threshold1=THRESHOLD_1, threshold2=THRESHOLD_2)
    save_image(edges, '04_edge_detect.jpg')
    
    ## 4. Contour Detect
    contour_detected_image = image.copy()
    contours, hierarchy = contour_detect.detect(
        edges,
        CONTOUR_MODE,
        CONTOUR_METHOD
    )
    contour_detect.draw(contour_detected_image, contours)
    save_image(contour_detected_image, '05_contour_detect.jpg')
    
    ## 5. Approximate Polygon
    approximated_image = image.copy()
    aproxs = approximate_polygon.approximate(
        contours,
        ESPILON_FACT
    )
    approximate_polygon.draw(approximated_image, aproxs)
    save_image(approximated_image, '06_approximate_polygon.jpg')