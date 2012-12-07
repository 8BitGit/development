#python document
from tkinter import *
from tkinter.messagebox import showinfo
import random

#database
players = []

def addplayer(player):
    players.append(player)
    
def showPlayers():
    plist=[]
    for player in players:
        plist += player
        
    popup = Toplevel()
    Label(popup, text='Who\'s Playing').pack(side=LEFT)
    Label(popup, text=players).pack(side=LEFT)
    top.mainloop()
    
    return plist
def pickWinner(playing):
    numOfPlayers = len(players)
    winner = random.randint(1, numOfPlayers)-1
    
    winnerWindow = Toplevel()
    Label(winnerWindow, text=players[winner]).pack(side=TOP)
    top.mainloop()
    
#gui
top = Tk()
top.title('User Lookup')

Label(top, text="Enter a name to add: ").pack(side=TOP)
ent = Entry(top)
ent.pack(side=TOP)
btn = Button(top, text="Compete", command=(lambda: addplayer(ent.get())))
btn.pack(side=RIGHT)
btn2 = Button(top, text="Whos Playing?", command=(lambda: showPlayers()))
btn2.pack(side=RIGHT)
pickwinner = Button(top, text="Pick Winenr", command=(lambda: pickWinner(players)))
pickwinner.pack(side=RIGHT)

top.mainloop()