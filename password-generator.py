import random
import string
def gen_password():
    #Initializing variables with a random value
    length = choice1 = choice2 =-1
    print("Specify length of password:\n1= Short(8-12 characters)")
    print("2=Medium(13-19 characters)\n3=Long(20-30 characters)")
    while choice1<0 or choice1>3:
        choice1 = int(input("Your choice?  "))
        if choice1 == 1:
            length = random.randint(8,12)
        elif choice1 == 2:
            length = random.randint(13,19)
        elif choice1 == 3:
            length = random.randint(20,30)
        else:
            print("Wrong Input. Enter again!")
    print("Specify the complexity of the password:")
    print("1 = Simple\n2=Mediocre\n3=Very Strong")
    while choice2<0 or choice2>3:
        choice2 = int(input("Your choice?  "))
        if choice2 == 1:
            #Password is only Alphanumeric
            characters=list(string.digits+string.ascii_letters)
        elif choice2 == 2:
            #Password contains special characters as well but,
            #Letters and digits are more probable
            characters = list("!@#$%^&*()?" + 2*string.digits + 2*string.ascii_letters)
        elif choice2 == 3:
            #Special characters will appear more often
            characters = list("!@#$%^&*()?" + string.digits + string.ascii_letters)
        else:
            print("Wrong Input. Enter again!")
    output_pass = []
    for i in range(length):
        output_pass.append(random.choice(characters))
    random.shuffle(output_pass)
    print("\nHere is a password suggestion:")
    print("".join(output_pass),"\n")
gen_password() 