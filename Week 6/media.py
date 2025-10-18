import cv2

image = cv2.imread("1.png")

if image is None:
    print("Hata: Görsdel bulunamadı.")
    exit()

cv2.imshow("Orijinal Gorsel",image)

cv2.waitKey(0)
cv2.destroyAllWindows()

h,w,c = image.shape

print(f"{w}X{h} piksel, {c} kanal")

image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imwrite("gray_image.png",image_gray)

