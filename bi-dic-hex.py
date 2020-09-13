# binary hexadecimal decimal'""

hexa={
    "0":0,
    "1":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "a":10,
    "b":11,
    "c":12,
    "d":13,
    "e":14,
    "f":15,
}
ind=[]
val=[]
def dec():
    s=str(input("enter the dexa number:"))
    for x,y in enumerate(s):
        ind.insert(0,x)
        val.append(hexa[y])
    for i in s:
        if i not in hexa:
            print("wrong numbers!")
            break
    else:
        print("right")
        
dec()

print(sum(list(map(lambda x,y: (16**x)*y,ind,val)))) # amazing!
dd=(list(map(lambda x: (16**x),ind)))
ff=[x*y for x,y in zip (dd,val)]
print(sum(ff))
# raise key error instead of the loops!