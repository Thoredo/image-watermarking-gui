import tkinter as tk
from tkinter.colorchooser import askcolor


class ColorWidget:
    """
    Represents the color selection widget for the watermark.

    Attributes
    ----------
    watermark (Watermark): The watermark widget to which the color is associated.
    color_label (tk.Label): The label for displaying the selected color.
    color_button (tk.Button): The button for choosing a color.

    Methods
    -------
    color_picker(): Opens a color picker dialog, updates the button color,
                    and sets the selected color for the watermark.
    """

    def __init__(self, watermark):
        """
        Initializes the ColorWidget.

        Parameters
        ----------
        watermark (Watermark): The watermark widget to which the color is associated.

        Returns
        -------
        None
        """
        self.watermark = watermark

        self.color_label = tk.Label(
            text="Color:", bg="#000000", fg="#fafafa", font=("Arial", 12, "bold")
        )
        self.color_label.grid(column=4, row=9, sticky=tk.W)

        self.color_button = tk.Button(
            text="      ", bg="#fafafa", fg="#fafafa", command=self.color_picker
        )
        self.color_button.grid(column=5, row=9, sticky=tk.E)

    def color_picker(self):
        """
        Opens a color picker dialog, updates the button color, and sets the
        selected color for the watermark.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        colors = askcolor(title="Choose a color")
        new_color = colors[0]
        self.color_button.configure(bg=colors[1])
        self.watermark.color_main = new_color
        self.watermark.show_watermark()
