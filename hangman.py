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
guess="p"
word="wioord"
wdic={i:word.__getitem__(i) for i in range (len(word))}
wdisplay={i:"*" for i in range (len(word))}

#word=[word[x] for x in range (len(word))]
if guess not in wdic.values():
  k=c.split("\n")
  print([k[x] for x in range (5)])
else:
  for x in wdic.keys(): 
    if wdic[x]==guess:
      wdisplay[x]=wdic[x] 
  print("".join(wdisplay.values()))