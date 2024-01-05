import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class WatermarkingDesktopApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Watermarking GUI")
        self.master.geometry("600x400")
        self.create_main_menu()

        self.tk_image = None

    def create_main_menu(self):
        self.select_img_label = tk.Label(text="Please select an image to edit")
        self.select_img_label.grid(row=0, column=0, padx=230, pady=(170, 10))

        self.browse_button = tk.Button(text="Browse", command=self.browse_image)
        self.browse_button.grid(row=1, column=0)

    def browse_image(self):
        image = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")]
        )
        self.show_chosen_image(image)

    def show_chosen_image(self, image_path):
        self.select_img_label.grid_remove()
        self.browse_button.grid_remove()

        pil_image = Image.open(image_path)
        self.tk_image = ImageTk.PhotoImage(pil_image)

        canvas = tk.Canvas(self.master, width=600, height=300)
        canvas.grid(row=0, column=0)

        canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)
