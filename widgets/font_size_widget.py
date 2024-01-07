import tkinter as tk


class FontSizeWidget:
    """
    Represents a widget for adjusting font size.

    Attributes
    ----------
    master (tk.Tk): The main Tkinter window.
    watermark (Watermark): The watermark widget to which the font size is associated.
    font_label (tk.Label): The label indicating the purpose of the Spinbox.
    chosen_font_size (tk.Spinbox): The Spinbox for selecting font size.

    Methods
    -------
    __init__(): Initializes the FontSizeWidget.
    change_font_size(): Changes the font size based on the selected value and
                        updates the displayed watermark.
    """

    def __init__(self, master, watermark):
        """
        Initializes the FontSizeWidget.

        Parameters
        ----------
        master (tk.Tk): The main Tkinter window.
        watermark (Watermark): The watermark widget to which the font size is associated.
        """
        self.master = master
        self.watermark = watermark

        self.font_label = tk.Label(
            text="Font Size:", bg="#000000", fg="#fafafa", font=("Arial", 12, "bold")
        )
        self.font_label.grid(column=4, row=11, sticky=tk.W)
        default_font_size = tk.StringVar(self.master)
        default_font_size.set("60")
        self.chosen_font_size = tk.Spinbox(
            self.master,
            from_=1,
            to=1000,
            width=5,
            highlightthickness=0,
            textvariable=default_font_size,
            command=self.change_font_size,
        )
        self.chosen_font_size.grid(column=5, row=11, sticky=tk.E)

    def change_font_size(self):
        """
        Changes the font size based on the selected value and updates the
        displayed watermark.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.watermark.font_size_main = int(self.chosen_font_size.get())
        self.watermark.show_watermark()
