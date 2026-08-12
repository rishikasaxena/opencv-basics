import cv2
image = cv2.imread("img.jpg")

if image is not None:
    cropped_image = image[100:200, 50:150]  # Crop the image (y1:y2, x1:x2)
    cv2.imshow("Cropped Image", cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()