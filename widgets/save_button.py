import tkinter as tk
from tkinter import filedialog
import os


class SaveButton:
    def __init__(self, master, watermark):
        self.master = master
        self.watermark = watermark

        self.save_button = tk.Button(
            text="Save", bg="#e7e7e7", fg="black", command=self.save_image
        )
        self.save_button.grid(column=7, row=16)

    def save_image(self):
        path = filedialog.asksaveasfilename(
            confirmoverwrite=True,
            defaultextension="png",
            filetypes=[
                ("jpeg", ".jpg"),
                ("png", ".png"),
                ("bitmap", "bmp"),
                ("gif", ".gif"),
            ],
        )
        if path and os.path.splitext(path)[1] == ".jpg":
            image = self.watermark.img_main.convert("RGB")
            image.save(path)
            tk.messagebox.showinfo("Success", "Image got watermarked and saved.")
