#factor challenge
"""def s():
    ask = int(input("Pick a number"))
    factors = []

    for i in range(1, ask +1):
        if ask % i == 0:
            factors.append(i)

    print(factors)

s()"""

#gcf
def gcf():
    ask1 = int(input("What's your first number? "))
    ask2 = int(input("What's your second number? "))
    values1 = []
    values2 = []
    values3 = []
    gcf = []

    for i in range(1, ask1 + 1):
        if ask1 % i == 0:
            values1.append(i)

    for i in range(1, ask2 + 1):
        if ask2 % i == 0:
            values2.append(i)

    for i in values1:
        if i in values2:
            values3.append(i)
    
    gcf = max(values3)

    print(f"The greatest commmon factor is: {gcf}")

gcf()
    
    