import tkinter as tk
from PIL import Image, ImageDraw, ImageFont


class Watermark:
    def __init__(
        self,
        master,
        select_file,
        size_label,
        image_frame,
    ):
        self.master = master
        self.select_file = select_file
        self.size_label = size_label
        self.image_frame = image_frame
        self.rotation_main = 0
        self.color_main = (255, 255, 255)
        self.opacity_main = (255,)
        self.font_size_main = 60
        self.font_main = "Arial"
        self.img_main = ""

        self.watermark_label = tk.Label(
            text="Watermark:",
            width=15,
            bg="#000000",
            fg="#fafafa",
            font=("Arial", 12, "bold"),
        )
        self.watermark_label.grid(column=3, row=2, sticky=tk.W)
        self.watermark_entry = tk.Entry(width=50)
        self.watermark_entry.grid(column=4, row=2, columnspan=4)
        self.show_watermark_button = tk.Button(
            text="Show",
            bg="#e7e7e7",
            fg="black",
            width=6,
            font=("Arial", 12),
            command=self.show_watermark,
        )
        self.show_watermark_button.grid(column=8, row=2, padx=(10, 0))

    def show_watermark(self):
        if not self.select_file.main_file:
            return

        with Image.open(self.select_file.main_file).convert("RGBA") as base:
            txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
            font = ImageFont.truetype(self.font_main.lower(), self.font_size_main)
            d = ImageDraw.Draw(txt)
            fill = self.color_main + (self.opacity_main,)
            d.text(
                (self.size_label.width_main, self.size_label.height_main),
                f"{self.watermark_entry.get()}",
                font=font,
                fill=fill,
            )
            rotated_txt = txt.rotate(self.rotation_main)
            out = Image.alpha_composite(base, rotated_txt)

            marked_img = out.convert("RGBA")
            w_img = self.select_file.resize_image(marked_img)
            self.image_frame.panel.configure(image=w_img)
            self.image_frame.panel.image = w_img

            self.img_main = marked_img
