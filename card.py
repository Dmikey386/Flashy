from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
# -------------------------- Words  -------------------------- # 

class Card(Canvas): 
    def __init__(self,word_es=None,word_en=None):
        super().__init__()
        self.front = PhotoImage(file='./images/card_front.png')
        self.back = PhotoImage(file='./images/card_back.png')
        self.word_es = word_es
        self.word_en = word_en
        self.lang = "Spanish"

        
    
    def display_card(self,word=None,side=None): 
        """ display the card information"""
        # Set default values inside the method
        if word == None:
            word = self.word_es
        if side == None: 
            side = self.front
        
        self.delete('all')
        self.config(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
        self.create_image(400,263,image=side)
        self.create_text(400,150,text=self.lang,fill='black',font=("Arial",40,"italic"))
        self.create_text(400,263,text=word,fill='black',font=("Arial",60,"bold"))
        self.grid(row=0,column=0,columnspan=3)

    def flip(self):
        """ flip the card from english or spanish side"""
        if self.lang  == "Spanish": 
            self.lang = "English"
            self.display_card(self.word_en,self.back)
            
        else: 
            self.lang = "Spanish"
            self.display_card(self.word_es,self.front)

        
        
            

