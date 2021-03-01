"""

Author : Kerem Tuna
Date   : 1 March 2021
GitHub : kt980610

"""

## Imports
import os # To see and change the Directiry

class Question:

    #Constructor
    def __init__(self,ID,questionString,answer,subject,solution,options):
         # Assign properties
        self.ID = ID

        self.questionString     = questionString
        self.options            = options
        self.answer             = answer
        self.subject            = subject
        self.solution           = solution

    def show_question_console(self,willPrint = True):

        # Create a string to prepare good format
        questionContent = """\n
Question ID      : {}
Question         : {}\n
\nA) {}
\nB) {}
\nC) {}
\nD) {}
\nE) {}""".format(self.ID,self.questionString,*self.options)

        # if the user wants to print to the console
        if willPrint:
            # Print the file to the console
            print(questionContent)

        # Return the string to use another way
        return questionContent

    # Save the solutoin as txt file
    # Default path is {ID}.txt
    def save_question_as_txt(self,willPrint = False):
        # Try to execute these operations
        try:

            questionString = self.show_question_console(False)

            save_path  = os.path.join( os.getcwd()+"/Assests/Questions/", str(self.ID)+".txt")

            # If willSaved is true save the Test properties as ID+".txt" file
            questionFile = open(save_path,"w") 

            # Write in the file 
            questionFile.write("--------> QUESTION OBJECT <--------\n")
            questionFile.write(questionString)
            questionFile.write("\n\nAll Rights are Reserved @2021 A-MEAN Company")
            # Close the file properly
            questionFile.close() 

            # Inform the user
            print(f"The Question {self.ID} saved successfully.")
        
        # If any problem occurs
        except:
            # Inform the user !!
            print(f"The Question {self.ID} cannot saved !! Try again ...")


# DRIVER PROGRAM

Question1 = Question(2,"Which genius is the best?","Leonardo Da Vinci","Culture","Because Da Vinci can do everything.",["Sherlock","Newton","Darwin","Emin","Da Vinci"])

Question1.show_question_console()
# Math_Test_Solution.save_solution_as_txt()

Question1.save_question_as_txt()


