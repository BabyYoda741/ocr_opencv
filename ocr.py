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
        self.txtarea.delete(1.0,END)
        self.img = askopenfilename(filetypes=[("Image files", ".png .jpg .gif .jpeg")])
        self.img = cv2.imread(self.img)
        cv2.imshow('Preview',self.img)

    def scan(self):
        self.img = cv2.cvtColor(self.img,cv2.COLOR_BGR2RGB)
        self.txtarea.insert(INSERT, pytesseract.image_to_string(self.img))
        himg,wimg,a = self.img.shape
        boxes = pytesseract.image_to_data(self.img)
        for x,b in enumerate(boxes.splitlines()):
            if x!=0:
                b = b.split()
                if len(b)==12:
                    x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
                    cv2.rectangle(self.img,(x,y),(w+x,h+y),(0,0,255),1)
                    #cv2.putText(self.img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50.255),1)
                    cv2.imshow('Result',self.img)

    def save(self):
        fname = asksaveasfilename(defaultextension=".txt",filetypes=[("Text file", "*.txt")],confirmoverwrite=False)
        fname = fname if ".txt" in fname else fname + ".txt"
        f = open(fname, 'w')
        f.write(pytesseract.image_to_string(self.img))
        f.close()

root = Tk()
Ocr(root)
root.mainloop()
