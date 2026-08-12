import cv2 

image = cv2.imread("img.jpg")

if image is None:
    print("Image not found")
else:
  print("image loaded successfully")

  resized_image = cv2.resize(image, (300, 300))
  cv2.imshow("original image", image)
  cv2.imshow("resized image", resized_image)   
  cv2.imwrite('reaized_output.jpg', resized_image)
  cv2.waitKey(0)
  cv2.destroyAllWindows() 
  