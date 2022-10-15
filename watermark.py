from tkinter import *
from PIL import Image, ImageDraw, ImageFont


def operation_watermark():
    # get image path from GUI
    # first make sure you strip the " from the path, so you don't have any issues later
    raw_path = str(img_path.get().strip('"'))
    # f to insert variable, r for a raw string
    im = Image.open(fr"{raw_path}")

    # crete watermark and paste it into the image
    watermark = im.copy()
    draw = ImageDraw.Draw(watermark)
    text_size = int(im.size[0] / 20)
    text = ImageFont.truetype("arial.ttf", text_size)
    # create a position for the mark, off center but very visible
    pos_xy = im.size[0] / 2
    # make a list from the str of the rgb entry, and convert items into int to be used
    raw_color = list(color_rgb.get().split(","))
    draw.text((pos_xy, pos_xy), f"{text_e.get()}", (int(raw_color[0]), int(raw_color[1]), int(raw_color[2])), font=text)

    # show the result
    watermark.show()


# GUI
FONT = ("Arial", 8, "normal")
# window
window = Tk()
window.title("WaterMark Maker")
window.minsize(width=420, height=200)
window.config(padx=10, pady=5)

# title
title = Label(text="WaterMark your images with text!", font=("Arial", 10, "bold"))
title.grid(row=0, column=1, pady=(5, 10))

# labels
img = Label(text="Image path", font=FONT)
img.grid(row=1, column=0, pady=5, sticky="w")

text_l = Label(text="Text", font=FONT)
text_l.grid(row=2, column=0, pady=5, sticky="w")

color = Label(text="Text Color (RGB)", font=FONT)
color.grid(row=3, column=0, pady=5, sticky="w")

explain = Label(text="After you hit 'GO', a new window will pop with the processed image.", font=FONT)
explain.grid(row=4, column=0, columnspan=3, pady=5, sticky="W")

# entries
img_path = Entry(width=45)
img_path.insert(0, r"eg: 'C:\Users\Family\Desktop\...'")
img_path.grid(row=1, column=1, columnspan=2, pady=5, sticky="w")

text_e = Entry(width=45)
text_e.grid(row=2, column=1, columnspan=2, pady=5, sticky="w")

color_rgb = Entry(width=45)
color_rgb.insert(0, r"eg: 136,47,209 - max value 255. Separate by a coma")
color_rgb.grid(row=3, column=1, columnspan=2, pady=5, sticky="w")

# button
go = Button(text="Go!", command=operation_watermark)
go.grid(row=5, column=1, pady=10)

window.mainloop()
