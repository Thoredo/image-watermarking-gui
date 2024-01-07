import tkinter as tk


class DirectionalArrows:
    def __init__(self, master, select_file, size_label, watermark):
        self.master = master
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
        if self.select_file.original_height > 1500:
            self.size_label.height_main -= 50
        else:
            self.size_label.height_main -= 10
        self.watermark.show_watermark()

    def down(self):
        if self.select_file.original_height > 1500:
            self.size_label.height_main += 50
        else:
            self.size_label.height_main += 10
        self.watermark.show_watermark()

    def left(self):
        if self.select_file.original_width > 1500:
            self.size_label.width_main -= 50
        else:
            self.size_label.width_main -= 10
        self.watermark.show_watermark()

    def right(self):
        if self.select_file.original_width > 1500:
            self.size_label.width_main += 50
        else:
            self.size_label.width_main += 10
        self.watermark.show_watermark()
