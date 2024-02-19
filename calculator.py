def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2
while True:

    print("##############")
    print('calculator')
    print("##############")
    print("1: Add")
    print("2: Substract")
    print("3: Multiplication")
    print("4: Division")
    print("5: Quit")

    option = input("select your operation: 1,2,3,4,5: ")

    if option == '5':
        print("exiting program..!")
        break
    if option in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if option == '1':
            print("Result: ", add(num1,num2))
        elif option == '2':
            print("Result: ", sub(num1,num2))
        elif option == '3':
            print("Result: ",mul(num1,num2))
        elif option == '4':
            print("Result: ", div(num1,num2))
    else:
        print("invalid option selected")
