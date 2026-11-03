import cv2

dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)

marker_id = 1
marker_pixels = 600
border_pixels = 100

marker = cv2.aruco.generateImageMarker(dictionary, marker_id, marker_pixels)
marker_with_border = cv2.copyMakeBorder(marker, border_pixels, border_pixels, border_pixels, border_pixels, 1, value=255)

cv2.imwrite("marker_1.png", marker_with_border)
print("Saved marker_1.png")
