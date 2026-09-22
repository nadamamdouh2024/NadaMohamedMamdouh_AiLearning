import cv2

cap = cv2.VideoCapture(0)

face_cascade= cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

while True:
    ret , frame = cap.read()
    if not ret :
        print ("Could not access the camera. ")
        break

    frame = cv2.flip(frame ,1)
    small = cv2.resize(frame, (320, 240))  #w,h
    gray = cv2.cvtColor(small,cv2.COLOR_RGB2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
    )

    scale_x = frame.shape[1] / 320   # shape(h,w)
    scale_y = frame.shape[0] / 240

    for x,y,w,h in faces:

        
        x = int(x * scale_x)
        y = int(y * scale_y)
        w = int(w * scale_x)
        h = int(h * scale_y)
        cv2.rectangle(
            frame,
            (x,y),
            (x+w,y+h),
            (0,255,0),
            2
        )


    cv2.putText(
        frame,
        f"Faces: {len(faces)}",
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,0,255),
        2
    )  

    cv2.imshow("Face Detection", frame)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
