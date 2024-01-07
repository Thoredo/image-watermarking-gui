import tkinter as tk


class ImageSizeLabel:
    """
    Represents a widget for displaying image size.

    Attributes
    ----------
    height_main (int): The main height value.
    width_main (int): The main width value.
    image_size (tk.Label): The label for displaying image size.

    Methods
    -------
    __init__(): Initializes the ImageSizeLabel.

    """

    def __init__(self):
        """
        Initializes the ImageSizeLabel.

        Parameters
        ----------
        None
        """
        self.height_main = 0
        self.width_main = 0
        self.image_size = tk.Label(
            text=f"Image size {self.height_main}/{self.width_main} (height/width)",
            bg="#000000",
            fg="#fafafa",
            font=("Arial", 8),
        )
        self.image_size.grid(column=0, row=16, pady=10)
