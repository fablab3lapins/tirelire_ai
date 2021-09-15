import cv2
import numpy as np


"""def regroup(scale, imgarray):
    rows = len(imgarray)
    cols = len(imgarray[0])
    rowsavailable = len(imgarray[0])
    width = imgarray[0][0].shape[1]
    height = imgarray[0][0].shape[0]

    widthscale = width*scale
    heightscale = height*scale

    
    if rowsavailable:
        for x in range (0, rows):
            for y in range (0, cols):
                if imgarray[x][y].shape[:2] == imgarray[0][0].shape[:2]:
                    imgarray[x][y] = cv2.resize(imgarray[x][y], (widthscale, heightscale), None)
                else:
                    imgarray[x][y] = cv2.resize(imgarray[x][y], (imgarray[0][0].shape[1], imgarray[0][0].shape[0]), None, scale, scale)
                if len(imgarray[x][y].shape) == 2:
                    imgarray[x][y] = cv2.cvtColor( imgarray[x][y], cv2.COLOR_GRAY2BGR)

        imageblank = np.zeros((height, width, 3), np.uint8)
        hor = [imageblank]*rows
        horcon = [imageblank]*rows
        for x in range (0, rows):
            hor[x] = np.hstack(imgarray[x])
        ver = np.vstack(hor)
    else:
        for x in range (0, rows):
            if imgarray[x].shape[:2] == imgarray[0].shape[:2]:
                    imgarray[x] = cv2.resize(imgarray[x], (widthscale, heightscale), None)
            else:
                 imgarray[x] = cv2.resize(imgarray[x], (imgarray[0].shape[1], imgarray[0].shape[0]), None, scale, scale)
            if len(imgarray[x].shape) == 2:
                imgarray[x] = cv2.cvtColor( imgarray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgarray)
        ver = hor
    return ver"""

cap = cv2.VideoCapture(0)

"""while True:
        _, frame =cap.read()

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_blue = np.array([38, 86, 0])
        upper_blue = np.array([121, 255, 255])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        a , contour   = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(frame, a, -1, (0, 0, 255), 3)
        
        cv2.imshow("frame", frame)
        cv2.imshow("mask", mask)

        key = cv2.waitKey(1)
        if key == ord("q"):
            break"""

while True:
    def empty(o):
        pass


    cv2.namedWindow("truc")
    cv2.resizeWindow("truc", 640,240)

    cv2.createTrackbar("gauss 1", "truc", 5, 10, empty)
    cv2.createTrackbar("gauss 2", "truc", 5, 10, empty)
    cv2.createTrackbar("canny 1", "truc", 50, 100, empty)
    cv2.createTrackbar("canny 2", "truc", 210, 400, empty)


    gauss1 = cv2.getTrackbarPos("gauss 1", "truc")
    gauss2 = cv2.getTrackbarPos("gauss 2", "truc")
    canny1 = cv2.getTrackbarPos("canny 1", "truc")
    canny2 = cv2.getTrackbarPos("canny 2", "truc")

    
    _,frame = cap.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    gauss = cv2.GaussianBlur(gray, (5, 5), 0)

    canny = cv2.Canny(gauss, 60, 210)

    cont = canny.copy()

    contr, hier = cv2.findContours(cont, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contr:
        area = cv2.contourArea(cnt)
        if area>400:
            cv2.drawContours(frame, cnt, -1, (0,0, 255), 2)

    cv2.imshow("contours", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break    



cap.release()

cv2.destroyAllWindows()

















            
            
            
                    
            
