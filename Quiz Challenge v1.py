from tkinter import *
from tkinter import ttk
import random

class ChemQuiz:
      
    
    def __init__(self, parent):
        

        self.frame0 = Frame(parent, bg="lightcyan", width="500", height="300")
        self.frame0.grid(row=0, column=0)
        self.label0 = Label(self.frame0, bg="black", fg="white", width=25, padx=20, pady=10, text="Welcome to Junior Chemistry Quiz", font=("Helvetica", "20", "bold italic"))
        self.label0.grid(columnspan=3)
        self.description = Label(self.frame0, text="This is the basic chemistry education quiz for Junior high school at 12-15 years old", font=("Helvetica", "12",), bg="light cyan")
        self.description.grid(row=1, columnspan=2, sticky="W")     
        
        self.labelname = Label(self.frame0, text="Name", width=20, font=("Helvetica", "14", "bold italic"), bg="light cyan")
        self.labelname.grid(row=3, column=0, sticky="W")
        self.name = StringVar()
        self.name.set("") 
        self.nameentry = Entry(self.frame0, textvariable=self.name, width=20)
        self.nameentry.grid(row=3, column=1, sticky="W")
        
        self.labelage = Label(self.frame0, text="Age", width=20, font=("Helvetica", "14", "bold italic"), bg="light cyan")
        self.labelage.grid(row=4, column=0, sticky="W")
        self.age = IntVar()
        self.age.set("")        
        self.ageentry = Entry(self.frame0, textvariable=self.age, width=20)
        self.ageentry.grid(row=4, column=1, sticky="W")
        self.warning = Label(self.frame0, text = "", bg="light cyan")
        self.warning.grid(row=5, column=1, columnspan=3, sticky=W)
     
        
        self.selectlabel = Label(self.frame0, text="Choose level", width=15, font=("Helvetica", "14", "bold italic"), bg="light cyan")
        self.selectlabel.grid(row=6, column=0, sticky="W")
    

        self.diff = ["Elements Symbol", "Ionic Charge", "Reaction"]
        self.diff_lvl = StringVar()
        self.diff_lvl.set(0)

        for i in range(len(self.diff)):
            rb = Radiobutton(self.frame0, variable = self.diff_lvl, value = i, bg="light cyan", text = self.diff[i], anchor = W, padx=50, width="10", height="2")
            rb.grid(row=i+7, column=0, sticky=W)            

        self.nextbutton = Button(self.frame0, text="Next")
        self.nextbutton.grid(row=8, column=1)   
        
if __name__ == "__main__":
    root = Tk()
    frames = ChemQuiz(root)
    root.title("Junior High School Chem Quiz")    
    root.mainloop()