import os
import sys
import tkinter as tk
from tkinter import filedialog
from tkinter.colorchooser import askcolor
from tkinter.ttk import Combobox
from matplotlib import font_manager
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, "./widgets/")

from widgets.image_frame import ImageFrame
from widgets.size_label import ImageSizeLabel
from widgets.select_file import SelectFile
from widgets.directional_arrows import DirectionalArrows
from widgets.watermark import Watermark
from widgets.rotation_buttons import RotationButtons


class WatermarkingDesktopApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Watermarking GUI")
        self.master.config(padx=20, pady=20, bg="black")
        self.master.minsize(height=100, width=500)

        self.create_main_menu()

    def create_main_menu(self):
        self.image_frame = ImageFrame(self.master)
        self.size_label = ImageSizeLabel(self.master)
        self.select_file = SelectFile(self.master, self.image_frame, self.size_label)
        self.color_label_button()
        self.opacity_label_slider()
        self.font_size_widget()
        self.select_font_widget()
        self.save_widget()
        self.watermark = Watermark(
            self.master,
            self.select_file,
            self.size_label,
            self.image_frame,
        )
        self.directional_arrows = DirectionalArrows(
            self.master, self.select_file, self.size_label, self.watermark
        )
        self.rotation_buttons = RotationButtons(self.master, self.watermark)

    def color_label_button(self):
        self.color_label = tk.Label(
            text="Color:", bg="#000000", fg="#fafafa", font=("Arial", 12, "bold")
        )
        self.color_label.grid(column=4, row=9, sticky=tk.W)

        self.color_button = tk.Button(
            text="      ", bg="#fafafa", fg="#fafafa", command=self.color_picker
        )
        self.color_button.grid(column=5, row=9, sticky=tk.E)

    def opacity_label_slider(self):
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

    def font_size_widget(self):
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

    def select_font_widget(self):
        font_list = font_manager.findSystemFonts(fontpaths=None, fontext="ttf")
        final_font_list = []
        formatted_font_list = [font.split("\\")[-1] for font in font_list]
        for font in formatted_font_list:
            if ".otf" not in font:
                final_font_list.append(font)
        final_font_list.sort()
        # Find the index of 'arial.ttf' in the font_list
        arial_index = final_font_list.index("arial.ttf")

        # Trim the font list up to 'arial.ttf' (inclusive)
        trimmed_font_list = final_font_list[arial_index:]

        default_font = tk.StringVar(self.master)
        default_font.set("arial")

        self.font_type_label = tk.Label(
            text="Font:", bg="#000000", fg="#fafafa", font=("Arial", 12, "bold")
        )
        self.font_type_label.grid(column=4, row=12, sticky=tk.W)

        self.chosen_font_type = Combobox(
            self.master,
            textvariable=default_font,
            values=trimmed_font_list,
            state="readonly",
        )
        self.chosen_font_type.grid(column=5, row=12, sticky=tk.E)
        self.chosen_font_type.bind("<<ComboboxSelected>>", self.change_font_type)

    def save_widget(self):
        self.save_button = tk.Button(
            text="Save", bg="#e7e7e7", fg="black", command=self.save_image
        )
        self.save_button.grid(column=7, row=16)

    def color_picker(self):
        colors = askcolor(title="Choose a color")
        new_color = colors[0]
        self.color_button.configure(bg=colors[1])
        self.watermark.color_main = new_color
        self.watermark.show_watermark()

    def change_opacity(self, value):
        opacity_value = int(value)
        self.watermark.opacity_main = opacity_value
        self.watermark.show_watermark()

    def change_font_size(self):
        self.watermark.font_size_main = int(self.chosen_font_size.get())
        self.watermark.show_watermark()

    def change_font_type(self, event=None):
        self.watermark.font_main = self.chosen_font_type.get()
        self.watermark.show_watermark()

    def save_image(self):
        path = filedialog.asksaveasfilename(
            confirmoverwrite=True,
            defaultextension="png",
            filetypes=[
                ("jpeg", ".jpg"),
                ("png", ".png"),
                ("bitmap", "bmp"),
                ("gif", ".gif"),
            ],
        )
        if path and os.path.splitext(path)[1] == ".jpg":
            image = self.watermark.img_main.convert("RGB")
            image.save(path)
            tk.messagebox.showinfo("Success", "Image got watermarked and saved.")
