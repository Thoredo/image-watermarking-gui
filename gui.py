import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont


class WatermarkingDesktopApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Watermarking GUI")
        self.master.config(padx=20, pady=20, bg="black")
        self.master.minsize(height=100, width=500)
        self.height_main = 0
        self.width_main = 0
        self.main_file = ""
        self.original_height = 0
        self.original_width = 0
        self.rotation_main = 0

        self.create_main_menu()

    def create_main_menu(self):
        self.blank_photo()
        self.image_size_label()
        self.watermark_text()
        self.select_file_button()
        self.direction_arrows()
        self.rotation_buttons()
        self.color_picker()

    def blank_photo(self):
        self.blank_photo = Image.new(mode="RGBA", size=(700, 600), color="#242424")
        self.image1 = ImageTk.PhotoImage(self.blank_photo)
        self.panel = tk.Label(self.master, image=self.image1)
        self.panel.image = self.image1
        self.panel.grid(column=0, rowspan=15)

    def image_size_label(self):
        self.image_size = tk.Label(
            text=f"Image size {self.height_main}/{self.width_main} (height/width)",
            bg="#000000",
            fg="#fafafa",
            font=("Arial", 8),
        )
        self.image_size.grid(column=0, row=16, pady=10)

    def watermark_text(self):
        self.watermark = tk.Label(
            text="Watermark:",
            width=15,
            bg="#000000",
            fg="#fafafa",
            font=("Arial", 12, "bold"),
        )
        self.watermark.grid(column=3, row=2, sticky=tk.W)
        self.watermark_entry = tk.Entry(width=50)
        self.watermark_entry.grid(column=4, row=2, columnspan=4)
        self.watermark = tk.Button(
            text="Show",
            bg="#e7e7e7",
            fg="black",
            width=6,
            font=("Arial", 12),
            command=self.show_watermark,
        )
        self.watermark.grid(column=8, row=2, padx=(10, 0))

    def select_file_button(self):
        self.select_file_button = tk.Button(
            text="Select File",
            font=("Arial", 12),
            bg="#e7e7e7",
            fg="black",
            command=self.select_file,
        )
        self.select_file_button.grid(column=0, row=17)

    def direction_arrows(self):
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

    def rotation_buttons(self):
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

    def color_picker(self):
        self.color_label = tk.Label(
            text="Color:", bg="#000000", fg="#fafafa", font=("Arial", 12, "bold")
        )
        self.color_label.grid(column=4, row=9, sticky=tk.W)

        self.color_button = tk.Button(text="      ", bg="#fafafa", fg="#fafafa")
        self.color_button.grid(column=5, row=9, sticky=tk.E)

    def select_file(self):
        self.main_file = filedialog.askopenfilename(
            filetypes=[
                ("JPEG files", "*.jpg;*.jpeg"),
                ("PNG files", "*.png"),
                ("Bitmap files", "*.bmp"),
                ("GIF files", "*.gif"),
            ]
        )
        self.show_selected_image()

    def show_selected_image(self):
        self.img = Image.open(self.main_file)
        width = self.img.size[0]
        height = self.img.size[1]
        self.resized_img = self.resize_image(self.img)
        self.panel.configure(image=self.resized_img)
        self.panel.image = self.resized_img
        self.image_size.config(
            text=f"Image size {height}/{width} (height/width)",
            bg="#000000",
            fg="#fafafa",
            font=("Arial", 8),
        )
        self.height_main = height / 2
        self.width_main = width / 2
        self.original_height = height
        self.original_width = width

    def resize_image(self, img):
        self.size = img.size
        self.panel_size = (700, 600)
        factor = min(
            float(self.panel_size[1]) / self.size[1],
            float(self.panel_size[0]) / self.size[0],
        )
        width = int(self.size[0] * factor)
        height = int(self.size[1] * factor)
        resized_img = img.resize((width, height), Image.LANCZOS)
        return ImageTk.PhotoImage(resized_img)

    def show_watermark(self):
        with Image.open(self.main_file).convert("RGBA") as base:
            txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
            d = ImageDraw.Draw(txt)
            font = ImageFont.truetype("arial.ttf", 60)
            d.text(
                (self.width_main, self.height_main),
                f"{self.watermark_entry.get()}",
                font=font,
                fill="black",
            )
            rotated_txt = txt.rotate(self.rotation_main)
            out = Image.alpha_composite(base, rotated_txt)

            marked_img = out.convert("RGBA")
            w_img = self.resize_image(marked_img)
            self.panel.configure(image=w_img)
            self.panel.image = w_img

            self.img_main = marked_img

    def up(self):
        if self.original_height > 1500:
            self.height_main -= 50
        else:
            self.height_main -= 10
        self.show_watermark()

    def down(self):
        if self.original_height > 1500:
            self.height_main += 50
        else:
            self.height_main += 10
        self.show_watermark()

    def left(self):
        if self.original_width > 1500:
            self.width_main -= 50
        else:
            self.width_main -= 10
        self.show_watermark()

    def right(self):
        if self.original_width > 1500:
            self.width_main += 50
        else:
            self.width_main += 10
        self.show_watermark()

    def rotate_left(self):
        self.rotation_main += 5
        self.show_watermark()

    def rotate_right(self):
        self.rotation_main -= 5
        self.show_watermark()
