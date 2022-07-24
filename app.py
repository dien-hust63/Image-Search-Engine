from threading import Thread
from imagesearch.colordescriptor import ColorDescriptor
from imagesearch.searcher import Searcher
from ast import Try
from pathlib import Path
from tkinter import filedialog
from PIL import Image, ImageTk
import tkinter as tk
from tkinter.constants import *
from tkinter.scrolledtext import ScrolledText
import cv2 
import os



class App:
    def __init__(self, image_folder_path, image_file_extensions, image_query):
        self.root = tk.Tk()
        self.image_folder_path = image_folder_path
        self.image_file_extensions = image_file_extensions
        self.image_query = image_query
        self.create_widgets()
        self.root.mainloop()
  

    def chooseFile(self):
        filename = filedialog.askopenfile(
        initialdir="/20212/Thị giác máy tính/Image-Search-Engine/queries",
        title="Select File",
        filetypes=(("JPG", "*.jpg"), ("all files", "*.*")),
        )
        self.image_query = ".\\queries\\" + filename.name.split("/")[-1]
        print(self.image_query)
        imageOpen = Image.open(filename.name)
        img = ImageTk.PhotoImage(imageOpen.resize((256, 256),Image.LANCZOS))
        label = tk.Label(self.root, image = img)
        label.image = img
        label.grid(row=2, column = 1) 

    def create_widgets(self):
        self.list_btn = tk.Button(self.root, text='Choose file', command=self.chooseFile)
        self.list_btn.grid(row=0, column=0)
        self.show_btn = tk.Button(self.root, text='Search', command=self.show_images)
        self.show_btn.grid(row=1, column=0)

        self.text = ScrolledText(self.root, wrap=WORD)
        self.text.grid(row=2, column=0, padx=10, pady=10)

        self.text.image_filenames = []
        self.text.images = []

    def show_images(self):
        cd = ColorDescriptor((8, 12, 3))

        query = cv2.imread(self.image_query)
        features = cd.describe(query)
        searcher = Searcher("index.csv")
        results = searcher.search(features)
        self.text.delete('1.0', END)  
        self.text.images.clear()
        for result in results:
            link_image = result[1]
            img = Image.open(result[1]).resize((256, 256), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)

            self.text.insert(INSERT, result[1]+'\n')
            self.text.image_create(INSERT, padx=5, pady=5, image=img)
            self.text.images.append(img)  
            self.text.insert(INSERT, '\n')


image_folder_path = '../queries/'
image_file_extensions = {'.jpg', '.png'}
image_query = ".\queries\image_0006.jpg"
App(image_folder_path, image_file_extensions,image_query)
