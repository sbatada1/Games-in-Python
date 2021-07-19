from tkinter import *


def happy():
    c = Canvas(width=500,height=500,bg = 'white')
    c.create_oval(30,40,450,450,fill='yellow')
    c.grid(row=1,column=1)

    c.create_oval(100,100,160,200,fill='black') #HAPPY-EYES
    c.create_oval(300,100,360,200,fill='black') #HAPPY-EYES

    c.create_oval(130,120,150,150,fill='white') #HAPPY-EYES
    c.create_oval(330,120,350,150,fill='white') #HAPPY-EYES

    
    c.create_arc(100,150,360,400,start=0,extent=-180,fill='red')  #HAPPY-SMILE

def sad():
    c = Canvas(width=500,height=500,bg = 'white')
    c.create_oval(30,40,450,450,fill='yellow')
    c.grid(row=1,column=1)

    c.create_arc(100,200,160,100,start=210,extent=120,fill='black')  #SAD-EYES
    c.create_arc(300,200,360,100,start=210,extent=120,fill='black')  #SAD-EYES

    c.create_arc(100,370,360,300,start=0,extent=180,fill='red')   #SAD-SMILE

def upset():
    c = Canvas(width=500,height=500,bg = 'white')
    c.create_oval(30,40,450,450,fill='yellow')
    c.grid(row=1,column=1)

    c.create_oval(100,100,160,200,fill='black') #HAPPY-EYES
    c.create_oval(300,100,360,200,fill='black') #HAPPY-EYES

    c.create_oval(130,120,150,150,fill='white') #HAPPY-EYES
    c.create_oval(330,120,350,150,fill='white') #HAPPY-EYES
    
    c.create_polygon(370,300,120,270,100,320)

def laugh():
    c = Canvas(width=500,height=500,bg = 'white')
    c.create_oval(30,40,450,450,fill='yellow')
    c.grid(row=1,column=1)

    c.create_oval(100,100,160,200,fill='black') #HAPPY-EYES
    c.create_oval(300,100,360,200,fill='black') #HAPPY-EYES

    c.create_oval(130,120,150,150,fill='white') #HAPPY-EYES
    c.create_oval(330,120,350,150,fill='white') #HAPPY-EYES

    c.create_polygon(100,250,360,250,360,280,100,280,fill='white')
    #c.create_polygon(50,300,350,300,350,120,50,120,fill='white')
    c.create_arc(100,150,360,400,start=0,extent=-180,fill='red')  #HAPPY-SMILE

    
    
    
    
root = Tk()
root.config(bg='white')
c = Canvas(width=500,height=500,bg = 'white')
c.create_oval(30,40,450,450,fill='yellow')
c.grid(row=1,column=1)

c.create_oval(100,100,160,200,fill='black') #HAPPY-EYES
c.create_oval(300,100,360,200,fill='black') #HAPPY-EYES

c.create_oval(130,120,150,150,fill='white') #HAPPY-EYES
c.create_oval(330,120,350,150,fill='white') #HAPPY-EYES


#c.create_arc(100,150,360,400,start=0,extent=-180,fill='red')  #HAPPY-SMILE
#c.create_line(110,190,90,230)
#c.create_line(110,190,120,230)

#c.create_line(350,190,370,220)
#c.create_line()
#c.create_arc()

#c.create_polygon(60,150,120,130,140,80,90,80) #ANGRY-EYEBROW




Button(root,text='HAPPY',bg='red',fg='blue',width=10,height=5,command=lambda:happy()).grid(row=0, column=0)
Button(root,text='SAD',bg='red',fg='blue',width=10,height=5,command=lambda:sad()).grid(row=0, column=3)
Button(root,text='UPSET',bg='red',fg='blue',width=10,height=5,command=lambda:upset()).grid(row=3, column=0)
Button(root,text='LAUGH',bg='red',fg='blue',width=10,height=5,command=lambda:laugh()).grid(row=3, column=3)



 

mainloop()
