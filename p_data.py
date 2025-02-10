#integers - whole numbers and floats - decimals
"""x = 3
y = float(3)
print(x,y)"""

#iterations allow us to scroll through the 
#values while printing the variables itself does the entire thing
"""values = [1,2.23,5,7,2,30,15]"""
"""print(values)
for i in values:
    print(i)"""

#prints out values from the variable in terms of their placement. 7 is out of range because we don't have a value in the 7th placement.
"""print(values[7])"""

#strings are individual letters that make up a word.
"""x = "this is a thing"
y = x.split()
z = y[0]
print(y)
print(z)"""
#split is basically what we did for the integer values where it takes one word from the string.

#below is for the challenge of counting the values in a sentence.
"""ask = input("put in a sentence!")

def wordcount(sentence):
    splity = sentence.split()
    return len(splity)

print (wordcount(ask))"""

"""number = int(input("Pick a number! Any number: "))

def odd_even(x):
    if x % 2 == 0:
        print("Even")
    else:
        print("Odd")

odd_even(number)"""

x = "test"
print(f"hello {x}")