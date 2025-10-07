import cv2

def apply_filter(img, kernel_size=(5,5), sigma=0):
    """
    Apply Gaussian Blur to an image.

    Parameters:
    - img: numpy array, input image (BGR or grayscale)
    - kernel_size: tuple of two odd integers, e.g., (5,5)
    - sigma: float, standard deviation. 0 means auto compute

    Returns:
    - blurred image (numpy array)
    """
    # Validate kernel size
    if kernel_size[0] % 2 == 0 or kernel_size[1] % 2 == 0:
        raise ValueError("Kernel size must be odd integers")
    
    blurred_img = cv2.GaussianBlur(img, kernel_size, sigma)
    return blurred_img