def calculator():
    print("Allowed operators: +,-,*,/,**,//,%")
    #Take inputs from user
    x= float(input("First Number: "))
    choice = input("Operator:  ")
    y= float(input("Second Number: "))
    #Perform operation based on the choices
    if choice == "+":
        ans = x+y
    elif choice == "-":
        ans = x-y
    elif choice == "*":
        ans = x*y
    elif choice == "/":
        ans = x/y
    elif choice == "**":
        ans = x**y
    elif choice == "//":
        ans = x//y
    elif choice == "%":
        ans = x%y
    print (x,choice,y,"=",ans)
    my_choice = int(input("Continue?(Yes=1, No=0)\n"))
    while my_choice !=0:
        calculator()
calculator()
