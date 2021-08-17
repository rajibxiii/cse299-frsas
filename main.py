from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
from traindata import Traindata
from performfacerecognition import Face_Recognition
from attendance import Attendance
from time import strftime
from datetime import datetime
from developer import Developer

class FaceRecSys:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Student Attendance System")
        root.resizable(0, 0)
        root.attributes('-alpha', 0.95)

        # Background Image
        imgBg = Image.open(r"images\colorBg.png")
        imgBg = imgBg.resize((1530, 790), Image.ANTIALIAS)
        self.PhoImgBg = ImageTk.PhotoImage(imgBg)  # set image

        BgImg = Label(self.root, image=self.PhoImgBg)  # shows in window
        BgImg.place(x=0, y=0, width=1530, height=790)  # place image


        # Date And Time
        def currentTime ():
            string = strftime('%d.%m.%Y ∙ %I:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, currentTime)

        lbl = Label (font = ("Calibri Light", 30))
        lbl.place(x=520, y=42, width=500, height=40)
        currentTime ()



        titleLabel = Label(
            text="STUDENT ATTENDANCE SYSTEM",
            font=(
                "Calibri Light",
                30,
            ),
            bg="#E8F0F2",
            fg="black",
        )

        titleLabel.place(x=0, y=120, width=1530, height=50)

        # Making  buttons for 'Student Details', 'Face Detector', 'Train Data', 'Attendance', 'Photos', 'Exit'

        # Student detail button
        studenButton = Image.open(r"images\StudentButton.jpg")
        studenButton = studenButton.resize((130, 130), Image.ANTIALIAS)
        self.PhoImgStdBtn = ImageTk.PhotoImage(studenButton)

        Btn1 = Button(
            BgImg, image=self.PhoImgStdBtn, command=self.student_details, cursor="hand2"
        )
        Btn1.place(x=250, y=270, width=130, height=130)

        Btn1 = Button(
            BgImg,
            text="STUDENT DETAILS",
            command=self.student_details,
            cursor="hand2",
            font=(
                "Calibri",
                12,
                "bold",
            ),
            bg="#3F0D12",
            fg="white",
        )
        Btn1.place(x=250, y=370, width=130, height=30)

        # Face Detect Button
        faceDetectButton = Image.open(r"images\facedetect.jpg")
        faceDetectButton = faceDetectButton.resize((130, 130), Image.ANTIALIAS)
        self.PhoImgFacDetBtn = ImageTk.PhotoImage(faceDetectButton)

        Btn2 = Button(BgImg, image=self.PhoImgFacDetBtn, cursor="hand2",command=self.facedata)
        Btn2.place(x=550, y=270, width=130, height=130)

        Btn2 = Button(
            BgImg,
            text="DETECT FACE",
            cursor="hand2",
            command=self.facedata,
            font=("Calibri",12,"bold"),
            bg="#3F0D12",
            fg="white",
        )
        Btn2.place(x=550, y=370, width=130, height=30)

 


    # Function for opening images
    def open_img (self):
        os.startfile("data")

    # Making Function for student details Button activate from main window
    def student_details(self):
        self.student_details_window = Toplevel(self.root)
        self.app = Student(self.student_details_window)


    def train_dataset(self):
        self.train_dataset_window = Toplevel(self.root)
        self.app = Traindata(self.train_dataset_window)


    def facedata(self):
        self.faceRecognitionwindow = Toplevel(self.root)
        self.app = Face_Recognition(self.faceRecognitionwindow)


    def attendanceData(self):
        self.attendance_window = Toplevel(self.root)
        self.app = Attendance(self.attendance_window)

    def developer(self):
        self.attendance_window = Toplevel(self.root)
        self.app = Developer(self.attendance_window)


if __name__ == "__main__":
    root = Tk()  # root is needed to call by toolkit (tk)
    obj = FaceRecSys(root)
    root.mainloop()
