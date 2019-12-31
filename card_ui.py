import tkinter
from PIL import Image, ImageTk
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
