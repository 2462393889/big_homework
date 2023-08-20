# -*- coding: utf-8 -*-
import cv2
import time
import numpy as np

tpPointsChoose = []
drawing = False
tempFlag = False

def draw_ROI(event, x, y, flags, param):
    global point1, tpPointsChoose,pts,drawing, tempFlag
    if event == cv2.EVENT_LBUTTONDOWN:
        tempFlag = True
        drawing = False
        point1 = (x, y)
        tpPointsChoose.append((x, y))  # 用于画点
    if event == cv2.EVENT_RBUTTONDOWN:
        tempFlag = True
        drawing = True
        pts = np.array([tpPointsChoose], np.int32)
        pts1 = tpPointsChoose[1:len(tpPointsChoose)]
        print(pts1)
    if event == cv2.EVENT_MBUTTONDOWN:
        tempFlag = False
        drawing = True
        tpPointsChoose = []

cv2.namedWindow('video')
cv2.setMouseCallback('video',draw_ROI)
cap = cv2.VideoCapture('./data/video/test.mp4')  # 文件名及格式
fps=cap.get(cv2.CAP_PROP_FPS)
size=(cap.get(cv2.CAP_PROP_FRAME_WIDTH),cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("fps: {}\nsize: {}".format(fps,size))
vfps = 0.7/fps  #延迟播放用，根据运算能力调整
while (True):
    # capture frame-by-frame（获取一帧）
    ret, frame = cap.read()
    # display the resulting frame
    if (tempFlag == True and drawing == False) :  # 鼠标点击
        cv2.circle(frame, point1, 5, (0, 255, 0), 2)    #画点，一个半径为5，颜色为（0，255，0），厚度为2的小圈
        for i in range(len(tpPointsChoose) - 1):       #画线
            cv2.line(frame, tpPointsChoose[i], tpPointsChoose[i + 1], (255, 0, 0), 2)
    if (tempFlag == True and drawing == True):  #鼠标右击
        cv2.polylines(frame, [pts], True, (0, 0, 255), thickness=2)
    if (tempFlag == False and drawing == True):  # 鼠标中键
        for i in range(len(tpPointsChoose) - 1):
            cv2.line(frame, tpPointsChoose[i], tpPointsChoose[i + 1], (0, 0, 255), 2)
    time.sleep(vfps)
    cv2.imshow('video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # 按q键退出
        break
# when everything done , release the capture
cap.release()
cv2.destroyAllWindows()