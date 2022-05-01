# ***************************************************************************************
# Name: Felmeta Muktar Id: UGR/3555/12
# Name: Jabir Esmael   Id: UGR/3314/12
# ****************************************************************************************
from Stack import Stack

openSym = ["(", "[", "{"]

closeSym = [")", "]", "}"]


def Brackets_valid():
    userInput = input("Enter  Symbols of ( ) [ ] { } separating by space to check whether valid or not : ")
    expressionList = userInput.split()
    print(expressionList)

    myBrack = Stack()

    for i in expressionList:

        if i in openSym:

            myBrack.push(i)

        elif i in closeSym:
            # size_stack() is imported from Stack
            if myBrack.size_stack() > 0:
                # pee() is imported from Stack
                myValue = myBrack.peek()
                if i == ')' and myValue == "(":
                    # pop() is imported from Stack
                    myBrack.pop()
                elif i == '}' and myValue == "{":
                    # pop() is imported from Stack
                    myBrack.pop()
                elif i == ']' and myValue == "[":
                    # pop() is imported from Stack
                    myBrack.pop()

                else:
                    return print("The symbol do not matched!!!!!!!!")

    return print("The symbol matched!!!!!!!!") if myBrack.size_stack() == 0 else print("The symbol do not "
                                                                                       "matched!!!!!!!!")


if __name__ == '__main__':
    Brackets_valid()
