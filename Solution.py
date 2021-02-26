"""

Author : Durmuş Kartci
Date   : 15 Feb 2021
GitHub : DurmushKartci

"""
# Solution Class holds the question's answer and solution ways

    # ID                -> Integer
    # Question          -> Question Object

## Imports
import os # To see and change the Directiry

class Solution:

    #Constructor
    def __init__(self,ID,Question):

        # Assign properties
        self.ID             = ID
        self.Question       = Question
        self.solutionString = " There is no solution assigned for the question!!"

        # Show the solution on the console
    def show_solution_console(self,willPrint = True):

        # Create a string to prepare good format
        solutionContent = """\n
Solution ID      : {}
Question         : {}\n
Solution         : {}""".format(self.ID,self.Question,self.solutionString)

        # if the user wants to print to the console
        if willPrint:
            # Print the file to the console
            print(solutionContent)

        # Return the string to use another way
        return solutionContent

    # Save the solutoin as txt file
    # Default path is {ID}.txt
    def save_solution_as_txt(self,willPrint = False):
        # Try to execute these operations
        try:

            solutionString = self.show_solution_console(False)

            save_path  = os.path.join( os.getcwd()+"/Assests/Solutions/", str(self.ID)+".txt")

            # If willSaved is true save the Test properties as ID+".txt" file
            solutionFile = open(save_path,"w") 

            # Write in the file 
            solutionFile.write("--------> SOLUTİON OBJECT <--------\n")
            solutionFile.write(solutionString)
            solutionFile.write("\n\nAll Rights are Reserved @2021 A-MEAN Company")
            # Close the file properly
            solutionFile.close() 

            # Inform the user
            print(f"The Solution {self.ID} saved successfully.")
        
        # If any problem occurs
        except:
            # Inform the user !!
            print(f"The Solution {self.ID} cannot saved !! Try again ...")





# DRIVER PROGRAM

Math_Test_Solution = Solution(2,"Which genius is the best one !!")

Math_Test_Solution.show_solution_console()

Math_Test_Solution.save_solution_as_txt()