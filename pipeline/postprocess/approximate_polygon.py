import cv2

def approximate(contours, epsilon_factor = 0.02):
    approxs = []
    for cnt in contours:
        epsilon = epsilon_factor * cv2.arcLength(cnt, True)
        approxs.append(cv2.approxPolyDP(cnt, epsilon, True))
    return approxs

def draw(image, approxs, color=(0, 255, 0), thickness = 2):
    for apr in approxs:
        cv2.drawContours(image, [apr], 0, color, thickness)
