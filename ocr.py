
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class Ocr():
    def __init__(self, root):
        self.root = root
        self.root.title("OCR")
        self.root.geometry("1000x600+0+0")
        abg = "light steel blue1"
        self.root.configure(bg=abg)
        bg_clr = "gray80"
        t_clr = "black"
        bclr = "DodgerBlue2"
        title = Label(self.root, text="Optical Character Recognition", bg=abg, fg=t_clr, bd=0, relief=GROOVE, font=("Bradley Hand ITC", 30, "bold"))
        title.pack(fill=X)

        #   ***********************Frame for buttons*****************
        F1 = LabelFrame(self.root, font=("times new roman", 15, "bold"), bg=abg, fg="gold",bd=0, relief=SUNKEN)
        F1.place(x=0, y=80, relwidth=1)

        #   ************************Buttons**************************
        Button(F1,width=12,text="Select Image",font=("times new roman", 14, "bold"), bg=bg_clr, fg="black", bd=10).grid(padx=10,pady=3,row=0, column=0)
        Button(F1,width=12,text="Recognise Text",font=("times new roman", 14, "bold"), bg=bg_clr, fg="black", bd=10).grid(padx=10,pady=3,row=0, column=1)
        Button(F1,width=12,text="Save",font=("times new roman", 14, "bold"), bg=bg_clr, fg="black", bd=10).grid(padx=10,pady=3,row=0, column=2)
        Label(F1, text="File no.", font=("times new roman", 15, "bold"), bg=abg, fg="black", bd=7, padx=20, pady=3).grid(row=0, column=3)
        Entry(F1, width=12, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=4, padx=10, pady=3)
        Button(F1,width=12,text="Search",font=("times new roman", 14, "bold"), bg=bg_clr, fg="black", bd=10).grid(padx=10,pady=3,row=0, column=5)

        #   ***********************Output Area***********************
        F2 = Frame(self.root, bd=10, relief=GROOVE)
        F2.place(x=90, y=170, width=800, height=370)
        Label(F2, text="Output Text", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(F2, orient=VERTICAL)
        self.txtarea = Text(F2, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

if __name__ == "__main__":
    root = Tk()
    Ocr(root)
    root.mainloop()
