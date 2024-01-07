import tkinter as tk


class OpacityWidget:
    """
    Represents a widget for adjusting watermark opacity.

    Attributes
    ----------
    master (tk.Tk): The main Tkinter window.
    watermark (Watermark): The watermark widget to which the opacity is associated.
    opacity_label (tk.Label): The label indicating the purpose of the Scale.
    opacity_slider (tk.Scale): The Scale widget for adjusting opacity.

    Methods
    -------
    __init__(): Initializes the OpacityWidget.
    change_opacity(): Changes the opacity based on the selected value and
                      updates the displayed watermark.
    """

    def __init__(self, master, watermark):
        """
        Initializes the OpacityWidget.

        Parameters
        ----------
        master (tk.Tk): The main Tkinter window.
        watermark (Watermark): The watermark widget to which the opacity is associated.
        """
        self.master = master
        self.watermark = watermark

        self.opacity_label = tk.Label(
            text="Opacity:", bg="#000000", fg="#fafafa", font=("Arial", 12, "bold")
        )
        self.opacity_label.grid(column=4, row=10, sticky=tk.W)

        self.opacity_slider = tk.Scale(
            self.master,
            from_=0,
            to=255,
            orient="horizontal",
            bg="#000000",
            fg="#fafafa",
            highlightthickness=0,
            command=self.change_opacity,
        )
        self.opacity_slider.set(255)
        self.opacity_slider.grid(column=5, row=10, ipadx=20, sticky=tk.E)

    def change_opacity(self, value):
        """
        Changes the opacity based on the selected value and updates the displayed watermark.

        Parameters
        ----------
        value (int): The selected opacity value.

        Returns
        -------
        None
        """
        opacity_value = int(value)
        self.watermark.opacity_main = opacity_value
        self.watermark.show_watermark()
