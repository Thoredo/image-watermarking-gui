import tkinter as tk


class RotationButtons:
    def __init__(self, master, watermark):
        self.master = master
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
        self.watermark.rotation_main += 5
        self.watermark.show_watermark()

    def rotate_right(self):
        self.watermark.rotation_main -= 5
        self.watermark.show_watermark()
