import tkinter as tk
from tkinter import filedialog, Text
from PIL import ImageTk, Image
import os

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
        img = ImageTk.PhotoImage(Image.open(app.name))
        label = tk.Label(frame, image=img)
        label.image = img
        label.pack()

        print(img)


def clearImage():
    apps = []
    for label in frame.winfo_children():
        label.destroy()


canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(
    root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp
)

openFile.pack()
clearQuery = tk.Button(
    root, text="Clear", padx=10, pady=5, fg="white", bg="#263D42", command=clearImage
)
clearQuery.pack()

root.mainloop()
