import math

def splitCheck(total,noOfPeople):

    return  math.ceil(total // noOfPeople)

try:
    bill = float(input("Enter billing ammount: "))
    pson = int(input("Enter no. of person: "))
    sSon = input("Checking the amount of the bill")

except ValueError:
    print("Lol,that not a valid value ")
else:
    pPCounter = splitCheck(bill, pson)
    print("Price per person {}$ ".format(pPCounter))
    print("Hello every one how are you what are you doing  ".format(pPCounter))




