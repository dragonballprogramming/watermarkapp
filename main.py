from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename
from PIL import Image

# Image path for saving image
Image_Path = "/Users/kylechesnick/PycharmProjects/day84watermarkapp/img/water-mark.jpg"

#setup tkinter window
window = Tk()
window.title("Watermark Generator")
window.config(padx=50, pady=50)

def water_mark():
    # import image from file
    pic = askopenfilename()
    img = Image.open(pic).convert("RGB")
    # Converts image to jpg
    if not img.mode == 'RGB':
        img = img.convert('RGB')
    w_img = Image.open(Image_Path).convert("RGBA")
    w_img = w_img.copy()
    #makes water mark image transparant
    w_img.putalpha(100)
    #sets size of the water mark compared to the image
    wm_resized = w_img.resize((round(img.size[0] * .40), round(img.size[1] * .40)))
    wm_mask = wm_resized.convert("RGBA")

    # Set position to lower right corner
    position = (img.size[0] - wm_resized.size[0], img.size[1] - wm_resized.size[1])
    transparent = Image.new('RGBA', img.size, (0, 0, 0, 0))
    transparent.paste(img, (0, 0))
    transparent.paste(wm_mask, position, mask=wm_mask)
    transparent.show()

    # Save watermarked photo to same folder it was taken from 
    finished_img = transparent.convert("RGB")
    finished_img_name = pic[:-4] + " WM.jpg"
    finished_img.save(finished_img_name)

#button label
button_label = Label(
    window,
    text='Upload image for watermark '
    )
button_label.grid(row=0, column=0, padx=10)

# upload button
up_load_button = Button(
    window,
    text='Upload Files',
    command=lambda:water_mark()
    )
up_load_button.grid(row=3, columnspan=3, pady=10)

# built in while loop to keep window open
window.mainloop()