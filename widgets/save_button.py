import tkinter as tk
from tkinter import filedialog
import os


class SaveButton:
    """
    Represents a widget for saving watermarked images.

    Attributes
    ----------
    watermark (Watermark): The watermark widget associated with the image to be saved.
    save_button (tk.Button): The button for triggering the image saving process.

    Methods
    -------
    __init__(): Initializes the SaveButton.

    save_image(): Saves the watermarked image based on user input.
    """

    def __init__(self, watermark):
        """
        Initializes the SaveButton.

        Parameters
        ----------
        watermark (Watermark): The watermark widget associated with the image to be saved.
        """
        self.watermark = watermark

        self.save_button = tk.Button(
            text="Save", bg="#e7e7e7", fg="black", command=self.save_image
        )
        self.save_button.grid(column=7, row=16)

    def save_image(self):
        """
        Saves the watermarked image based on user input.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
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
