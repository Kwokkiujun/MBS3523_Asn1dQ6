import cv2
EVT = 0
def draw_rectangle(event,x,y,flags,param):
    global EVT
    global Pnt1
    global Pnt2
    if event == cv2.EVENT_LBUTTONDOWN:
        EVT = event
        Pnt1 = (x,y)
    if event == cv2.EVENT_LBUTTONUP:
        EVT = event
        Pnt2 = (x, y)
    if event == cv2.EVENT_RBUTTONUP:
        EVT = event

cv2.namedWindow('MBS3523')
cv2.setMouseCallback('MBS3523',draw_rectangle)

cam = cv2.VideoCapture(0)


while True:
    _, img = cam.read()
    cv2.putText(img, 'MBS3523 Assignment 1b-Q6 Name: Kwok Kiu Jun', (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.75,
                (0, 0, 255), 2)
    if EVT == 4:
        cv2.rectangle(img, Pnt1,Pnt2,(255,0,255),3)
        imgROI = img[Pnt1[1]:Pnt2[1],Pnt1[0]:Pnt2[0]]
        cv2.imshow('ROI',imgROI)
    if EVT == 5:
        img[:,:]=img
        cv2.destroyWindow('ROI')
        EVT = 0

    cv2.imshow('MBS3523', img)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
