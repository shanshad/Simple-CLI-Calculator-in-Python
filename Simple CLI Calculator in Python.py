def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b
def power(a,b):
    return a**b
def mod(a,b):
    return a%b

n1=int(input("Enter first number : "))
choice='y'
while choice=='y' or choice=='n':
    
    op=input("+\n-\n*\n/\n%\n^\nChoose an operation : ")
    opl=['+','-','*','%','/','^']
    if op not in opl:
        print("Invalid input :")
        exit()
    n2=int(input("Enter second Number : "))

    if op=='+':
        result=add(n1,n2)
        print(f"{n1} + {n2} = {result}")
    elif op=='-':
        result=sub(n1,n2)
        print(f"{n1} - {n2} = {result}")
    elif op=='*':
        result=mult(n1,n2)
        print(f"{n1} * {n2} = {result}")
    elif op=='/' and n2 == 0:
        print("Error: Division by zero is not allowed.")
        continue
    elif op=='/':
        result=div(n1,n2)
        print(f"{n1} / {n2} = {result}")
    elif op=='^':
        result=power(n1,n2)
        print(f"{n1} ^ {n2} = {result}")
    elif op=='%':
        result=mod(n1,n2)
        print(f"{n1} % {n2} = {result}")
    choice=input(f"press \'y\' to continue calculation with {result} or \'n\' to start new calculations or \'x\' to exit : ").lower() 
    
    if choice=='y':
        n1=result
    elif choice=='n':
        n1=int(input("Enter first number : "))
    elif choice=='x':
        exit()
    else:
        print("enter valid input : ")
        exit()
    
    
    
    
    