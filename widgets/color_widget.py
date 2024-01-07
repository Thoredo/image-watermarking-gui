import tkinter as tk
from tkinter.colorchooser import askcolor


class ColorWidget:
    def __init__(self, master, watermark):
        self.master = master
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
        colors = askcolor(title="Choose a color")
        new_color = colors[0]
        self.color_button.configure(bg=colors[1])
        self.watermark.color_main = new_color
        self.watermark.show_watermark()
