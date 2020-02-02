import tkinter
from PIL import Image, ImageTk
from typing import List


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
            # For pack of 15 cards, 3 rows of 5
            self.button_list[-1].grid(column=int(i % 5), row = int(i / 5))
            i = i + 1
    
    def buttonClick(self, btn_id: int):
        # Register vote, update associations and store to DB
        pass
    
    def start(self):
        self.frame.mainloop()


if __name__ == "__main__":
    cards = ["images/BlackLotus.png", "images/GoblinChainwhirler.png"]
    if True:
        guiFrame = CardSelect(cards)
        guiFrame.start()
