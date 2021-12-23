import cv2
import DB
from unidecode import unidecode
import re
def Input():
    Name = input("Enter Your Name : ")
    Age = input("Enter Your Age : ")
    Gender = input("Enter Your Gender : ") 
    DB.insertDB(Name,Age,Gender)
    word = unidecode(Name)
    Id = DB.getIdUser(Name)
    return word,Id

    #return re.sub("\s+","_",word)   


# trích suất ảnh từ camera
cap = cv2.VideoCapture(0)
# load model haarcascade
detect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
name,Id = Input()
index = 0
while (True):
    ret, img = cap.read()
    # chuyển về ảnh xám
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # nhận diện khuôn mặt
    face = detect.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in face:
        # vẽ 1 đường bao quanh khuôn mặt
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        index +=1
        cv2.imwrite(f"dataSet/{name}_{Id}_{str(index)}.jpg",gray[y : y + h,x: x + w])
    # hiển thị ảnh nhận diện
    cv2.imshow('frame', img)
    cv2.waitKey(1)
    if index>=500:
        break
cap.release()
cv2.destroyAllWindows()