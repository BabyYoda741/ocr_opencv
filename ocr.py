from tkinter import *
#from tkinter import messagebox
#from tkinter import ttk

class Ocr:
    def __init__(self, root):
        self.root = root
        self.root.title("Optical Character Recognition")
        self.root.geometry("1280x720+120+10")
     
        F1 = Frame(self.root)
        F1.place(x=0, y=30, width=640, height=50)

        Button(F1,width=12,text="Open Image",font=("arial", 13), bg="gray80", bd=1).grid(padx=10,pady=3,row=0, column=0)
        Button(F1,width=12,text="Start OCR",font=("arial", 13), bg="gray80", bd=1).grid(padx=10,pady=3,row=0, column=1)
            
        F2 = Frame(self.root)
        F2.place(x=640, y=80, width=640, height=620)
  
        scroll_y = Scrollbar(F2, orient=VERTICAL)
        self.txtarea = Text(F2, font="arial 12", yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        F3 = Frame(self.root)
        F3.place(x=640, y=30, width=640, height=50)

        Button(F3,width=12,text="Save as Text",font=("arial", 13), bg="gray80", bd=1).grid(padx=10,pady=3,row=0, column=0)
        Button(F3,width=12,text="Search",font=("arial", 13), bg="gray80", bd=1).grid(padx=10,pady=3,row=0, column=1)

        F4 = Frame(self.root)
        F4.place(x=0, y=80, width=640, height=620)

        #image view

      
root = Tk()
Ocr(root)
root.mainloop()
