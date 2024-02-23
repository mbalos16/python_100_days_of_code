"""'
One of my favourite websites to go to when I'm designing anything is a colour 
palette website called Flat UI Colors: https://flatuicolors.com/palette/defo

It's a really simple static website that shows a bunch of colours and their HEX codes. 
I can copy the HEX codes and use it in my CSS or any design software.

On day 76, you learnt about image processing with NumPy. Using this knowledge 
and your developer skills (that means Googling), build a website where a user 
can upload an image and you will tell them what are the top 10 most common colours in that image.

This is a good example of this functionality: http://www.coolphptools.com/color_extract#demo
"""

import os

from flask import Flask, render_template, request, send_from_directory, url_for

from image_processing import extract_palette_from_img

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/palette", methods=["POST"])
def get_image_palette():
    if request.method == "POST":
        image = request.files["img"]
        path = os.path.join(app.config["UPLOAD"], image.filename)
        image.save(path)
        image_path = url_for("uploaded_file", filename=image.filename)
        colours = extract_palette_from_img(path)
        return render_template("colors.html", image_path=image_path, colours=colours)


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD"], filename)


if __name__ == "__main__":
    upload_dir = os.path.split(__file__)[0]
    upload_dir = os.path.join(upload_dir, "static", "uploads")
    os.makedirs(upload_dir, exist_ok=True)
    app.config["UPLOAD"] = upload_dir
    app.run(debug=True)
