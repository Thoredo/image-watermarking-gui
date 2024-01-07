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
from widgets.font_type_widget import FontTypeWidget


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
        self.select_font_widget = FontTypeWidget(self.master, self.watermark)

    def save_widget(self):
        self.save_button = tk.Button(
            text="Save", bg="#e7e7e7", fg="black", command=self.save_image
        )
        self.save_button.grid(column=7, row=16)

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
