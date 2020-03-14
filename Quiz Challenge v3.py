from tkinter import *
from tkinter import ttk


class ChemData: #storing data form data.txt into q_list in the programme
    def __init__(self, topic, question, answer):
        
        self.topic = topic
        self.question = question
        self.answer = answer
        q_list.append(self)

class ChemQuiz: #containing GUI and functions
      
    
    def __init__(self, parent):
        
#Intriduction screen (First frame)
        self.introscreen = Frame(parent, bg="lightcyan", width="500", height="300")
        self.introscreen.grid(row=0, column=0)
        self.introbanner = Label(self.introscreen, bg="black", fg="white", width=25, padx=20, pady=10, text="Welcome to Junior Chemistry Quiz", font=("Helvetica", "20", "bold italic"))
        self.introbanner.grid(columnspan=3)
        self.desclabel = Label(self.introscreen, text="This is the basic chemistry education quiz for Junior high school at 12-15 years old", font=("Helvetica", "12",), bg="light cyan")
        self.desclabel.grid(row=1, columnspan=2, sticky="W")     
        
        self.namelabel = Label(self.introscreen, text="Name", width=20, font=("Helvetica", "14", "bold italic"), bg="light cyan")
        self.namelabel.grid(row=3, column=0, sticky="W")
        self.name = StringVar()
        self.name.set("") 
        self.nameentry = Entry(self.introscreen, textvariable=self.name, width=20)
        self.nameentry.grid(row=3, column=1, sticky="W")
        
        self.agelabel = Label(self.introscreen, text="Age", width=20, font=("Helvetica", "14", "bold italic"), bg="light cyan")
        self.agelabel.grid(row=4, column=0, sticky="W")
        self.age = IntVar()
        self.age.set("")        
        self.ageentry = Entry(self.introscreen, textvariable=self.age, width=20)
        self.ageentry.grid(row=4, column=1, sticky="W")
        self.warninglabel = Label(self.introscreen, text = "", bg="light cyan")
        self.warninglabel.grid(row=5, column=1, columnspan=3, sticky=W)
     
        
        self.choicelabel = Label(self.introscreen, text="Choose level", width=15, font=("Helvetica", "14", "bold italic"), bg="light cyan")
        self.choicelabel.grid(row=6, column=0, sticky="W")
    

        self.lessons = ["Elements Symbol", "Ionic Charge", "Reaction"]
        self.lesson = StringVar()
        self.lesson.set(0)

        for i in range(len(self.lessons)):
            qset = Radiobutton(self.introscreen, variable = self.lesson, value = i, bg="light cyan", text = self.lessons[i], anchor = W, padx=50, width="10", height="2")
            qset.grid(row=i+7, column=0, sticky=W)            

        self.nextbutton = Button(self.introscreen, text="Next", command = self.runscreen)
        self.nextbutton.grid(row=8, column=1)   
        
#
        self.index = 0
        self.score = 0
        
#Question screen (Second frame)        
        self.questionscreen = Frame(parent, bg="cornflowerblue", width="500", height="300")
        self.questionbanner = Label(self.questionscreen, bg="black", fg="white", width=20, padx=30, pady=10, text="{} Quiz".format(self.lessons[i]), font=("Helvetica", "24", "bold italic"))
        self.questionbanner.grid(columnspan=3)    
        
        self.question_number = Label(self.questionscreen, text="", width=20, font=("Helvetica", "14", "bold italic"), bg="cornflowerblue")
        self.question_number.grid(row=1, column=0, sticky="W")  

        self.question_label = Label(self.questionscreen, text="", width=20, font=("Helvetica", "14", "bold italic"), bg="cornflowerblue")
        self.question_label.grid(row=2, column=0, sticky="W")
        self.answer_text = Entry(self.questionscreen, width=20)
        self.answer_text.grid(row=2, column=1, sticky="W")  
        self.feedback = Label(self.questionscreen, text = "Click Check answer button", bg="cornflowerblue")
        self.feedback.grid(row = 3, column = 0)  
        
        self.checkbutton = Button(self.questionscreen, text="Check", command=self.check_answer)
        self.checkbutton.grid(row=3, column=1, sticky=W)
        self.nextquestion = Button(self.questionscreen, text="Next", width = 5, command=self.next_question, relief = RIDGE)
        self.nextquestion.grid(row=3, column=2, sticky=W)
        
        
        self.homebutton = Button(self.questionscreen, text="Home", command=self.home)
        self.homebutton.grid(row=4, column=2, sticky="E")         
        
#Report Screen (Third frame)        
        self.reportscreen = Frame(parent, bg="lightskyblue", width="500", height="300")
        
        
    def runscreen(self):
        try:
            if self.name.get() == "":
                self.warninglabel.configure(text = "Please enter your name")
                self.nameentry.focus()             
            elif self.name.get().strip().isalpha() == False:
                self.warninglabel.configure(text = "Please enter your name")
                self.nameentry.delete(0, END)
                self.nameentry.focus()                
            elif self.age.get() == "":
                self.warninglabel.configure(text = "Please enter a number")
                self.ageentry.delete(0, END)                
            elif self.age.get() > 15:
                self.warninglabel.configure(text = "You are too old to play this game")
                self.ageentry.delete(0, END)                
            elif self.age.get() <=0:
                self.warninglabel.configure(text = "Please enter a positive number")
                self.ageentry.delete(0, END)                
            elif self.age.get() <12:
                self.warninglabel.configure(text = "You are too young to play this game!")    
                self.ageentry.delete(0, END) 
            else:
                self.introscreen.grid_remove()
                self.questionscreen.grid()
                self.next_question()
        except ValueError:
            self.warninglabel.configure(text = "Please enter a number")
            self.ageentry.delete(0, END)
            self.ageentry.focus()
    
    
    def home(self):
        pass
        
        
    def next_question(self):
        self.question_choice = self.lesson.get() 
        
        if self.question_choice == 0: 
            questionset1_text = q_list[self.index+1].question
            self.answer = q_list[self.index+1].answer 
            self.index +=1 
            self.question_label.configure(text = questionset1_text) 
            self.question_number.configure(text = "Question" + str(self.index)+ "/10") 
    
        elif self.question_choice == 1: 
            questionset2_text = q_list[self.index+11].question
            self.answer = q_list[self.index+11].answer
            self.index +=1 
            self.question_label.configure(text = questionset2_text) 
            self.question_number.configure(text = "Question" + str(self.index)+ "/10") 
            
        else: 
            questionset3_text = q_list[self.index+21].question
            self.answer = q_list[self.index+21].answer
            self.index +=1 
            self.question_label.configure(text = questionset3_text) 
            self.question_number.configure(text = "Question" + str(self.index)+ "/10") 
        
        if self.index >= 10: 
            self.questionscreen.grid_remove() 
            self.reportscreen.grid(row = 1, columnspan = 4) 
    
    
    def check_answer(self):
        pass
    
    
    
    
    
#Main Routine        
def store_data(): #read all data from question_data.txt and store all value with in the list created separate by line
    question_data = open("question_data.txt","r")
    data_lines = question_data.readlines()
    
    for line in data_lines:
        stored_data_lines = line.strip().split(",")
        ChemData(*stored_data_lines)
        question_data.close()
        
if __name__ == "__main__":
    root = Tk()
    frames = ChemQuiz(root)
    root.title("Junior High School Chem Quiz")   
    q_list = []
    store_data()
    root.mainloop()