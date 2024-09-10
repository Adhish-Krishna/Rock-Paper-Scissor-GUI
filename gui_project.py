#Importing Tkinter For GUI
#Importing random for random computer's choice

from tkinter import *

from tkinter.font import Font

import random

root=Tk()

playerchoice=""
computerchoice=""
playerscore=0
computerscore=0

root.title("Rock Paper Scissor")

root.resizable(0,0)

root.geometry("800x400")

root.config(bg='#172143')

main_font=Font(size=15)

#Importing main png

rps_img=PhotoImage(file="rps.png")
small_rps_img=rps_img.subsample(5,5)

#Creating icon for the application
root.iconphoto(True,small_rps_img)

main_label=Label(root,image=small_rps_img,bg='#172143').pack()

label_1=Label(root,text="Player's Choice:",font=main_font,bg='#172143',fg='White').place(x=10,y=250)

#Methods for processing the data

#Random Choice for computer

def random_computer_choice():
    return random.choice(["Rock","Paper","Scissor"])

#Creating AI
def process(playerchoice,computerchoice):

    global playerscore
    global computerscore

    if computerchoice=="Rock":
       lbl_1=Label(root,image=small_rock_img,bg='#fff91e').place(x=700,y=100)   
       if playerchoice=="Rock":
           lbl_2=Label(root,image=small_rock_img,bg='#fff91e').place(x=50,y=100)
           pass
       elif playerchoice=="Paper":
           lbl_2=Label(root,image=small_paper_img,bg='#fff91e').place(x=50,y=100) 
           playerscore+=1
       elif playerchoice=="Scissor":
           lbl_2=Label(root,image=small_scissor_img,bg='#fff91e').place(x=50,y=100)
           computerscore+=1

    if computerchoice=="Paper":
       lbl_1=Label(root,image=small_paper_img,bg='#fff91e').place(x=700,y=100)
       if playerchoice=="Paper":
           lbl_2=Label(root,image=small_paper_img,bg='#fff91e').place(x=50,y=100)
           pass
       elif playerchoice=="Rock":
          lbl_2=Label(root,image=small_rock_img,bg='#fff91e').place(x=50,y=100)
          computerscore+=1
       elif playerchoice=="Scissor":
          lbl_2=Label(root,image=small_scissor_img,bg='#fff91e').place(x=50,y=100)
          playerscore+=1

    if computerchoice=="Scissor":
       lbl_1=Label(root,image=small_scissor_img,bg='#fff91e').place(x=700,y=100) 
       if playerchoice=="Scissor":
           lbl_2=Label(root,image=small_scissor_img,bg='#fff91e').place(x=50,y=100)
           pass
       elif playerchoice=="Rock":
          lbl_2=Label(root,image=small_rock_img,bg='#fff91e').place(x=50,y=100)
          playerscore+=1
       elif playerchoice=="Paper":
          lbl_2=Label(root,image=small_paper_img,bg='#fff91e').place(x=50,y=100)
          computerscore+=1

    text_inside_box="Player Choice:{} \t Computer Choice:{} \n Player Score:{} \t Computer Score:{}".format(playerchoice,computerchoice,playerscore,computerscore)
    text_box=Label(root,text=text_inside_box,bg='#31a3ff',font=main_font,fg='Black').place(x=150,y=120)
        
#Getting input from the buttons
   
def Rock():
    playerchoice="Rock"
    computerchoice=random_computer_choice()
    process(playerchoice,computerchoice)

def Paper():
    playerchoice="Paper"
    computerchoice=random_computer_choice()
    process(playerchoice,computerchoice)

def Scissor():
    playerchoice="Scissor"
    computerchoice=random_computer_choice()
    process(playerchoice,computerchoice)

#Importing images
rock_img=PhotoImage(file="rps rock1.png")
small_rock_img=rock_img.subsample(4,4)

paper_img=PhotoImage(file="rps paper.png")
small_paper_img=paper_img.subsample(5,5)

scissor_img=PhotoImage(file="rps scissor2.png")
small_scissor_img=scissor_img.subsample(4,5)

#Creating Buttons

Rock_button=Button(root,image=small_rock_img,font=main_font,padx=10,pady=20,bg='#31a3ff',fg='White',command=Rock).place(x=50,y=300)

Paper_button=Button(root,image=small_paper_img,font=main_font,padx=10,pady=20,bg='#31a3ff',fg='White',command=Paper).place(x=350,y=300)

Scissor_button=Button(root,image=small_scissor_img,font=main_font,padx=10,pady=20,bg='#31a3ff',fg='White',command=Scissor).place(x=700,y=300)

root.mainloop()