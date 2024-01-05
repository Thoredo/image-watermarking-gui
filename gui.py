import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class WatermarkingDesktopApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Watermarking GUI")
        self.master.config(padx=20, pady=20, bg="black")
        self.master.minsize(height=100, width=500)
        self.height_main = 0
        self.width_main = 0

        self.create_main_menu()

    def create_main_menu(self):
        self.blank_photo()
        self.image_size_label()
        self.watermark_text()

    def blank_photo(self):
        self.blank_photo = Image.new(mode="RGBA", size=(700, 600), color="#242424")
        self.image1 = ImageTk.PhotoImage(self.blank_photo)
        self.panel = tk.Label(self.master, image=self.image1)
        self.panel.image = self.image1
        self.panel.grid(column=0, rowspan=15)

    def image_size_label(self):
        self.image_size = tk.Label(
            text=f"Image size {self.height_main}/{self.width_main} (height/width)",
            bg="#000000",
            fg="#fafafa",
            font=("Arial", 8),
        )
        self.image_size.grid(column=0, row=16)

    def watermark_text(self):
        self.watermark = tk.Label(
            text="Watermark:",
            width=15,
            bg="#000000",
            fg="#fafafa",
            font=("Arial", 12, "bold"),
        )
        self.watermark.grid(column=3, row=2, sticky=tk.W)
        self.watermark_entry = tk.Entry(width=50)
        self.watermark_entry.grid(column=4, row=2, columnspan=4)
        self.show_watermark = tk.Button(text="Show", bg="#e7e7e7", fg="black", width=6)
        self.show_watermark.grid(column=8, row=2, padx=(10, 0))
