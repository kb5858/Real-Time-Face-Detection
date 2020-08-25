import cv2

cascade_classifier = cv2.CascadeClassifier('Face_detection  (2)\haarcascade_eye.xml')
cap = cv2.VideoCapture(0)

while True:
    
    # Capture frame-by-frame

    ret, frame = cap.read()

    # Operations on the frame come here

    gray = cv2.cvtColor(frame, 0)
    detections = cascade_classifier.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)
    if(len(detections) > 0):
        (x,y,w,h) = detections[0]
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    # Display the resulting frame

    cv2.imshow('frame',frame)

    k=cv2.waitKey(10)
    if(k==27):
        break

# When everything done, release the capture

cap.release()
cv2.destroyAllWindows()