import cv2

def detect(edges, mode, method):
    
    # Convert Contour Retrieval Mode
    if mode == "EXTERNAL":  # Retrieve only External Contours
        mode_code = cv2.RETR_EXTERNAL
    elif mode == "LIST":    # Retrieve all Contours (no hierarchy)
        mode_code = cv2.RETR_LIST
    else:
        raise ValueError(f"Unsupported Contour Retrieval Mode: {mode}")

    # Convert Contour Approximation Method
    if method == "NONE":    # Stores all the contour points
        method_code = cv2.RETR_EXTERNAL
    elif method == "SIMPLE":  # Compress points along straight lines
        method_code = cv2.CHAIN_APPROX_SIMPLE
    else:
        raise ValueError(f"Unsupported Contour Approximation Method: {method}")

    contours, hierarchy = cv2.findContours(
        edges,
        mode_code,
        method_code
    )
    return contours, hierarchy

def draw(image, contours, color=(0, 255, 0), thickness = 2):
    for cnt in contours:
        cv2.drawContours(image, [cnt], 0, color, thickness)