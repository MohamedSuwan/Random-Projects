# piano
import winsound
oneF={
    "a":131,
    "s":134,
    "d":147,
    "f":156,
    "g":165
}

def notesound():
    l=str(input())
    winsound.Beep(oneF[l],750)
    notesound()
notesound()
