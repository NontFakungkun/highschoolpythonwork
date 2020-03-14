#import tkinter for GUI
from tkinter import *
from tkinter import ttk


class ChemData: #storing data form question_data.txt into q_list in the programme
    def __init__(self, topic, question, answer):
        
        #Converting the arguments into self variable and add them in q_list with append method
        self.topic = topic
        self.question = question
        self.answer = answer
        q_list.append(self)
        
#I decide to create ChemData as a support class because these 2 classes have different function and purpose
#ChemData is for transfering data from external text file into a list to be used in this code
#ChemQuiz is for GUI and the interaction of the program

class ChemQuiz: #containing GUI and functions
      
    
    def __init__(self, parent):#The constructor function for the class. Contain all GUI parts 
        
        #Introduction screen (First frame)
        self.introscreen = Frame(parent, bg="lightcyan", width="500", height="300")
        self.introscreen.grid(row=0, column=0)
        self.intro_banner = Label(self.introscreen, bg="black", fg="white", width=25, padx=20, pady=10, text="Welcome to Junior Chemistry Quiz", font=("Helvetica", "20", "bold italic"))
        self.intro_banner.grid(columnspan=3)
        self.desc_label = Label(self.introscreen, text="This is the basic chemistry education quiz \nfor Junior high school at 12-15 years old", font=("Helvetica", "12",), bg="light cyan")
        self.desc_label.grid(row=1, columnspan=2)     
        
        self.image = PhotoImage(file="flask.png")
        image_label = Label(self.introscreen, image=self.image, bg="light cyan")
        image_label.grid(row=2, columnspan=2, padx=10, pady=10)
        
        #Create name string variable and let the input value at name_entry to be the value
        self.name_label = Label(self.introscreen, text="Name", width=20, font=("Helvetica", "14", "bold italic"), bg="light cyan")
        self.name_label.grid(row=3, column=0, sticky="W")
        self.name = StringVar()
        self.name.set("") 
        self.name_entry = Entry(self.introscreen, textvariable=self.name, width=20)
        self.name_entry.grid(row=3, column=1, sticky="W")
        
        #SImilarly to name by now with age, the vairable is integer since age supposed to be a whole number so we can detect it easier
        self.age_label = Label(self.introscreen, text="Age", width=20, font=("Helvetica", "14", "bold italic"), bg="light cyan")
        self.age_label.grid(row=4, column=0, sticky="W")
        self.age = IntVar()
        self.age.set("")        
        self.age_entry = Entry(self.introscreen, textvariable=self.age, width=20)
        self.age_entry.grid(row=4, column=1, sticky="W")
        #Warning label now empty which will be replace later as the code progress
        self.warning_label = Label(self.introscreen, text = "", bg="light cyan")
        self.warning_label.grid(row=5, column=1, columnspan=3, sticky=W)
     
        #Create a list of question topic and a integer variable set to 0 
        self.lessons = ["Elements Symbol (Easy)", "Ionic Charge (Medium)", "Reaction (Hard)"]
        self.lesson = IntVar()
        self.lesson.set(0)

        self.choice_label = Label(self.introscreen, text="Choose level", width=15, font=("Helvetica", "14", "bold italic"), bg="light cyan")
        self.choice_label.grid(row=6, column=0, columnspan = 2)
        
        #for loop for efficiency in displaying radiobuttons. This loop can save some line used for coding the same thing 3 times
        #The for loop will repeat by the amount of value in the lessons list each radiobutton has value for themselves, the first one is 0, then 1 and 2 respectively. The value will be stored in lesson variable
        for i in range(len(self.lessons)):
            qset = Radiobutton(self.introscreen, variable = self.lesson, value = i, bg="light cyan", text = self.lessons[i], padx=50, width=10, height="2")
            qset.grid(row=i+7, column=0, columnspan = 2)  
            
        #Additional variable which will be used in runscreen function
        self.age_activator = 0
        
        #Next button for activating runscreen function
        self.next_button = Button(self.introscreen, text="Next", command = self.runscreen)
        self.next_button.grid(row=10, column=0, columnspan = 2)   
        
        
        
        #Question screen (Second frame)        
        self.questionscreen = Frame(parent, bg="cornflowerblue", width="500", height="300")
        self.question_banner = Label(self.questionscreen, bg="black", fg="white", width=31, padx=30, pady=10, text="", font=("Helvetica", "24", "bold italic"))
        self.question_banner.grid(columnspan=3)  
        
        #question number and score display and question label is set empty, waiting to be replace as the code progress
        self.question_number = Label(self.questionscreen, text="", width=20, font=("Helvetica", "14", "bold italic"), bg="cornflowerblue")
        self.question_number.grid(row=1, column=0, sticky="W")  
        self.score_display = Label(self.questionscreen, text="", width=20, font=("Helvetica", "14", "bold italic"), bg="cornflowerblue")
        self.score_display.grid(row=1, column=1, sticky="W")        
        self.question_label = Label(self.questionscreen, text="", width=55, font=("Helvetica", "8", "bold"), bg="cornflowerblue")
        self.question_label.grid(row=2, column=0, sticky="W")
        
        #An entry which the input value will be taken to check_answer function to check if it is correct or not
        self.answer_text = Entry(self.questionscreen, width=20)
        self.answer_text.grid(row=2, column=1, sticky="W")  
        
        #feedback label will also be replace as the code progress
        self.feedback = Label(self.questionscreen, text = "Click Check answer button", bg="cornflowerblue")
        self.feedback.grid(row = 3, column = 0)  
        
        #Check button to run check_answer function which will check for the right answer and give feedback
        self.check_button = Button(self.questionscreen, text="Check", command=self.check_answer)
        self.check_button.grid(row=3, column=1, sticky=W)
        
        #Run next_question function to skip the checking process and run the next question
        self.skip_question = Button(self.questionscreen, text="Skip", width = 5, command=self.next_question)
        self.skip_question.grid(row=3, column=2, sticky=W)
        
        self.space = Label(self.questionscreen, text="", bg="cornflowerblue")
        self.space.grid(row=4,columnspan=2)
        
        #Home button will take user back to login screen
        self.homebutton = Button(self.questionscreen, text="Home", command=self.home)
        self.homebutton.grid(row=5, column=2, sticky=W)         
        
        #Report Screen (Third frame)        
        self.reportscreen = Frame(parent, bg="lightskyblue", width="500", height="300")
        
        #force the frame to be in a certain size
        self.reportscreen.grid_propagate(0)
        
        #List of heading of report detail
        report_head = ["Name", "Age", "Score", "Percentage"]   
        self.report_topic = Label(self.reportscreen, text = "", width = 42, bg="black", fg="white", font = ("Helvetica", "15", "bold italic"))
        self.report_topic.grid(row = 0, columnspan = 3)
        
        #The range display report detail heading down the row with for loop, again, for efficiency coding and saving some more line
        for i in range(len(report_head)):
            heading = Label(self.reportscreen, text = report_head[i] + ":", width = 15, bg="lightskyblue", anchor = E, font = ("Helvetica", "12", "bold italic"))
            heading.grid(row = i+2, column = 0, sticky = "W")
            
        #The information for the report, taken from input variable, name and age
        self.report_name = Label(self.reportscreen, textvariable = self.name, width = 15, anchor = W, font = ("Helvetica", "12", "bold italic"), bg="lightskyblue")
        self.report_name.grid( row = 2, column = 1, sticky = "W")
        
        self.report_age = Label(self.reportscreen, textvariable = self.age, width = 15, anchor = W, font = ("Helvetica", "12", "bold italic"), bg="lightskyblue")
        self.report_age.grid( row = 3, column = 1, sticky = "W")
        
        #Empty text label waiting to be replace later in the code, will be replaced by score value after the quiz is done, cannot put score value in first since it is not defined yet in this line (score value will be defined in runscreen function)
        self.report_score = Label(self.reportscreen, text = "", width = 15, anchor = W, font = ("Helvetica", "12", "bold italic"), bg="lightskyblue")
        self.report_score.grid( row = 4, column = 1, sticky = "W")      
        
        #Similarly for score percentage
        self.score_percentage = Label(self.reportscreen, text = "", width = 15, anchor = W, font = ("Helvetica", "12", "bold italic"), bg="lightskyblue")
        self.score_percentage.grid( row = 5, column = 1, sticky = "W") 
        
        self.end_message = Label(self.reportscreen, text = "You have finished the quiz. We encourage you to try another one", width = "55", font = ("Helvetica", "8", "bold italic"), bg="lightskyblue")
        self.end_message.grid( row = 6, columnspan = 2)
        
        #The radiobutton choice similar to login screen. This is made so the same user can continue doing the next question set without entering the same information again
        self.choice_label = Label(self.reportscreen, text="Choose level", width=15, font=("Helvetica", "12", "bold italic"), bg="lightskyblue")
        self.choice_label.grid(row=7, column=0, sticky="W")

        for i in range(len(self.lessons)):
            qset = Radiobutton(self.reportscreen, variable = self.lesson, value = i, bg="lightskyblue", text = self.lessons[i], anchor = W, padx=50, width="10", height="2")
            qset.grid(row=i+8, column=0, sticky=W)      
            
        #next question button similarly to the one in login screen
        self.next_questionset = Button(self.reportscreen, text="Next", width = 10, command=self.runscreen)
        self.next_questionset.grid(row=9, column=1)
        
        #home button similarly to question screen
        self.restart_button = Button(self.reportscreen, text="Home", width = 10, command=self.home)
        self.restart_button.grid(row=9, column=2)
        
    def runscreen(self): #Function for checking the name and age input then proceed to switch from intro screen to question screen
        
        #create variables used in the function 1.index: Counting all question attempted 2.score: Count the correct answer
        self.index = 0
        self.score = 0     
        
        try:#try/except function can prevent invalid or error input e.g. NULL and letter input for age entry
            
            #detect for NULL input in name entry
            if self.name.get() == "":
                self.warning_label.configure(text = "Please enter your name")
                self.name_entry.focus()       
                
            #detect for invalid string input for name entry with isalpha method since isalpha method will return false if the value contains non-alphabet character
            elif self.name.get().strip().isalpha() == False:
                self.warning_label.configure(text = "Please enter valid name")
                self.name_entry.delete(0, END)
                self.name_entry.focus()   
                
            #detect for NULL input in age entry
            elif self.age.get() == "":
                self.warning_label.configure(text = "Please enter a number")
                self.age_entry.delete(0, END)
                self.age_entry.focus()  
                
            #detect for age entry over criteria. However, I still let the user access with a confirmation of off criteria age input
            elif self.age.get() > 15:
                self.warning_label.configure(text = "This quiz is made for children within 12-15 years old. \nClick again if you really want to do the quiz")
                self.age_entry.delete(0, END) 
                
                #An if statement used to allow the access to next screen with twice input as the first time click the next button will not proceed but activate key value will now able to proceed to the next screen if the age is entered
                if self.age_activator == 1:
                    self.introscreen.grid_remove()
                    self.questionscreen.grid()
                    self.next_question()  
                    
                #This is the reason I cannot put the age_activator variables with index and score variable as the variable is meant to be used for allowing the access for the second click. So, if I put age_activator variables together with other variables, its value will keep changing back to 0 and the code cannot proceed to next screen as the transaction occurs at age_activator == 1
                else:
                    self.age_activator += 1
                    
            #Similarly to the case above        
            elif self.age.get() <12:
                self.warning_label.configure(text = "This quiz is made for children within 12-15 years old. \nClick again if you really want to do the quiz")
                self.age_entry.delete(0, END) 
                if self.age_activator == 1: #Similarly to the case above
                    self.introscreen.grid_remove()
                    self.questionscreen.grid()
                    self.next_question()    
                else:
                    self.age_activator += 1
            elif self.age.get() <=0:
                self.warning_label.configure(text = "Please enter a positive number")
                self.age_entry.delete(0, END)   
                
            else: #if the name and age input value don't meet any false criteria, the screen then proceed to switch off login screen and display question screen(also report screen for restart_button in report screen)
                self.introscreen.grid_remove()
                self.reportscreen.grid_remove()
                self.questionscreen.grid()
                self.next_question()
                
        except ValueError: #Any invalid or error input will get this feedback and have to input the value again in valid form (not by any false criteria above)
            self.warning_label.configure(text = "Please enter valid age")
            self.age_entry.delete(0, END)
            self.age_entry.focus()
    
    
    def home(self): #Use for switch all other screen into login screen
        
        #Remove question or report screen then remove all input value on entry, ready for the new user
        self.questionscreen.grid_remove()
        self.reportscreen.grid_remove()
        
        self.name_entry.delete(0, END)
        self.age_entry.delete(0, END)
        
        #Also, reset some variable for the next quiz to remain the same work as when the code starts
        self.age_activator = 0
        self.warning_label.configure(text = "")
        self.feedback.configure(text = "")
        self.introscreen.grid()
        
        
    def next_question(self): #The function is for displaying the next question according to the topic selected
        self.question_choice = self.lesson.get() 
        
        #The banner will display heading accorind to the chosen topic at the start
        self.question_banner.configure(text = "{} Quiz".format(self.lessons[self.question_choice])) 
        
        #If the first question set is selected (run the question number index (0) which is the first line. The question label will be replce by the question in line according to index while the correct answer for the question will store in a variable)
        if self.question_choice == 0: 
            
            #transfer question amount to a variable so we can use a single line works for this varaible for all question sets. This increases flexibility to the code since it now can handle the any number of question in a same topic
            self.question_number_text = str(question_number_set0)
            easyquestion_text = q_list[self.index].question
            self.correct_answer = q_list[self.index].answer  
            self.question_label.configure(text = easyquestion_text) 
            
            #If the second question set(Ionic Charge) is selected (run the question number index(0) plus amount of quetion before the first topic. This increases flexibility to the code since it now can handle the any number of question in a same topic
        elif self.question_choice == 1:
            self.question_number_text = str(question_number_set1)
            mediumquestion_text = q_list[self.index+question_number_set0].question
            self.correct_answer = q_list[self.index+question_number_set0].answer
            self.question_label.configure(text = mediumquestion_text) 
            
        else: 
            self.question_number_text = str(question_number_set2)
            # This if statement exist to fix a problem that after the last line in the list is shown, the code cannot proceed because the index is out of range from the index+=1 below as it will try to play the next line below the last line which is not exist and give error
            
            #This if statement will display question as long as it is not the last question, when the index number pass the question amount, skip the process so error won't occur. This line also apply to all question_set since the amount will be stored in this 'question_number_text' variable one at a time(for a quiz running)
            if self.index < int(self.question_number_text):
                #If the third question set (Reaction) is selected (run the question number index(0) plus amount of question before the first two topics. This increases flexibility to the code since it now can handle the any number of question in a same topic
                #structure also make code become more dynamic
                hardquestion_text = q_list[self.index+question_number_set1+question_number_set0].question
                self.correct_answer = q_list[self.index+question_number_set1+question_number_set0].answer
                self.question_label.configure(text = hardquestion_text) 
            else:
                pass
            
        #increase the number of question attempted every the function pass so the next question can comeup when next_button feedback, line reading in questin_data text is according to index value
        self.index += 1    
        
        #Replace question number and score display with the text below with the maximum question amount is the counted value for each question set. This increase flexibility of the program since it will automatically change according to the amount of questions with the same topic
        
        #There is no problem using the same variable 'question_number_text' for all question_number_set variable because I know that the value will not be replace for running the code one full time. This also benefit me as I can write a line that can still work for all question set independently
        self.question_number.configure(text = "Question " + str(self.index)+ "/" + str(self.question_number_text))
        self.score_display.configure(text = "Score" + str(self.score) + "/" + str(self.question_number_text))
        
        #when index number surpass the last question of the question set, procees to report screen while replace report score, topic and score percentage are now replaced
        if self.index > int(self.question_number_text): 
            
            #Switch from question to report screen
            self.questionscreen.grid_remove() 
            self.reportscreen.grid() 
            
            #replace report score and topic with the given information 
            self.report_score.configure(text = int(self.score))  
            self.report_topic.configure(text = "Topic:" + self.lessons[self.question_choice]) 
            
            #I calculate the score with all question numbers x 100 with it showing 2 decimal numbers
            self.score_percentage.configure(text =  "{:.2f} %".format(float(self.score) / float(self.question_number_text)*100))
            
    
    
    def check_answer(self): #Check for the correct answer when user attempt to and count the amount of correct answer in score variable
        
        if self.question_choice == 0:#If the first question set (Element Symbol) is selected
            
            #Any invalid input just in any unexpected case
            try:
                #The answer is taken from input value in answer_text entry with get method and takes all space before and after the word out with strip method because I know all answer in this set is a word and any space typed in by mistake around the word can be taken out. Also, capitalize is very important for element symbol so the user supposed to put the answer with capitalization on theright place.
                answer = self.answer_text.get().strip() 
                
                #Prevent any non-alphabet input wince the answer are all alphabet
                if answer.isalpha() == False:
                    self.feedback.configure(text = "Please enter your answer with alphabet only")
                    self.answer_text.delete(0, END)
                    self.answer_text.focus()     
                    
                #For correct answer, score increases by 1
                elif answer == self.correct_answer:
                    self.feedback.configure(text = "")
                    self.score += 1
                    self.answer_text.delete(0, END)
                    self.answer_text.focus()
                    self.next_question()
                    
                #for wrong answer, no score increases
                else:
                    self.feedback.configure(text = "You might have to capitalize your answer")
                    self.answer_text.delete(0, END)
                    self.answer_text.focus()
                    self.next_question()
            except ValueError:
                    self.feedback.configure(text = "Please enter your answer")
                    self.answer_text.delete(0, END)
                    self.answer_text.focus()            
            
        elif self.question_choice == 1:#If the second question set (Ionic Charge) is selected
            try:#Prevent any invalid and alphabet input since the answer has to be a number
                
                #The answer is taken from input value in answer_text entry with get method which is converted into an integer
                answer = int(self.answer_text.get())
                
                #For correct answer, score increases by 1
                if answer == int(self.correct_answer):
                    self.feedback.configure(text = "")
                    self.score += 1
                    self.answer_text.delete(0, END)
                    self.answer_text.focus()
                    self.next_question()
                    
                #for wrong answer, no score increases
                else:
                    self.feedback.configure(text = "")
                    self.answer_text.delete(0, END)
                    self.answer_text.focus()
                    self.next_question()
            except ValueError:
                    self.feedback.configure(text = "Please enter your answer with number only")
                    self.answer_text.delete(0, END)
                    self.answer_text.focus()
        else:#If the third question set (Reaction) is selected
            
            try:#Any invalid input just in any unexpected case
                
                #The answer is taken from input value in answer_text entry with get method and is converted into all lower-case modewith lower method as I think there is a lot of possibility for user to open with or without capitalize which might cause them to lose score unnescessarily, and as the answers are mostly words so I decide to convert all answers in reaction question set into lower case for higher chance of user to get correct answer
                answer = self.answer_text.get().lower()
                
                #Prevent NULL input, feedback below will be shown
                if answer == "":
                    self.feedback.configure(text = "Please enter your answer")
                    self.answer_text.delete(0, END)
                    self.answer_text.focus()      
                    
                #For correct answer, score increases by 1
                elif answer == self.correct_answer:
                    self.feedback.configure(text = "")
                    self.score += 1
                    self.answer_text.delete(0, END)
                    self.answer_text.focus()
                    self.next_question()
                    
                #For wrong answer, no score increases
                else:
                    self.feedback.configure(text = "")
                    self.answer_text.delete(0, END)
                    self.answer_text.focus()
                    self.next_question()
            except ValueError:
                    self.feedback.configure(text = "Please enter your answer")
                    self.answer_text.delete(0, END)
                    self.answer_text.focus() 
                    
    
#The function has 2 purpose. 1.Read all line of data in question.txt and store them in q_list 2.count the question amount for different question topic
def store_data(question_number_set0, question_number_set1, question_number_set2): 
    
    #read all data from question_data.txt which contains question topic,detail, and answer in each line
    question_data = open("question_data.txt","r")
    
    #Take data out with readlines method and store lines of data in a variable 
    data_lines = question_data.readlines()
    
    #The process will repeat for each line, separate the value for different categories (topic. question, answer) with "," by split method and run support class ChemData with the stored variable to append all value into q_list
    for line in data_lines:
        stored_data_line = line.strip().split(",")
        ChemData(*stored_data_line)
        question_data.close()
        
    #These set of loops is used to count the amount of question line which contain the same topic as listed
    #The loop function is run every line and any line with the detected topic value as the same as listed will add 1 into the question_number_set, the line with other topic will cause function to do nothing
    #The first question set 'Elements Symbol', the question amount store in question_number_set0
    for i in range(len(q_list)):
        if q_list[i].topic == "Elements Symbol":
            question_number_set0 += 1
        else: 
            pass
        
    #The second question set 'Ionic Charge', the question amount store in question_number_set1
    for i in range(len(q_list)):
        if q_list[i].topic == "Ionic Charge":
            question_number_set1 += 1
        else: 
            pass
        
    #The third question set 'Reaction', the question amount store in question_number_set2
    for i in range(len(q_list)):
        if q_list[i].topic == "Reaction":
            question_number_set2 += 1
        else: 
            pass
        
    #return all changed values out to main routine respectively. The returned number in function must be align with the variable to be received in the main routine so the value won't be swapped 
    return question_number_set0, question_number_set1, question_number_set2

#Main Routine     
if __name__ == "__main__":
    
    #Set up GUI in class ChemQuiz and set it title
    root = Tk()
    frames = ChemQuiz(root)
    root.title("Junior High School Chem Quiz")  
    
    #create empty lists for data and variable for counting number of each section
    q_list = []
    question_number_set0 = 0
    question_number_set1 = 0
    question_number_set2 = 0
    
    #Use the created variables as arguments and return their value out to the same variables in store_data function
    question_number_set0, question_number_set1, question_number_set2 = store_data(question_number_set0, question_number_set1, question_number_set2)
    
    #Run mainploop for GUI which is in class ChemQuiz
    root.mainloop()