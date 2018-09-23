import math

def splitCheck(total,noOfPeople):

    return  math.ceil(total // noOfPeople)

try:
    bill = float(input("Enter billing ammount: "))
    pson = int(input("Enter no. of person: "))
    sSon = input("hello")

except ValueError:
    print("Lol,that not a valid value ")
else:
    pPCounter = splitCheck(bill, pson)
    print("Price per person {}$ ".format(pPCounter))




