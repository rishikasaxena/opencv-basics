import cv2

image = cv2.imread('img.jpg')

if image is not None:
    cv2.imwrite('saved_image.jpg', image)
    print("Image saved successfully.")
else:
    print("Image not found.")