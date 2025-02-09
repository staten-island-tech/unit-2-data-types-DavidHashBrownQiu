""""def login(password):
    #if statements evaluate that this is true
    if password == "secret":
        print("logged in")
    else:
        print("incorrect")
x = input("what da passworrd")
login(x)"""

def grade(score):
    if score >=92:
        print("A")
    elif score >= 82:
        print("B")
    elif score >= 72:
        print("C")
    else:
        print("F")
x = int(input("what's your score"))
grade(x)

#we must use an integer for this case

def gamble(age,id):

    if age >=21:
        if id:
            print("Legal")
        else:
            print("GET AN ID")
    else:
        print("Go gamble")

x = int(input("what's your age"))
y = input("do you have an id")
gamble(x,y)