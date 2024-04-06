import cv2
from cv2 import GaussianBlur

#Video capture
cap = cv2.VideoCapture('it303.mp4')

#Extracting frames
while(cap.isOpened()):
    ret, ogframe = cap.read()

    if not ret:
        break

    frame = cv2.cvtColor(ogframe, cv2.COLOR_BGR2HSV)
    # frame = correct_skew(frame)

    frame = GaussianBlur(frame, (5,5), 0)
    
    #Edge detection
    edges = cv2.Canny(frame,50,100)
    edges = cv2.adaptiveThreshold(edges,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
    
    cv2.imshow('Edges', edges)
    cv2.imshow('Frames', ogframe)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
