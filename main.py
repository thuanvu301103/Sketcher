from pipeline.load.loader import show_image, load_image
from pipeline.preprocess import color_convert
from pipeline.preprocess.noise_reduce import gaussian_blur
import cv2

if __name__ == "__main__":
    
    ## 1. Load image
    image = load_image("image.png")
    show_image(image, "Origin")

    ## 2. Preprocess image    
    # 2.1. Color convert
    gray_image = color_convert.convert(image, 'RGB', 'GRAY')
    show_image(gray_image, "Color Converted")
    # 2.2. Noise reduce
    blured_image = gaussian_blur.apply_filter(gray_image, kernel_size=(13,13), sigma=2)
    show_image(blured_image, "Blured")

    ## 3. Edge Detect
    edges = cv2.Canny(blured_image, threshold1=5, threshold2=10)
    show_image(edges, "Edge Detected")

    ## 4. Contour Detect
    contours, hierarchy = cv2.findContours(
        edges,                  # ảnh nhị phân
        cv2.RETR_EXTERNAL,      # chỉ lấy contour ngoài cùng
        cv2.CHAIN_APPROX_SIMPLE # giảm bớt điểm thẳng hàng
    )
    #cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

    ## Polygon
    for cnt in contours:
        epsilon = 0.02 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)
        cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)

    cv2.imshow('Contours', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()