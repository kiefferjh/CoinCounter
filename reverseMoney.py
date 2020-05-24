# Reverse Money Counter
# Hopefully very easy

# Apparently this is what Natalie actually wanted me to build...and it took 5 min literally

def questions():
    fifties = input("Gimme yer fifties")
    twenties = input("Twenties...")
    tens = input("How many tens you got")
    fives = input("How many fives you got fool")
    ones = input("How many ones you got bitch")
    quarters = input("How many quarters you got bitch")
    dimes = input("How many dimes")
    nickels = input("How many nickelback")
    pennies = input("How many pennies?")

    newTotal = 0

    fifties = int(fifties)
    twenties = int(twenties)
    tens = int(tens)
    fives = int(fives)
    ones = int(ones)
    quarters = int(quarters)
    dimes = int(dimes)
    nickels = int(nickels)
    pennies = int(pennies)

    newTotal = newTotal + pennies
    newTotal = newTotal + (nickels * 5)
    newTotal = newTotal + (dimes * 10)
    newTotal = newTotal + (quarters * 25)
    newTotal = newTotal + (ones * 100)
    newTotal = newTotal + (fives * 500)
    newTotal = newTotal + (tens * 1000)
    newTotal = newTotal + (twenties * 2000)
    newTotal = newTotal + (fifties * 5000)


    newTotal = newTotal / 100

    return newTotal





total = 0

total = questions()

print (total)
