import tkinter as tk
from tkinter import *
import cv2
from PIL import Image, ImageTk
import DB
from unidecode import unidecode

UI = tk.Tk()
UI.title("Nhận diện khuôn mặt")
UI.iconbitmap(r'ico.ico')
UI.configure(bg='white')
UI.geometry("1000x700")
UI.resizable(False, False)


camera_lb =Label(UI,bg='white')
camera_lb.place(x=500,y=25,width=450,height=600)

title_lb = Label(UI,text="Face Recognition Camera",border=0,bg='white',font=("Courier", 20 ,"bold"))
title_lb.place(x=550,y=22)


inform_lb = Label(UI,text="Personal Information",border=0,bg='white',font=("Courier", 20 ,"bold"))
inform_lb.place(x=80,y=20)

icon_img = Image.open('person_icon.png')
icon_inform = ImageTk.PhotoImage(icon_img.resize((30,30)))
imform_lb = Label(UI,image=icon_inform,bg='white',border=0)
imform_lb.place(x=20,y=70)

inform_lb_text = Label(UI,text="Không có thông tin",border=0,bg='white',font=("Courier", 18 ,"bold"))
inform_lb_text.place(x=80,y=75)

age_img = Image.open('icon_age.png')
icon_age = ImageTk.PhotoImage(age_img.resize((30,30)))
age_lb = Label(UI,image=icon_age,bg='white',border=0)
age_lb.place(x=20,y=120)

age_lb_text = Label(UI,text="Không có thông tin",border=0,bg='white',font=("Courier", 18 ,"bold"))
age_lb_text.place(x=80,y=125)

gender_img = Image.open('icon_gender.png')
icon_gender = ImageTk.PhotoImage(gender_img.resize((30,30)))
ger_lb = Label(UI,image=icon_gender,bg='white',border=0)
ger_lb.place(x=20,y=170)

gender_lb_text = Label(UI,text="Không có thông tin",border=0,bg='white',font=("Courier", 18 ,"bold"))
gender_lb_text.place(x=80,y=175)

#label.grid(row=0, column=0)
detect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(r"E:\Face_recognition\train\trainningData.yml")
cap= cv2.VideoCapture(0) 
# Define function to show frame
def show_frames():
   ret, im = cap.read() 
   # Get the latest frame and convert into Image
   cv2image= cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
   gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
   face = detect.detectMultiScale(cv2image, 1.3, 5)
   confidence = 0 
   for (x, y, w, h) in face:
        # vẽ 1 đường bao quanh khuôn mặt
        cv2.rectangle(cv2image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        roi_gray = gray[y:y+h,x:x+w]
        id,confidence = recognizer.predict(roi_gray)
   if confidence > 50 :
           profile = DB.getProfile(id)
           Name = unidecode(profile[1])
           Age = profile [2]
           Gender = profile [3]
           if profile != None :
              inform_lb_text.configure(text=Name)
              age_lb_text.configure(text=Age)
              gender_lb_text.configure(text=Gender)
            
           else  : 
              inform_lb_text.configure(text="Không có thông tin")
              age_lb_text.configure(text="Không có thông tin")
              gender_lb_text.configure(text="Không có thông tin")
                 
   else:
      inform_lb_text.configure(text="Không có thông tin")
      age_lb_text.configure(text="Không có thông tin")
      gender_lb_text.configure(text="Không có thông tin")                 
   img = Image.fromarray(cv2image)
   # Convert image to PhotoImage
   imgtk = ImageTk.PhotoImage(image = img)
   camera_lb.imgtk = imgtk
   camera_lb.configure(image=imgtk)
   # Repeat after an interval to capture continiously
   camera_lb.after(20, show_frames)

show_frames()
UI.mainloop()