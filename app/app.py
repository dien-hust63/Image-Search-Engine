import tkinter as tk
from tkinter import BOTTOM, X, filedialog, RIGHT, Y
from turtle import ycor
from PIL import ImageTk, Image
import os

from numpy import size

root = tk.Tk()
apps = []


def addApp():
    filename = filedialog.askopenfile(
        initialdir="/20212/Thị giác máy tính/Image-Search-Engine/queries",
        title="Select File",
        filetypes=(("JPG", "*.jpg"), ("all files", "*.*")),
    )
    apps.append(filename)
    print(filename)
    for app in apps:
        imageOpen = Image.open(app.name)
        img = ImageTk.PhotoImage(imageOpen.resize((400, 300),Image.ANTIALIAS))
        label = tk.Label(queryFrame, image=img,width=400, height=300)
        label.image = img
        label.pack()

        print(img)


def clearImage():
    apps = []
    for label in queryFrame.winfo_children():
        label.destroy()

root.title("Image Search Engine")
canvas = tk.Canvas(root, height=700, width=1400, bg="#263D42")
canvas.pack()
queryFrame = tk.Frame(root, background="bisque")
resultFrame = tk.Frame(root, background="pink")


queryFrame.place(x=0, y=0, anchor="nw", width=500, height=700)
resultFrame.place(x=500, y=0, anchor="nw", width=900, height=700)
labelQuery = tk.Label(queryFrame, text="Query", bg="orange",  font=('Arial', 25)).pack()
labelQuery2 = tk.Label(resultFrame, text="Result", bg="orange",  font=('Arial', 25)).pack()
openFile = tk.Button(
    queryFrame, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp
)

openFile.pack()
clearQuery = tk.Button(
    root, text="Clear", padx=10, pady=5, fg="white", bg="#263D42", command=clearImage
)
clearQuery.pack()
#scroll
h = tk.Scrollbar(queryFrame, orient = 'horizontal')
h.pack(side = BOTTOM, fill = X)
v = tk.Scrollbar(queryFrame)
v.pack(side = RIGHT, fill = Y)
h.config(command=queryFrame.xview)
v.config(command=queryFrame.yview)
#end scroll
root.mainloop()
