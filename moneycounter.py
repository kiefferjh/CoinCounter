# Haven't coded in weeks, here we go!

#Money Counting Program

import re

# Pennies, Nickels, Dimes, Quarters, Dollars etc.

# An amount will be entered for example: $15.36
#and a result should come out....say
#One ten dollar bill, one five, one quarter, one dime and one penny.
#Biggest bills get pref

#It's BEEN SO LONG, this would have been really easy but oh well....
#It's all about problem solving.
#First I want to find a way to represent the number internally,
#So I'm going to turn a string into an integer and get rid of the decimal perhaps...

enteredAmount = input("Please enter the amount of money: \n")
#Entered Amount will look like $15.36, hopefully without the $ sign.

#print(enteredAmount)

# Looks like we've got a problem with the period symbol.
#That's why we have libraries folks.

#but can I remember how to use them...
cleanedEnteredAmount = re.sub('[^\w\s]','',enteredAmount) #I'm a terrible coder
cleanedEnteredAmount = int(cleanedEnteredAmount)
print(cleanedEnteredAmount)
print(type(cleanedEnteredAmount))

# We could have kept the period...but for now we shall not.
#Now it looks like math time... UGH

#more zeroes because no decimal place
hundred = 10000
fifty = 5000
twenty = 2000
ten = 1000
five = 500
one = 100
quarter = 25
dime = 10
nickel = 5
penny = 1


#here's a function
def checkFor(unit, leftOver):
    unit = int(unit)
    leftOver = int(leftOver)
    #Where left over is the amount of money left to look through and unit is the kind of money we are searching for
    #left over will be cleanedEnteredAmount the first time

    #We need to know how many times the unit can evenly go in to the lefOver
    #Looks like regular division is fine
    try:
        howManyWentIn = leftOver // unit
    except:
        print("An Exception Occccccured baby")
    #print("How MANY WENT IN: \n")
    print(howManyWentIn) #Should print what it is
    # print("UNIT: \n")
    # print(unit)
    if unit == 10000:
        print("Hundred(s)")
    elif unit == 5000:
        print("Fifty / Fifties")
    elif unit == 2000:
        print("Twenties")
    elif unit == 1000:
        print("Tens")
    elif unit == 500:
        print("Fives")
    elif unit == 100:
        print("Ones")
    elif unit == 25:
        print("Quarters")
    elif unit == 10:
        print("Dimes")
    elif unit == 5:
        print("Nickels")
    elif unit == 1:
        print("Pennies")

    #here I'm saying the newLeftOver shall be the previous minus the amount already counted
    newLeftOver = leftOver - (unit * howManyWentIn)
    return newLeftOver

afterHun = checkFor(hundred, cleanedEnteredAmount)
afterFif = checkFor(fifty, afterHun)
afterTwen = checkFor(twenty, afterFif)
afterTen = checkFor(ten, afterTwen)
afterFive = checkFor(five, afterTen)
afterOne = checkFor(one, afterFive)
afterQuarter = checkFor(quarter, afterOne)
afterDime = checkFor(dime, afterQuarter)
afterNickel = checkFor(nickel, afterDime)
afterPenny = checkFor(penny, afterNickel)
