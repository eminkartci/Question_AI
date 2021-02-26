"""

Author : Durmuş Kartci
Date   : 15 Feb 2021
GitHub : DurmushKartci

"""
# Solution Class holds the question's answer and solution ways

    # ID                -> Integer
    # Question          -> Question Object List 
class Solution:

    #Constructor
    def __init__(self,ID,Question):

        # Assign properties
        self.ID             = ID
        self.Question       = Question

        # Show the test at the console
    def show_solution_console(self):

        # Create a string to prepare good format
        solutionString = """\nSolution ID      : {}\nQuestion         : {}\n""".format(self.ID,self.Question,)

        # Print the file to the console
        print(solutionString)

        # Return the string to use another way
        return solutionString


    def save_solution_as_txt(self):
        solutionString = self.show_solution_console()
        # If willSaved is true save the Test properties as ID+".txt" file
        solutionFile = open( str(self.ID)+".txt","w") 
        solutionFile.write("--------> SOLUTİON OBJECT <--------\n")
        solutionFile.write(solutionString)
        solutionFile.write("\n\nAll Rights are Reserved @2021 A-MEAN Company")
        solutionFile.close() 



# DRIVER PROGRAM

Math_Test_Solution = Solution(2,["Q1","Q2","Q3"])

Math_Test_Solution.show_solution_console()

Math_Test_Solution.save_solution_as_txt()