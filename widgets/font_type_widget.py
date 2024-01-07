import tkinter as tk
from tkinter.ttk import Combobox
from matplotlib import font_manager


class FontTypeWidget:
    def __init__(self, master, watermark):
        self.master = master
        self.watermark = watermark

        font_list = font_manager.findSystemFonts(fontpaths=None, fontext="ttf")
        final_font_list = []
        formatted_font_list = [font.split("\\")[-1] for font in font_list]
        for font in formatted_font_list:
            if ".otf" not in font:
                final_font_list.append(
                    font.replace(".ttf", "").replace(".TTF", "").replace(".ttc", "")
                )
        final_font_list.sort()
        # Find the index of 'arial' in the font_list
        arial_index = final_font_list.index("arial")

        # Trim the font list up to 'arial'
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

    def change_font_type(self, event=None):
        self.watermark.font_main = self.chosen_font_type.get()
        self.watermark.show_watermark()
