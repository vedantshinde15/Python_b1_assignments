from assignment_9 import MyMathModule, MyException

try:
    num =float(input("Enter a number: "))
    m = MyMathModule(num)
    
    
    if num == 0:
        raise MyException("Number cannot be zero!")
 
    print("Enter Choice")
    opr=input("1.Square 2.Square root 3.Factorial 4.Logarithm 5.Round off ")

    if opr=="1":
        print("Square:", m.square())

    elif opr=="2":
        print("Square Root:", m.square_root())

    elif opr=="3":
        print("Factorial:", m.factorial())
    
    elif opr=="4":
        print("Logarithm:", m.logarithm())  

    elif opr=="5":
        print("Round off:",m.ceil())                    

    else:
        print("Invalid Input")    
    
       
except MyException as e:
    print("Exception:", e.msg())
