import cv2
#import numpy as np

# Đọc ảnh
image = cv2.imread('D:\duongthang.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('moi.png',image)


sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)  # Đạo hàm theo trục x
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)  # Đạo hàm theo trục y

# Chuyển đổi kết quả sang kiểu uint8 để hiển thị
sobelx = cv2.convertScaleAbs(sobelx)
sobely = cv2.convertScaleAbs(sobely)

# Kết hợp cả hai kết quả
sobel_combined = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

# Hiển thị ảnh 
#cv2.imshow('Sobel X', sobelx)
#cv2.imshow('Sobel Y', sobely)
cv2.imshow('Sobel Combined', sobel_combined)
cv2.waitKey(0)