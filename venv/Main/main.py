import math

def splitCheck(total,noOfPeople):
    if noOfPeople <=1:
        raise ValueError("More than one person is required")
    return  math.ceil(total // noOfPeople)

try:
    bill = float(input("Enter billing ammount: "))
    pson = int(input("Enter no. of person: "))
    pPCounter = splitCheck(bill, pson)

except ValueError as err:
    print("Lol,that not a valid value ")
    print("({})".format(err))
else:
    print("Price per person {}$ ".format(pPCounter))
    print("Hello every one how are you what are you doing  ".format(pPCounter))




