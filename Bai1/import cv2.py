import cv2
import numpy as np

img = cv2.imread('D:\MachineVison\moi.png')
cv2.imwrite('new.png',img)
new_img = cv2.imread('new.png')
gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 50, 150, apertureSize=3)  # Phát hiện cạnh bằng Canny


lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=150, minLineLength=7, maxLineGap=5)

# Vẽ các đoạn thẳng
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(new_img, (x1, y1), (x2, y2), (0, 255, 0), 2)


# Hiển thị kết quả
cv2.imshow('Input',img)
cv2.imshow("output", new_img)
cv2.waitKey(0)