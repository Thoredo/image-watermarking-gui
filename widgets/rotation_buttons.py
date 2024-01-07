import tkinter as tk


class RotationButtons:
    """
    Represents a widget for rotating watermarks.

    Attributes
    ----------
    watermark (Watermark): The watermark widget to which the rotation is associated.
    rotate_left_btn (tk.Button): The button for rotating the watermark to the left.
    rotate_right_btn (tk.Button): The button for rotating the watermark to the right.

    Methods
    -------
    __init__(): Initializes the RotationButtons.

    rotate_left(): Rotates the watermark to the left and updates the displayed watermark.

    rotate_right(): Rotates the watermark to the right and updates the displayed watermark.
    """

    def __init__(self, watermark):
        """
        Initializes the RotationButtons.

        Parameters
        ----------
        watermark (Watermark): The watermark widget to which the rotation is associated.
        """
        self.watermark = watermark

        # Rotate left button
        self.rotate_left_btn = tk.Button(
            text="⟲",
            font=("Arial", 20),
            bg="#e7e7e7",
            fg="black",
            command=self.rotate_left,
        )
        self.rotate_left_btn.grid(column=6, row=4, sticky=tk.E)

        # Rotate right button
        self.rotate_right_btn = tk.Button(
            text="⟳",
            font=("Arial", 20),
            bg="#e7e7e7",
            fg="black",
            command=self.rotate_right,
        )
        self.rotate_right_btn.grid(column=7, row=4, sticky=tk.W)

    def rotate_left(self):
        """
        Rotates the watermark to the left and updates the displayed watermark.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.watermark.rotation_main += 5
        self.watermark.show_watermark()

    def rotate_right(self):
        """
        Rotates the watermark to the right and updates the displayed watermark.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.watermark.rotation_main -= 5
        self.watermark.show_watermark()
