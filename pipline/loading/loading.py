import cv2

img = cv2.imread("image.jpg")

cv2.imshow("Image", img)
cv2.waitKey(0)          # Chờ nhấn phím
cv2.destroyAllWindows() # Đóng cửa sổ