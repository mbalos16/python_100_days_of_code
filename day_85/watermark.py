'''
Using what you have learnt about Tkinter, you will create a desktop application with a Graphical User Interface (GUI) 
where you can upload an image and use Python to add a watermark logo/text. Normally, you would have to use an image 
editing software like Photoshop to add the watermark, but your program is going to do it automatically.

Use case: e.g you want to start posting your photos to Instagram but you want to add your website to all the photos, 
you can now use your software to add your website/logo automatically to any image.

A similar online service is: https://watermarkly.com/

You might need:
https://pypi.org/project/Pillow/
https://docs.python.org/3/library/tkinter.html

and some Googling.
'''

from tkinter import *
import tkinter as tk
from PIL import Image, ImageFont, ImageDraw
from tkinter import filedialog

BACKGROUND_COLOUR = "#592720"
TEXT_COLOUR_ON_BG = "#ecf0f1"
BTN_COLOR = "#44362F"
FONT_NAME = "Copperplate"
CATEGORY_COLOR = "#F4A460"
TITLE_COLOR = "#EDC9AF"
SMALL_TEXT_FONT = "Helvetica"


### Functions
def watermark_info(image_path):
    """Informs the user if the image has been uploaded correctly."""
    msg = tk.messagebox.showinfo(
        "alert",
        f"Your images has been uploaded successfuly and watermarked. Please follow this link to see the image:{image_path}",
    )


def watermark(image_path, logo_path, logo_text):
    """Watermark the image with a logo or a text

    Args:
        image_path (str): path of the image
        logo_path (str): path of the logo
        logo_text (str): text as logo
    """
    image_path = image_path.cget("text")
    logo_path = logo_path.cget("text")
    logo_text = logo_text.get("1.0", END).strip()
    # Get the image path.
    # Get the text or the logo: if text watermark_image_text else: watermark_image_logo
    print(image_path, logo_path, logo_text)
    if logo_path.startswith("/"):
        image_watermark_logo = watermark_image_logo(
            img_path=image_path, logo_path=logo_path
        )
    elif len(logo_text) != 0:
        image_watermark_text = watermark_image_text(img_path=image_path, text=logo_text)
    watermark_info(image_path)


def upload_image(path_field):
    """Opens the dialog box for the user to locate the file in the system."""
    path = filedialog.askopenfilename(
        filetypes=[("JPG files", ".jpg"), ("PNG files", ".png")],
        title="Upload your image to WW",
    )
    path_field.configure(text=path)
    return path


def watermark_image_text(img_path, text):
    """Watermarks an image with text.
    Args:
        img_path (str): The path where the image is located.
        text (str): The text to be added on top of the image as a logo.
    """

    # load image
    image = Image.open(img_path).convert("RGBA")
    # create the frame
    text_img = Image.new("RGBA", image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(text_img)
    # Specify the position for the text
    text_position = (10, 10)

    # Measure the size of the font
    font = ImageFont.truetype(FONT_NAME, 1)
    left, upper, right, lower = font.getbbox(text)

    # Calculate the scaling factor so that the text is 1/20 the height of the image
    factor = 1 / 20 * image.size[1] / (lower - upper)
    font = ImageFont.truetype(FONT_NAME, factor)

    # Draw the text
    draw.text(text_position, text, fill=(0, 0, 0), font=font)

    # Composite the text overlay onto the original image
    watermarked_image = Image.alpha_composite(image, text_img)
    image_saved = save_image(watermarked_image, img_path)
    return image_saved


def watermark_image_logo(img_path, logo_path):
    """Watermarks an image with a provided logo.
    Args:
        img_path (str): The path to the image.
        logo_path (str): The path to the logo.
    Returns:
        str: A confirmation that the wathermarked image has been saved correctly and the parh to it.
    """
    # load image
    image = load_image(img_path)
    # load logo
    logo = load_image(logo_path)
    # merge the image and the logo
    new_image = merge_images(img_bottom=image, img_top=logo)
    # save the image and return the notifiaction
    image_saved = save_image(new_image, img_path)
    return image_saved


def merge_images(img_bottom, img_top):
    """Merge two images together adding one on top of the other.

    Args:
        img_bottom (PIL.Image): The main image.
        img_top (PIL.Image): The logo.

    Returns:
        PIL.Image: The resulting image after watermarking
    """
    # get the sizes of the bottom and top images
    width_bottom, height_bottom = img_bottom.size
    width_top, height_top = img_top.size

    # We want the logo to be 1/20th of the image
    factor = 1 / 10 * min(width_bottom / width_top, height_bottom / height_top)
    # resize the top image
    img_top = resize_logo(img_top, width_top, height_top, factor=factor)
    width_top, height_top = img_top.size  # Update after resize

    # Create the new image canvas
    final_image = Image.new("RGBA", (width_bottom, height_bottom))
    # Add the bottom image to the canvas
    final_image.paste(img_bottom)
    # Add the top image tot he canvas
    margin = min(width_top, height_top)
    position = int(width_bottom - width_top - margin), int(
        height_bottom - height_top - margin
    )
    final_image.paste(img_top, position, mask=img_top)
    return final_image


def resize_logo(image, width, height, factor):
    """Resize the provided image keeping the aspect ratio.
    Args:
        image (PIL.Image): The main image to be resized.
        width (int): Image width
        height (int): Image heignt
        factor (float): Resize factor
    Returns:
        PIL.Image: The resized image.
    """
    new_width = int(width * factor)
    new_height = int(height * factor)
    img = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    return img


def load_image(img_path):
    """Opens the image.
    Args:
        img_path (str): The image path to be open.
    Returns:
        PIL.Image: The main image.
    """
    return Image.open(img_path)


def save_image(img, path):
    """This function will save the image.
    Args:
        img (PIL.Image): Image to save.
        path (str): Path to the image
    Returns:
        str: _description_
    """
    img = img.convert("RGB")
    img_path = path.replace(".jpg", "_wathermark.jpg")
    img = img.save(img_path)
    return print(
        f"The watermarked image has been saved correctly. Please follow this path: {img_path} to see the result."
    )


def app():
    """The tkinter aplication that opens the GUI."""
    ### Window creation
    window = tk.Tk()
    window.minsize(width=600, height=400)
    window.configure(background=BACKGROUND_COLOUR)
    window.title("WW - Watermark APP")
    window.config(padx=80, pady=20)

    ## Extra space
    extra = tk.Label(
        text="",
        foreground=TEXT_COLOUR_ON_BG,
        bg=BACKGROUND_COLOUR,
        font=(FONT_NAME, 11, "italic"),
    )
    extra.pack(pady=15)

    ### App title and subtitle
    title_text = tk.Label(
        text="Weever Watermark",
        foreground=TITLE_COLOR,
        bg=BACKGROUND_COLOUR,
        font=(FONT_NAME, 32, "bold"),
        anchor=CENTER,
    )
    title_text.pack(padx=20)

    subtitle = tk.Label(
        text="Claim Your Content, Effortlessly",
        foreground=TEXT_COLOUR_ON_BG,
        bg=BACKGROUND_COLOUR,
        font=(FONT_NAME, 16),
    )
    subtitle.pack()
    leader_label = tk.Label(
        text="The leader application for watermarking images.",
        foreground=TEXT_COLOUR_ON_BG,
        bg=BACKGROUND_COLOUR,
        font=(FONT_NAME, 11, "italic"),
    )
    leader_label.pack()

    ## Extra space
    extra = tk.Label(
        text=" ",
        foreground=TEXT_COLOUR_ON_BG,
        bg=BACKGROUND_COLOUR,
    )
    extra.pack(pady=15)

    ### Add image
    add_image_label = tk.Label(
        text="Upload Your Image to be Signed",
        bd=0,
        fg=CATEGORY_COLOR,
        bg=BACKGROUND_COLOUR,
        font=(FONT_NAME, 18),
    )
    add_image_label.pack()

    ### Upload image
    upload_image_btn = tk.Button(
        window,
        text="Browse image",
        width = 32,
        bd=0,
        highlightbackground=BACKGROUND_COLOUR,
        command=lambda: upload_image(extension_image),
        fg=BACKGROUND_COLOUR,
        bg=BACKGROUND_COLOUR,
    )
    upload_image_btn.pack(pady=2)

    ## Extensions allowed for the image
    extension_image = tk.Label(
        text="Extensions: .jpg, .png",
        foreground=TEXT_COLOUR_ON_BG,
        bg=BACKGROUND_COLOUR,
        font=(SMALL_TEXT_FONT, 10),

    )
    extension_image.pack()

    ## Extra space
    extra = tk.Label(
        text="",
        foreground=TEXT_COLOUR_ON_BG,
        bg=BACKGROUND_COLOUR,
        font=(FONT_NAME, 11, "italic"),
    )
    extra.pack(pady=10)

    ### Select watermark option
    selection_text = tk.Label(
        text="Upload Your Signature",
        foreground=CATEGORY_COLOR,
        bg=BACKGROUND_COLOUR,
        font=(FONT_NAME, 18),
    )
    selection_text.pack()


    ### Upload logo
    upload_logo_btn = tk.Button(
        window,
        text="Browse logo",
        bd=0,
        width = 32,
        highlightbackground=BACKGROUND_COLOUR,
        command=lambda: upload_image(logo_extensions),
        fg=BACKGROUND_COLOUR,
        bg=BACKGROUND_COLOUR,
    )
    upload_logo_btn.pack()

    ## Extensions allowed for the logo
    logo_extensions = tk.Label(
        text="Extension: .jpg, .png",
        foreground=TEXT_COLOUR_ON_BG,
        bg=BACKGROUND_COLOUR,
        font=(SMALL_TEXT_FONT, 10),
    )
    logo_extensions.pack()
    logo_extensions.config(padx=100)

    ## OR
    or_text = tk.Label(
        text="------- OR -------",
        foreground=TEXT_COLOUR_ON_BG,
        bg=BACKGROUND_COLOUR,
        font=(SMALL_TEXT_FONT, 12),
    )
    or_text.pack(pady=10)

    ### Add text
    add_text_label = tk.Label(
        text="Add text as signature",
        bd=0,
        fg=TEXT_COLOUR_ON_BG,
        bg=BACKGROUND_COLOUR,
        font=(SMALL_TEXT_FONT, 12),
    )
    add_text_label.pack()

    input_text = tk.Text(window, height=3, width=24)
    input_text.pack()

    ## Button for watermarking
    watermark_btn = tk.Button(
        text="WATERMARK",
        bd=0,
        highlightbackground=BACKGROUND_COLOUR,
        command=lambda: watermark(extension_image, logo_extensions, input_text),
        fg=BACKGROUND_COLOUR,
        width=32,
    )
    watermark_btn.pack(pady=10)

    ## Extra space
    extra = tk.Label(
        text="",
        foreground=TEXT_COLOUR_ON_BG,
        bg=BACKGROUND_COLOUR,
        font=(FONT_NAME, 11, "italic"),
    )
    extra.pack(pady=15)
    window.mainloop()


if __name__ == "__main__":
    app()
