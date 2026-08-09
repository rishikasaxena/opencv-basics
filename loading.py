import cv2

image = cv2.imread("img.jpg")

if image is None:
    print("Image not found")
else:
    cv2.imshow("Loaded Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    