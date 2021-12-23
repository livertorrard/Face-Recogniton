import DB
import cv2
from unidecode import unidecode

# load model haarcascade
detect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.read(r"E:\Face_recognition\train\trainningData.yml")
# trích suất ảnh từ camera
cap = cv2.VideoCapture(0)

while (True):
    ret, img = cap.read()
    # chuyển về ảnh xám
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # nhận diện khuôn mặt
    face = detect.detectMultiScale(gray)
    for (x, y, w, h) in face:
        # vẽ 1 đường bao quanh khuôn mặt
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        roi_gray = gray[y:y+h,x:x+w]
        id,confidence = recognizer.predict(roi_gray)
        print(confidence)
        if confidence > 50 :
           profile = DB.getProfile(id)
           Name = unidecode(profile[1])
           Age = profile [2]
           Gender = profile [3]
           if(profile != None):
               cv2.putText(img,f"Ten : {Name} tuoi : {Age} Gender : {Gender}",(x+10,y+h+30),1,1,(0,0,255),2)
        else:
            cv2.putText(img,"Khong nhan dang duoc",(x+10,y+h+30),1,1,(0,0,255),2)       

    # hiển thị ảnh nhận diện
    cv2.imshow('frame', img)
    if(cv2.waitKey(1)==ord('q')):
        break

cap.release()
cv2.destroyAllWindows