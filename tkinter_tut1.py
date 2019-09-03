from tkinter import *
from PIL import Image, ImageTk
root = Tk()

# Width x Height
# root.geometry("800x300")
# root.minsize(80, 30)
# root.maxsize(800, 300)
# m = Label(text = "Kashif Hassan")
# p = PhotoImage(file = "kashif.jpg")

i = Image.open("kashif.jpg")
p = ImageTk.PhotoImage(i)
k = Label(image = p)

k.pack()
root.mainloop()
