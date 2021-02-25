import cv2

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 750
cam = cv2.VideoCapture(0)
CASC_PATH = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(CASC_PATH)

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )

    images = []
    images.append(frame)
    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        croppedImg = frame[y:y+h, x:x+w]        
        images.append(croppedImg)

    imageSize = SCREEN_WIDTH/len(images)

    resizedImages = []
    for img in images:
        resizedImages.append(cv2.resize(img, (int(imageSize), SCREEN_HEIGHT)))

    cv2.imshow("Faces!", cv2.hconcat(resizedImages))

    k = cv2.waitKey(1)
    if k%256 == 27:
        #Esc pressed
        print("escape hit, closing...")
        break

cam.release()

cv2.destroyAllWindows()
