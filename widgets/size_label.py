import tkinter as tk


class ImageSizeLabel:
    def __init__(self):
        self.height_main = 0
        self.width_main = 0
        self.image_size = tk.Label(
            text=f"Image size {self.height_main}/{self.width_main} (height/width)",
            bg="#000000",
            fg="#fafafa",
            font=("Arial", 8),
        )
        self.image_size.grid(column=0, row=16, pady=10)
