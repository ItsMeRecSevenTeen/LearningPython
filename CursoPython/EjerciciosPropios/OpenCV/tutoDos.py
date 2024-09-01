import cv2
import random
img = cv2.imread(r'Ejercicios mios\OpenCV\assets\python.jpg')

# for i in range(img.shape[0]):
#     for j in range(100):
#         img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
tag = img[200:400, 100:300]
img[100:300, 250:450] = tag
print(img.shape)
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()