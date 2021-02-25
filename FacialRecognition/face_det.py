import cv2

SCREEN_WIDTH = 1920 * 0.75
SCREEN_HEIGHT = 1080 * 0.75

CASC_PATH = "haarcascade_frontalface_default.xml"

camera = cv2.VideoCapture()
faceCascade = cv2.CascadeClassifier(CASC_PATH)

def main():
    loop = True
    frame
    while loop:
        faces = getFaces()
        

def getFaces():
    frame = camera.read()
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        grayFrame,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    return faces

if __name__ == "__main__":
    main()
