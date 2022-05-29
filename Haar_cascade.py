import cv2

cap = cv2.VideoCapture('highway.mp4')
cascade = cv2.CascadeClassifier('car_cascade.xml')

while True:
    ret, img = cap.read()

    objects = cascade.detectMultiScale(img, scaleFactor=1.5, minNeighbors=5, minSize=(20, 20))

    for (x, y, w, h) in objects:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow('Result', img)

    k = cv2.waitKey(30) & 0xFF

    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()