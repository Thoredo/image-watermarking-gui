import tkinter as tk


class OpacityWidget:
    def __init__(self, master, watermark):
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
        opacity_value = int(value)
        self.watermark.opacity_main = opacity_value
        self.watermark.show_watermark()
