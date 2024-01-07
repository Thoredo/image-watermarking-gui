import tkinter as tk


class DirectionalArrows:
    """
    Represents directional arrows for adjusting the watermark position.

    Attributes
    ----------
    select_file (SelectFile): The widget for selecting image files.
    size_label (ImageSizeLabel): The widget for displaying image size.
    watermark (Watermark): The widget for adding watermarks to images.
    up_btn (tk.Button): The button for moving the watermark up.
    down_btn (tk.Button): The button for moving the watermark down.
    left_btn (tk.Button): The button for moving the watermark left.
    right_btn (tk.Button): The button for moving the watermark right.

    Methods
    -------
    __init__(): Initializes the DirectionalArrows.
    up(): Moves the watermark up and updates the displayed watermark.
    down(): Moves the watermark down and updates the displayed watermark.
    left(): Moves the watermark left and updates the displayed watermark.
    right(): Moves the watermark right and updates the displayed watermark.
    """

    def __init__(self, select_file, size_label, watermark):
        """
        Initializes the DirectionalArrows.

        Parameters
        ----------
        select_file (SelectFile): The widget for selecting image files.
        size_label (ImageSizeLabel): The widget for displaying image size.
        watermark (Watermark): The widget for adding watermarks to images.
        """
        self.select_file = select_file
        self.size_label = size_label
        self.watermark = watermark

        # Up button
        self.up_btn = tk.Button(
            text="⮝", font=("Arial", 20), bg="#e7e7e7", fg="black", command=self.up
        )
        self.up_btn.grid(column=4, row=3, sticky=tk.S)

        # Down button
        self.down_btn = tk.Button(
            text="⮟", font=("Arial", 20), bg="#e7e7e7", fg="black", command=self.down
        )
        self.down_btn.grid(column=4, row=5, sticky=tk.N)

        # Left button
        self.left_btn = tk.Button(
            text="⮜", font=("Arial", 20), bg="#e7e7e7", fg="black", command=self.left
        )
        self.left_btn.grid(column=3, row=4, sticky=tk.E)

        # Right button
        self.right_btn = tk.Button(
            text="⮞", font=("Arial", 20), bg="#e7e7e7", fg="black", command=self.right
        )
        self.right_btn.grid(column=5, row=4, sticky=tk.W)

    def up(self):
        """
        Moves the watermark up and updates the displayed watermark.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        if self.select_file.original_height > 1500:
            self.size_label.height_main -= 50
        else:
            self.size_label.height_main -= 10
        self.watermark.show_watermark()

    def down(self):
        """
        Moves the watermark down and updates the displayed watermark.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        if self.select_file.original_height > 1500:
            self.size_label.height_main += 50
        else:
            self.size_label.height_main += 10
        self.watermark.show_watermark()

    def left(self):
        """
        Moves the watermark left and updates the displayed watermark.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        if self.select_file.original_width > 1500:
            self.size_label.width_main -= 50
        else:
            self.size_label.width_main -= 10
        self.watermark.show_watermark()

    def right(self):
        """
        Moves the watermark right and updates the displayed watermark.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        if self.select_file.original_width > 1500:
            self.size_label.width_main += 50
        else:
            self.size_label.width_main += 10
        self.watermark.show_watermark()
