from tkinter import *
#from tkinter import messagebox
#from tkinter import ttk
import cv2
import pytesseract
#from PIL import Image, ImageTk
#import numpy
from tkinter.filedialog import *

pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

class Ocr:
    def __init__(self, root):
        self.root = root
        self.root.title("Optical Character Recognition")
        self.root.geometry("1280x720+120+10")

        F1 = Frame(self.root)
        F1.place(x=0, y=30, width=640, height=50)
        Button(F1,width=12,text="Open Image",font=("arial", 13), bg="gray80", bd=1, command=self.imglocate).grid(padx=10,pady=3,row=0, column=0)
        Button(F1,width=12,text="Start OCR",font=("arial", 13), bg="gray80", bd=1, command=self.scan).grid(padx=10,pady=3,row=0, column=1)
   
        F2 = Frame(self.root)
        F2.place(x=640, y=80, width=640, height=620)
        scroll_y = Scrollbar(F2, orient=VERTICAL)
        self.txtarea = Text(F2, font="arial 12", yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        F3 = Frame(self.root)
        F3.place(x=640, y=30, width=640, height=50)
        Button(F3,width=12,text="Save as Text",font=("arial", 13), bg="gray80", bd=1, command=self.save).grid(padx=10,pady=3,row=0, column=0)
        Button(F3,width=12,text="Search",font=("arial", 13), bg="gray80", bd=1).grid(padx=10,pady=3,row=0, column=1)

        F4 = Frame(self.root)
        F4.place(x=0, y=80, width=640, height=620)

    def imglocate(self):
        self.img = askopenfilename()
        self.img = cv2.imread(self.img)
        self.img = cv2.cvtColor(self.img,cv2.COLOR_BGR2RGB)
        cv2.imshow('Result',self.img)
        #show image
    
    def scan(self):
        self.txtarea.insert(INSERT, pytesseract.image_to_string(self.img))

    def save(self):
        dlg = asksaveasfilename(confirmoverwrite=False)
        fname = dlg
        f = open(fname, 'w')
        f.write(pytesseract.image_to_string(self.img))
        f.close()


root = Tk()
Ocr(root)
root.mainloop()
