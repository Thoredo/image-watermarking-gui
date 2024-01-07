import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class SelectFile:
    def __init__(self, master, image_frame, size_label):
        self.master = master
        self.main_file = ""
        self.original_height = 0
        self.original_width = 0
        self.image_frame = image_frame
        self.size_label = size_label

        self.select_file_button = tk.Button(
            text="Select File",
            font=("Arial", 12),
            bg="#e7e7e7",
            fg="black",
            command=self.file_dialog,
        )
        self.select_file_button.grid(column=0, row=17)

    def file_dialog(self):
        self.main_file = filedialog.askopenfilename(
            filetypes=[
                ("JPEG files", "*.jpg;*.jpeg"),
                ("PNG files", "*.png"),
                ("Bitmap files", "*.bmp"),
                ("GIF files", "*.gif"),
            ]
        )
        self.show_selected_image()

    def show_selected_image(self):
        self.img = Image.open(self.main_file)
        width = self.img.size[0]
        height = self.img.size[1]
        self.resized_img = self.resize_image(self.img)
        self.image_frame.panel.configure(image=self.resized_img)
        self.image_frame.panel.image = self.resized_img
        self.size_label.image_size.config(
            text=f"Image size {height}/{width} (height/width)",
            bg="#000000",
            fg="#fafafa",
            font=("Arial", 8),
        )
        self.size_label.height_main = height / 2
        self.size_label.width_main = width / 2
        self.original_height = height
        self.original_width = width

    def resize_image(self, img):
        self.size = img.size
        self.panel_size = (700, 600)
        factor = min(
            float(self.panel_size[1]) / self.size[1],
            float(self.panel_size[0]) / self.size[0],
        )
        width = int(self.size[0] * factor)
        height = int(self.size[1] * factor)
        resized_img = img.resize((width, height), Image.LANCZOS)
        return ImageTk.PhotoImage(resized_img)
