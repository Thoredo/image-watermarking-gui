import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class SelectFile:
    """
    Represents a widget for selecting image files.

    Attributes
    ----------
    main_file (str): The path of the selected image file.
    original_height (int): The original height of the selected image.
    original_width (int): The original width of the selected image.
    image_frame (ImageFrame): The widget for displaying images.
    size_label (ImageSizeLabel): The widget for displaying image size.
    select_file_button (tk.Button): The button for triggering the file selection dialog.

    Methods
    -------
    __init__(): Initializes the SelectFile.

    file_dialog(): Opens a file dialog for selecting an image file.

    show_selected_image(): Displays the selected image in the ImageFrame and updates the ImageSizeLabel.

    resize_image(img): Resizes the image to fit within the specified dimensions.
    """

    def __init__(self, image_frame, size_label):
        """
        Initializes the SelectFile.

        Parameters
        ----------
        image_frame (ImageFrame): The widget for displaying images.
        size_label (ImageSizeLabel): The widget for displaying image size.
        """
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
        """
        Opens a file dialog for selecting an image file.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
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
        """
        Displays the selected image in the ImageFrame and updates the ImageSizeLabel.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
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
        """
        Resizes the image to fit within the specified dimensions.

        Parameters
        ----------
        img (PIL.Image.Image): The image to be resized.

        Returns
        -------
        ImageTk.PhotoImage: The resized image.
        """
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
