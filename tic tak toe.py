from tkinter import *

def callback(r,c):
    global player
    if player == 'X' and  state[r][c] == 0 and stop_game == False:
        b[r][c].configure(text="X",fg='red',bg='yellow')
        state[r][c]='X'
        player = 'O'

    if player == 'O' and  state[r][c] == 0 and stop_game == False:
        b[r][c].configure(text="O",fg='red',bg='yellow')
        state[r][c]='O'
        player = 'X'
        
    winner()

def winner():
    global stop_game
    for i in range(3):  
        if state[0][i]==state[1][i]==state[2][i]!=0:
            b[0][i].configure(bg='grey')
            b[1][i].configure(bg='grey')
            b[2][i].configure(bg='grey')
            stop_game=True

    for i in range(3):
        if state[i][0]==state[i][1]==state[i][2]!=0:
            b[i][0].configure(bg='grey')
            b[i][1].configure(bg='grey')
            b[i][2].configure(bg='grey')
            stop_game=True

    if state[0][0]==state[1][1]==state[2][2]!=0:
        b[0][0].configure(bg='grey')
        b[1][1].configure(bg='grey')
        b[2][2].configure(bg='grey')
        stop_game=True

    if state[0][2]==state[1][1]==state[2][0]!=0:
        b[0][2].configure(bg='grey')
        b[1][1].configure(bg='grey')
        b[2][0].configure(bg='grey')
        stop_game=True
root = Tk()
f=Frame()

f.grid(row=6,column=6)
player = 'X'
stop_game = False
labelfont= ('times',20,'bold')
#a=tkFont.Font(family='Helvetica', size= 40,weight=tkFont.BOLD)

b = [[0,0,0],
     [0,0,0],
     [0,0,0]]

state = [[0,0,0],
         [0,0,0],
         [0,0,0]]


for i in range(3):
    for j in range(3):
        b[i][j]=Button(f,width=20,height=6,command=lambda r=i,c=j:callback(r,c))
        b[i][j].configure(bg='yellow')
        b[i][j].grid(row=i,column=j,ipadx=10,ipady=10,sticky="NSEW")

#for i range(3):
    
        
mainloop()
