import sys

cPassWord = input("Enter password : ")
attemptCounter = 3
while cPassWord != "delta":
    if attemptCounter < 1 :
        sys.exit("Lost all 3 attempt")
    input("Wrong!, Enter again {} chances left : ".format(attemptCounter) )
    attemptCounter -= 1
print("Welcome aboard")