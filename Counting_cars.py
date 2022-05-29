import cv2
import numpy as np
import pickle
class Car:
    def __init__(self,x,y):
        self.x = x
        self.y = y

#загрузка YOLO
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))
cap = cv2.VideoCapture("los_angeles.mp4")
#загрузка изображения
while True:
    _,img = cap.read()
    img = cv2.resize(img, None, fx=0.4, fy=0.4)
    height, width, channels = img.shape

    # Detecting objects
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    net.setInput(blob)
    outs = net.forward(output_layers)

    # Showing informations on the screen
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)#индексы для избежания дублирования прямоугольников

    counting_obj = dict()
    class_ids.sort()
    count_ = 0
    for i in range(len(class_ids) - 1):
        if class_ids[i] == class_ids[i + 1]:
            count_ += 1
        else:
            counting_obj[classes[class_ids[i]]] = count_
            count_ = 0


    cars_ = []

    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            if(class_ids[i] == 2):
                tmp_car = Car(x + w / 2, y + h / 2)
                cars_.append(tmp_car)

            color = colors[class_ids[i]]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)

    with open('coordinates.pickle', 'wb') as f:# сериализация
        pickle.dump(cars_, f)

    space = 1
    for key in counting_obj.keys():
        cv2.putText(img, key + ' ' + str(counting_obj[key]), (0, 10 + space * 30), font, 3, 3, 3)
        space += 1


    cv2.imshow("Image", img)
    ch = cv2.waitKey(30)
    if ch == 27:
        break

cv2.destroyAllWindows()