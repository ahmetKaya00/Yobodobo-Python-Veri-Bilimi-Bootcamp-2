import cv2

image = cv2.imread("1.png")

new_width = 400
new_height = int(image.shape[0] * (new_width / image.shape[1]))

resized_image = cv2.resize(image,(new_width,new_height))

cv2.imwrite("new_size.png",resized_image)

rotated_90 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("Orijinal Gorsel",rotated_90)
cv2.waitKey(0)
cv2.destroyAllWindows()

croppen_image = image[50:250,50:250]

cv2.imshow("Kirpilmis Gorsel",croppen_image)
cv2.waitKey(0)
cv2.destroyAllWindows()