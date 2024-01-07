import sys

sys.path.insert(0, "./widgets/")

# Importing necessary widgets
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
from widgets.save_button import SaveButton


class WatermarkingDesktopApp:
    """
    Creates an instance for the Watermarking Desktop App, contains the main gui
    and imports all widgets from other classes.

    Attributes
    ----------
    master (tk.Tk): The main Tkinter window.
    image_frame (ImageFrame): The widget for displaying images.
    size_label (ImageSizeLabel): The widget for displaying image size.
    select_file (SelectFile): The widget for selecting image files.
    watermark (Watermark): The widget for adding watermarks to images.
    directional_arrows (DirectionalArrows): The widget for adjusting image position.
    rotation_buttons (RotationButtons): The widget for rotating watermarks.
    color_widget (ColorWidget): The widget for selecting watermark color.
    opacity_widget (OpacityWidget): The widget for adjusting watermark opacity.
    font_size_widget (FontSizeWidget): The widget for adjusting font size.
    select_font_widget (FontTypeWidget): The widget for selecting font type.
    save_widget (SaveButton): The widget for saving watermarked images.

    Methods
    ----------
    __init__(): Initializes the WatermarkingDesktopApp.

    create_main_menu(): Creates the main menu of the application.
    """

    def __init__(self, master):
        """
        Initializes the WatermarkingDesktopApp.

        Parameters
        ----------
        master(tk.Tk): The main Tkinter window.

        Returns
        -------
        None
        """
        self.master = master
        self.master.title("Watermarking GUI")
        self.master.config(padx=20, pady=20, bg="black")
        self.master.minsize(height=100, width=500)

        self.create_main_menu()

    def create_main_menu(self):
        """
        Creates the main menu of the application.
        Initializes and places all the necessary widgets.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.image_frame = ImageFrame(self.master)
        self.size_label = ImageSizeLabel()
        self.select_file = SelectFile(self.image_frame, self.size_label)
        self.watermark = Watermark(
            self.select_file,
            self.size_label,
            self.image_frame,
        )
        self.directional_arrows = DirectionalArrows(
            self.select_file, self.size_label, self.watermark
        )
        self.rotation_buttons = RotationButtons(self.watermark)
        self.color_widget = ColorWidget(self.watermark)
        self.opacity_widget = OpacityWidget(self.master, self.watermark)
        self.font_size_widget = FontSizeWidget(self.master, self.watermark)
        self.select_font_widget = FontTypeWidget(self.master, self.watermark)
        self.save_widget = SaveButton(self.watermark)
