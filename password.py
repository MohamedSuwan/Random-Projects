import random
import string
import winsound
import pprint

def intpass():
    #ask the user if he wants to enter any numbers and the program completes" ljust!
    intsize=int(input("Enter the size of the password : "))
    ranum=[random.randint(0,9) for i in range(intsize)]
    ranum="".join([str(ranum[i]) for i in range(len(ranum))])
    winsound.Beep(1000,100)
    print(f"the random Password consesting of {intsize} digits is {ranum}")
intpass()
import winsound


def mixpass():
    #ask the user if he wants to enter any numbers and the program completes" ljust!
    intsize=int(input("Enter the size of the password : "))
    ramix=[random.choice(string.ascii_uppercase+ string.digits) for i in range(intsize)]
    ramix="".join([ramix[i] for i in range(len(ramix))])
    winsound.Beep(1000,100)
    pprint.pprint(f"the random Password consisting of {intsize} fields is : {ramix}")
mixpass()
