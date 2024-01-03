import tkinter as tk
from tkinter import filedialog


class WatermarkingDesktopApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Watermarking GUI")
        self.master.geometry("600x400")
        self.create_main_menu()

    def create_main_menu(self):
        self.select_img_label = tk.Label(text="Please select an image to edit")
        self.select_img_label.grid(row=0, column=0, padx=230, pady=(170, 10))

        self.browse_button = tk.Button(text="Browse", command=self.browse_image)
        self.browse_button.grid(row=1, column=0)

    def browse_image(self):
        image = filedialog.askopenfile()
