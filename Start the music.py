import pyautogui as gu

# search for the player's icon and click it.
gu.click(gu.locateOnScreen("/home/roy/Pictures/playericon.png"),duration=(.2))
# gu.click(165,750,duration =0.2)# icon coordinations

# untill the music player boots.
gu.sleep(1.1)

# click the icon it sees whether it's play or pause.
if gu.locateOnScreen("/home/roy/Pictures/play.png"):
    gu.click(gu.locateOnScreen("/home/roy/Pictures/play.png"))
else:
    gu.click(gu.locateOnScreen("/home/roy/Pictures/pause.png"),duration=(.2))
    
# minimize the player's window.    
gu.click(gu.locateOnScreen("/home/roy/Pictures/mini.png"),duration=(.2))


