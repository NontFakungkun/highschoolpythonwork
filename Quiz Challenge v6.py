from tkinter import *
from tkinter import ttk


class ChemData: #storing data form question_data.txt into q_list in the programme
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
        self.desclabel = Label(self.introscreen, text="This is the basic chemistry education quiz \nfor Junior high school at 12-15 years old", font=("Helvetica", "12",), bg="light cyan")
        self.desclabel.grid(row=1, columnspan=2)     
        
        self.image = PhotoImage(file="flask.png")
        image_label = Label(self.introscreen, image=self.image, bg="light cyan")
        image_label.grid(row=2, columnspan=2, padx=10, pady=10)
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
        self.choicelabel.grid(row=6, column=0, columnspan = 2)
    

        self.lessons = ["Elements Symbol (Easy)", "Ionic Charge (Medium)", "Reaction (Hard)"]
        self.lesson = IntVar()
        self.lesson.set(0)

        for i in range(len(self.lessons)):
            qset = Radiobutton(self.introscreen, variable = self.lesson, value = i, bg="light cyan", text = self.lessons[i], padx=50, width=10, height="2")
            qset.grid(row=i+7, column=0, columnspan = 2)  
        # additional variable which will be used in rescreen function    
        self.age_activator = 0

        self.nextbutton = Button(self.introscreen, text="Next", command = self.runscreen)
        self.nextbutton.grid(row=10, column=0, columnspan = 2)   
        
#
        
        
#Question screen (Second frame)        
        self.questionscreen = Frame(parent, bg="cornflowerblue", width="500", height="300")
        self.questionbanner = Label(self.questionscreen, bg="black", fg="white", width=20, padx=30, pady=10, text="", font=("Helvetica", "24", "bold italic"))
        self.questionbanner.grid(columnspan=3)    
        
        self.question_number = Label(self.questionscreen, text="", width=20, font=("Helvetica", "14", "bold italic"), bg="cornflowerblue")
        self.question_number.grid(row=1, column=0, sticky="W")  
        self.score_display = Label(self.questionscreen, text="", width=20, font=("Helvetica", "14", "bold italic"), bg="cornflowerblue")
        self.score_display.grid(row=1, column=1, sticky="W")        

        self.question_label = Label(self.questionscreen, text="", width=40, font=("Helvetica", "8", "bold"), bg="cornflowerblue")
        self.question_label.grid(row=2, column=0, sticky="W")
        self.answer_text = Entry(self.questionscreen, width=20)
        self.answer_text.grid(row=2, column=1, sticky="W")  
        self.feedback = Label(self.questionscreen, text = "Click Check answer button", bg="cornflowerblue")
        self.feedback.grid(row = 3, column = 0)  
        
        self.checkbutton = Button(self.questionscreen, text="Check", command=self.check_answer)
        self.checkbutton.grid(row=3, column=1, sticky=W)
        self.skipquestion = Button(self.questionscreen, text="Skip", width = 5, command=self.next_question)
        self.skipquestion.grid(row=3, column=2, sticky=W)
        
        self.space = Label(self.questionscreen, text="", bg="cornflowerblue")
        self.space.grid(row=4,columnspan=2)
        
        self.homebutton = Button(self.questionscreen, text="Home", command=self.home)
        self.homebutton.grid(row=5, column=2, sticky=W)         
        
#Report Screen (Third frame)        
        self.reportscreen = Frame(parent, bg="lightskyblue", width="500", height="300")
        self.reportscreen.grid_propagate(0)
        report_head = ["Name", "Age", "Score"]
            
        self.report_topic = Label(self.reportscreen, text = "", width = 25, bg="lightskyblue", font = ("Helvetica", "15", "bold italic"))
        self.report_topic.grid(row = 0, columnspan = 3)
        for i in range(len(report_head)):
            rb = Label(self.reportscreen, text = report_head[i] + ":", width = 15, bg="lightskyblue", anchor = E, font = ("Helvetica", "12", "bold italic"))
            rb.grid(row = i+2, column = 0, sticky = "W")
            
        self.report_name = Label(self.reportscreen, textvariable = self.name, width = 15, anchor = W, font = ("Helvetica", "12", "bold italic"), bg="lightskyblue")
        self.report_name.grid( row = 2, column = 1, sticky = "W")
        
        self.report_age = Label(self.reportscreen, textvariable = self.age, width = 15, anchor = W, font = ("Helvetica", "12", "bold italic"), bg="lightskyblue")
        self.report_age.grid( row = 3, column = 1, sticky = "W")
        
        self.report_score = Label(self.reportscreen, text = "", width = 15, anchor = W, font = ("Helvetica", "12", "bold italic"), bg="lightskyblue")
        self.report_score.grid( row = 4, column = 1, sticky = "W")         
        
        self.end_message = Label(self.reportscreen, text = "You have finished the quiz. We encourage you to try another one", width = "55", font = ("Helvetica", "8", "bold italic"), bg="lightskyblue")
        self.end_message.grid( row = 5, columnspan = 2)
        
        self.choicelabel = Label(self.reportscreen, text="Choose level", width=15, font=("Helvetica", "12", "bold italic"), bg="lightskyblue")
        self.choicelabel.grid(row=6, column=0, sticky="W")

        for i in range(len(self.lessons)):
            qset = Radiobutton(self.reportscreen, variable = self.lesson, value = i, bg="lightskyblue", text = self.lessons[i], anchor = W, padx=50, width="10", height="2")
            qset.grid(row=i+7, column=0, sticky=W)        
            
        self.next_questionset = Button(self.reportscreen, text="Next", width = 10, command=self.runscreen)
        self.next_questionset.grid(row=8, column=1)
        
        self.restartbutton = Button(self.reportscreen, text="Home", width = 10, command=self.home)
        self.restartbutton.grid(row=8, column=2)
        
    def runscreen(self):
        self.index = 0
        self.score = 0        
        try:

            if self.name.get() == "":
                self.warninglabel.configure(text = "Please enter your name")
                self.nameentry.focus()             
            elif self.name.get().strip().isalpha() == False:
                self.warninglabel.configure(text = "Please enter valid name")
                self.nameentry.delete(0, END)
                self.nameentry.focus()   
            elif self.age.get() == "":
                self.warninglabel.configure(text = "Please enter a number")
                self.ageentry.delete(0, END)
                self.ageentry.focus()                
            elif self.age.get() > 15:
                self.warninglabel.configure(text = "This quiz is made for children within 12-15 years old. \nClick again if you really want to do the quiz")
                self.ageentry.delete(0, END) 
                if self.age_activator == 1:
                    self.introscreen.grid_remove()
                    self.questionscreen.grid()
                    self.next_question()    
                else:
                    self.age_activator += 1
            elif self.age.get() <=0:
                self.warninglabel.configure(text = "Please enter a positive number")
                self.ageentry.delete(0, END)                
            elif self.age.get() <12:
                self.warninglabel.configure(text = "This quiz is made for children within 12-15 years old. \nClick again if you really want to do the quiz")
                self.ageentry.delete(0, END) 
                if self.age_activator == 1:
                    self.introscreen.grid_remove()
                    self.questionscreen.grid()
                    self.next_question()    
                else: 
                    self.age_activator += 1
            else:
                self.introscreen.grid_remove()
                self.reportscreen.grid_remove()
                self.questionscreen.grid()
                self.next_question()
        except ValueError:
            self.warninglabel.configure(text = "Please enter valid age")
            self.ageentry.delete(0, END)
            self.ageentry.focus()
    
    
    def home(self):
        self.questionscreen.grid_remove()
        self.reportscreen.grid_remove()
        self.nameentry.delete(0, END)
        self.ageentry.delete(0, END)
        self.age_activator = 0
        self.warninglabel.configure(text = "")
        self.feedback.configure(text = "")
        self.introscreen.grid()
        
        
    def next_question(self):
        self.question_choice = self.lesson.get() 
        self.questionbanner.configure(text = "{} Quiz".format(self.lessons[self.question_choice])) 
        
        if self.question_choice == 0: 
            self.question_number_text = str(question_number_set0)
            easyquestion_text = q_list[self.index].question
            self.correct_answer = q_list[self.index].answer  
            self.question_label.configure(text = easyquestion_text) 
            
    
        elif self.question_choice == 1: 
            self.question_number_text = str(question_number_set1)
            mediumquestion_text = q_list[self.index+question_number_set0].question
            self.correct_answer = q_list[self.index+question_number_set0].answer
            self.question_label.configure(text = mediumquestion_text) 
            
            
        else: 
            self.question_number_text = str(question_number_set2)
            if self.index < int(self.question_number_text):
                hardquestion_text = q_list[self.index+question_number_set1+question_number_set0].question
                self.correct_answer = q_list[self.index+question_number_set1+question_number_set0].answer
                self.question_label.configure(text = hardquestion_text) 
            else:
                pass
   
        self.index += 1    
            
        self.question_number.configure(text = "Question " + str(self.index)+ "/" + str(self.question_number_text))
        self.score_display.configure(text = "Score" + str(self.score) + "/" + str(self.question_number_text))
        if self.index > int(self.question_number_text): 
            self.questionscreen.grid_remove() 
            self.reportscreen.grid() 
            self.report_score.configure(text = int(self.score))  
            self.report_topic.configure(text = "Topic: " + self.lessons[self.question_choice])  
    
    
    def check_answer(self):
        if self.question_choice == 0:
            try:
                answer = self.answer_text.get().strip()                    
                if answer.isalpha() == False:
                    self.feedback.configure(text = "Please enter your answer with alphabet only")
                    self.answer_text.delete(0, END)
                    self.answer_text.focus()                    
                elif answer == self.correct_answer:
                    self.feedback.configure(text = "")
                    self.score += 1
                    self.answer_text.delete(0, END)
                    self.answer_text.focus()
                    self.next_question()
                else:
                    self.feedback.configure(text = "You might have to capitalize your answer")
                    self.answer_text.delete(0, END)
                    self.answer_text.focus()
                    self.next_question()
            except ValueError:
                    self.feedback.configure(text = "Please enter your answer")
                    self.answer_text.delete(0, END)
                    self.answer_text.focus()            
            
        elif self.question_choice == 1:
            try:
                answer = int(self.answer_text.get())
                if answer == int(self.correct_answer):
                    self.feedback.configure(text = "")
                    self.score += 1
                    self.answer_text.delete(0, END)
                    self.answer_text.focus()
                    self.next_question()
                else:
                    self.feedback.configure(text = "")
                    self.answer_text.delete(0, END)
                    self.answer_text.focus()
                    self.next_question()
            except ValueError:
                    self.feedback.configure(text = "Please enter your answer with number only")
                    self.answer_text.delete(0, END)
                    self.answer_text.focus()
        else:
            try:
                answer = self.answer_text.get().lower()
                if answer == "":
                    self.feedback.configure(text = "Please enter your answer")
                    self.answer_text.delete(0, END)
                    self.answer_text.focus()                 
                elif answer == self.correct_answer:
                    self.feedback.configure(text = "")
                    self.score += 1
                    self.answer_text.delete(0, END)
                    self.answer_text.focus()
                    self.next_question()
                else:
                    self.feedback.configure(text = "")
                    self.answer_text.delete(0, END)
                    self.answer_text.focus()
                    self.next_question()
            except ValueError:
                    self.feedback.configure(text = "Please enter your answer")
                    self.answer_text.delete(0, END)
                    self.answer_text.focus() 

    
    
    
#Main Routine        
def store_data(question_number_set0, question_number_set1, question_number_set2): 
    #read all data from question_data.txt and store all value with in the list created separate by line
    question_data = open("question_data.txt","r")
    data_lines = question_data.readlines()
    
    for line in data_lines:
        stored_data_lines = line.strip().split(",")
        ChemData(*stored_data_lines)
        question_data.close()
        
    for i in range(len(q_list)):
        if q_list[i].topic == "Elements Symbol":
            question_number_set0 += 1
        else: 
            pass
    for i in range(len(q_list)):
        if q_list[i].topic == "Ionic Charge":
            question_number_set1 += 1
        else: 
            pass
    for i in range(len(q_list)):
        if q_list[i].topic == "Reaction":
            question_number_set2 += 1
        else: 
            pass
    print(question_number_set0, question_number_set1, question_number_set2)
    return question_number_set0, question_number_set1, question_number_set2
        
if __name__ == "__main__":
    root = Tk()
    frames = ChemQuiz(root)
    root.title("Junior High School Chem Quiz")   
    q_list = []
    question_number_set0 = 0
    question_number_set1 = 0
    question_number_set2 = 0
    question_number_set0, question_number_set1, question_number_set2 = store_data(question_number_set0, question_number_set1, question_number_set2)
    root.mainloop()