import os
import sys
import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Combobox
from matplotlib import font_manager

sys.path.insert(0, "./widgets/")

from widgets.image_frame import ImageFrame
from widgets.size_label import ImageSizeLabel
from widgets.select_file import SelectFile
from widgets.directional_arrows import DirectionalArrows
from widgets.watermark import Watermark
from widgets.rotation_buttons import RotationButtons
from widgets.color_widget import ColorWidget
from widgets.opacity_widget import OpacityWidget
from widgets.font_size_widget import FontSizeWidget


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
        self.color_widget = ColorWidget(self.master, self.watermark)
        self.opacity_widget = OpacityWidget(self.master, self.watermark)
        self.font_size_widget = FontSizeWidget(self.master, self.watermark)

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
