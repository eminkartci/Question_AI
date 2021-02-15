
"""

Author : Emin Kartci
Date   : 15 Feb 2021
GitHub : eminkartci

"""

# Test Class holds the questions and have a specific Subject

    # ID                -> Integer
    # Question          -> Question Object List 
    # Subject           -> Subject Object
    # QuestionCount     -> Integer

class Test:         

    # Constructor
    def __init__(self,ID,Question,Subject,QuestionCount):

        # Assign properties
        self.ID             = ID
        self.Question       = Question
        self.Subject        = Subject
        self.QuestionCount  = QuestionCount


    # Show the test at the console
    def show_test_console(self):

        # Create a string to prepare good format
        testString = """TEST ID         : {}\nSubject         : {}\nQuestion Count  : {}
        """.format(self.ID,self.Subject,self.QuestionCount)

        # Print the file to the console
        print(testString)

        # Return the string to use another way
        return testString


    def save_test_as_txt(self):
        testString = self.show_test_console()
        # If willSaved is true save the Test properties as ID+".txt" file
        testFile = open( str(self.ID)+".txt","w") 
        testFile.write("--------> TEST OBJECT <--------\n")
        testFile.write(testString)
        testFile.write("\n\nAll Rights are Reserved @2021 A-MEAN Company")
        testFile.close() 

# DRIVER PROGRAM
Math_Test = Test(1,["Q1","Q2","Q3"],"Math",15)

Math_Test.show_test_console()

Math_Test.save_test_as_txt()
