from PIL import Image, ImageTk
import tkinter as tk


class ImageFrame:
    """
    Represents a widget for displaying images.

    Attributes
    ----------
    master (tk.Tk): The main Tkinter window.
    blank_photo (PIL.Image): A blank image used as the default display.
    image1 (ImageTk.PhotoImage): The Tkinter-compatible image.
    panel (tk.Label): The label used for displaying the image.

    Methods
    -------
    __init__(): Initializes the ImageFrame.
    """

    def __init__(self, master):
        """
        Initializes the ImageFrame.

        Parameters
        ----------
        master (tk.Tk): The main Tkinter window.
        """
        self.master = master
        self.blank_photo = Image.new(mode="RGBA", size=(700, 600), color="#242424")
        self.image1 = ImageTk.PhotoImage(self.blank_photo)
        self.panel = tk.Label(self.master, image=self.image1)
        self.panel.image = self.image1
        self.panel.grid(column=0, rowspan=15)
