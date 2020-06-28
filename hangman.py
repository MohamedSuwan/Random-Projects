# here im gonna draw the hanged man character
c="""
          |
          |
        __|__
       [|X X|]
        |___|
          |
         /|\\
        / | \\
       *  |  *
          |
         / \\
        /   \\
       *     *
"""
word="hehehehe"
wdic={i:word.__getitem__(i) for i in range (len(word))}
wdisplay={i:"*" for i in range (len(word))}
guesses=[]
#word=[word[x] for x in range (len(word))]
inc=4
for i in range(8):
  guess=str(input("enter your guess "))

  if guess not in wdic.values():
    k=c.split("\n")
    guesses.append(guess)
    print("you tried: ",guesses)
    #print([f"{k[x]}" for x in range (5)])
    print("\n".join(k[0:inc]))
    inc+=4
  else:
    for x in wdic.keys(): 
      if wdic[x]==guess:
        wdisplay[x]=wdic[x] 
    print("".join(wdisplay.values()))
    print("you tried: ",guesses)
