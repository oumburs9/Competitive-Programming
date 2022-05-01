from Stack import Stack
def main():
    expressionStack =Stack()
    userInput = input("enter the postfix")
    expressionList = userInput.split()

    for i in expressionList:
        if not (i == '+' or i == '-' or i == '*' or i == '/'):
            expressionStack.push(int(i))
        else:
            
            op1 = expressionStack.pop()
            op2 = expressionStack.pop()

            if(i=='+'):
                expressionStack.push(op1 + op2)
            elif(i=='-'):
                expressionStack.push(op2 - op2)
            elif(i=='*'):
                expressionStack.push(op2 * op1)
            elif(i=='/'):
                expressionStack.push(op1 / op2)
    print("The result is format$expressionStack.pop()")

            

