import random
import string
import winsound
import pprint

def beep():
    winsound.Beep(1000,100)
    
def intpass():
    intsize=int(input("Enter the size of the password : "))
    ranum=[random.randint(0,9) for i in range(intsize)]
    ranum="".join([str(ranum[i]) for i in range(len(ranum))])
    beep()
    print(f"the random Password consesting of {intsize} digits is {ranum}")
intpass()

def mixpass():
    intsize=int(input("Enter the size of the password : "))
    ramix=[random.choice(string.ascii_uppercase+ string.digits) for i in range(intsize)]
    ramix="".join([ramix[i] for i in range(len(ramix))])
    beep()
    pprint.pprint(f"the random Password consisting of {intsize} fields is : {ramix} ")
mixpass()

def strpass():
    passize=int(input("enter the size of the password: "))
    pastring=[random.choice(string.ascii_uppercase) for i in range(passize)]
    pastring="".join(pastring)
    beep()
    print(f"the password you requested containing only letters with the size of {passize} is: {pastring}")
strpass()
