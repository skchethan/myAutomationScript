
"""
This module is about creating a class snippet as a reference  
"""

class Myclass:
    #Define the constructor method with two parameters
    def __init__(self,arg1, arg2) -> None:
        #Assign the value of the first parameter to the instance variable
        self.arg1 = arg1
        #Assign the value of the second parameter to the instance variable
        self.arg2 = arg2

    #Define a method to print the values of the instance variables
    def method1_using_constructor_variable(self) -> None:
        #Print the value of the first instance variable
        print(f"{self.arg1} variable1")
        #Print the value of the second instance variable
        print(f"{self.arg2} variable2")


#Define a main function
def main():
    #Create an instance of the Myclass class, passing in two variables
    object_1 = Myclass("input1_var", "input2_var")

    #Call the method1_using_constructor_variable method on the object_1 instance
    object_1.method1_using_constructor_variable()

#Call the main function
if __name__ == '__main__':
    main()