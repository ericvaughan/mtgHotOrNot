import tkinter
from PIL import Image, ImageTk
from typing import List

def card_select_window(cards: List[str]) -> int:
    root=tkinter.Tk()
    image_o = Image.open("images/BlackLotus.png").resize((189, 264), Image.ANTIALIAS)
    card_img1 = ImageTk.PhotoImage(image_o)
    
    image_o = Image.open("images/GoblinChainwhirler.png").resize((189, 264), Image.ANTIALIAS)
    card_img2 = ImageTk.PhotoImage(image_o)
    b1=tkinter.Button(root, image=card_img1)
    b1.pack()
    b2=tkinter.Button(root, image=card_img2)
    b2.pack()
    root.mainloop()

class CardSelect:

    def __init__(self, cards: List[str]):
        self.frame = tkinter.Tk()
        #self.frame.grid()
        self.button_list = []
        self.card_imgs = []
        # Button should return identity upon being pressed. To indicate which card was selected
        i = 0
        for card in cards:
            image_o = Image.open(card).resize((189, 264), Image.ANTIALIAS)
            self.card_imgs.append(ImageTk.PhotoImage(image_o))
            self.button_list.append(
                tkinter.Button(
                    master=self.frame,
                    image=self.card_imgs[i],
                    command = lambda i=i: self.buttonClick(i),
                )
            )
            self.button_list[-1].pack()
            i = i+1
    
    def buttonClick(self, btn_id: int):
        """ handle button click event and output text from entry area"""
        import pdb;pdb.set_trace()
        pass
    
    def begin(self):
        self.frame.mainloop()


if __name__ == "__main__":
    cards = ["images/BlackLotus.png", "images/GoblinChainwhirler.png"]
    if True:
        guiFrame = CardSelect(cards)
        guiFrame.begin()
