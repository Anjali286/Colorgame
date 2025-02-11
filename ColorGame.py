import tkinter
import random
from tkinter import messagebox

colors=["Black","Red","White","Blue","Green","Yellow","Pink","Brown","Orange","Purple"]

score=0
timeleft=15

def game(event):
   if timeleft==15:
      countdown()
      
   nxtcolor()



def nxtcolor():
   global score
   global timeleft

   if timeleft >0:
      e.focus_set()
      if e.get().lower()==colors[1].lower():
         score+=1

      e.delete(0,tkinter.END)
      random.shuffle(colors)

      label.config(fg=str(colors[1]), text=str(colors[0]))
      scoreLabel.config(text="Score:" +str(score))

def countdown():
   global timeleft
   '''if timeleft==0:
      messagebox.showinfo("Time Left","Time is over & Your score is",str(score))'''
      
   if timeleft>0:
      timeleft-=1
      timeLabel.config(text="Time Left : "+str(timeleft))
      timeLabel.after(1000,countdown)
      
# creating GUI window

root=tkinter.Tk()
root.title("**COLOR GAME**")
root.geometry("300x200")
#root.resizable(0,0)

#instructions
instructions=tkinter.Label(root,text="Type the color of word,Not the text!!",
                          font=("Helvetica",12))
instructions.pack()
#score
scoreLabel=tkinter.Label(root,text="Press Enter key to Start",
                         font=("Helvetica",12))
scoreLabel.pack()
#timeleft
timeLabel=tkinter.Label(root,text="Time Left : "+str(timeleft),
                        font=('Helvetica',12))
timeLabel.pack()
#display color
label=tkinter.Label(root,font=("Helvetica",60))
label.pack()


e=tkinter.Entry(root)
root.bind('<Return>',game)
e.pack()

e.focus_set()
  

root.mainloop()

if timeleft==0:
   #root=tkinter.Tk()
   #root.geometry("100x100")
   messagebox.showinfo("Timeleft","Time is over")
   #root.mainloop()


print("hello")
print("This is a colorgame")
















   
