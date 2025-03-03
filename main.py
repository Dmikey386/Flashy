from tkinter import *
from tkinter import messagebox
from card import Card
import pandas as pd
import os
import random 


BACKGROUND_COLOR = "#B1DDC6"
current_index = None
try: 
    study_df = pd.read_csv('to_study.csv')
except FileNotFoundError: 
    study_df = pd.read_csv('example_translated.csv')
    study_df.to_csv('to_study.csv',index=False)
# -------------------------- RIGHT delete FUNCTIONS -------------------------- # 
def keep_card(): 
    next_card()

def delete_card():
    global study_df

    #update csv
    try:
        study_df.drop(index=current_index,inplace=True)
        next_card()
    except ValueError:
        remake = messagebox.askyesno("Alert","Your deck is empty \n Do you want to reset with default wordset")
        if remake == True:
            study_df = pd.read_csv('example_translated.csv')
            study_df.to_csv('to_study.csv',index=False)
        else: 
            card.display_card("")
            os.remove('to_study.csv')
    else:
        study_df.reset_index(drop=True,inplace=True)
        study_df.to_csv('to_study.csv',index=False)


def next_card(): 
    global current_index
    current_index = random.randint(0,len(study_df)-1)
    es = study_df.iloc[current_index][0]
    en = study_df.iloc[current_index][1]

    card.word_es = es
    card.word_en = en
    card.display_card()


# -------------------------- UI -------------------------- # 
root = Tk() 
root.title("Flashy")
root.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

# CARD - Canvas
card = Card()
next_card()

# BUTTONS
flip = Button(text="FLIP",font=('Arial',30),highlightthickness=0,bd=0,command=card.flip)
flip.grid(row=1,column=1)


keep = Button(text="KEEP CARD",font=('Arial',30),highlightthickness=0,bd=0,command=keep_card)
keep.grid(row=1, column=0)

delete = Button(text="DELETE CARD",font=('Arial',30),highlightthickness=0,bd=0,command=delete_card)
delete.grid(row=1,column=2)

root.mainloop()



            

