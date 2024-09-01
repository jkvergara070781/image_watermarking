from PIL import ImageTk, Image, ImageDraw
import tkinter as tk
from tkinter import filedialog as fd

root = tk.Tk()
root.title('Image Watermarking')

window_width = 1200
window_height = 800

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

root.wm_geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

label = tk.Label(root)
button_1 = tk.Button(root, text='Open Image File', bg='grey', font=('verdana', 16))
button_2 = tk.Button(root, text='Apply Water Mark', bg='grey', font=('verdana', 16), state='disabled')
button_3 = tk.Button(root, text='Save Image File', bg='grey', font=('verdana', 16), state='disabled')
entry = tk.Entry(root, font=('verdana', 16))

image = None
photo_image = None


def select_image():
    global image, photo_image
    entry.delete(0, tk.END)
    filetypes = (('GIF', '*.gif'), ('JPEG', '*.jpg'), ('PNG', '*.png'))
    filename = fd.askopenfilename(title='Select Image', initialdir='/', filetypes=filetypes)
    if filename:
        image = Image.open(filename)
        photo_image = ImageTk.PhotoImage(image)
        label.image = photo_image
        label['image'] = photo_image
        entry.insert(0, filename)
        button_2.config(state='normal')
    else:
        return


button_1['command'] = select_image


def add_watermark():
    global image, photo_image
    image_path = entry.get()
    image = Image.open(image_path)
    width, height = image.size
    draw = ImageDraw.Draw(image)
    for i in range(0, width + height, 50):
        draw.line([(0, height - i), (i, height)], fill=(255, 255, 255, 30), width=3)
    photo_image = ImageTk.PhotoImage(image)
    label.image = photo_image
    label['image'] = photo_image
    button_3.config(state='normal')
    return image


button_2['command'] = add_watermark


def save_image():
    global image
    image = add_watermark()
    filetypes = (
        ('GIF', '*.gif'), ('JPEG', '*.jpg'), ('PNG', '*.png')
        )
    file_path = fd.asksaveasfilename(title='Save Image', filetypes=filetypes)

    if file_path:
        image.save(file_path)
        button_2.config(state='disabled')
        button_3.config(state='disabled')
    else:
        return


button_3['command'] = save_image

root.grid_rowconfigure(0, weight=4)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

label.grid(row=0, column=0, columnspan=3)
button_1.grid(row=1, column=0, ipadx=5, ipady=5)
entry.grid(row=1, column=1, columnspan=2, sticky='we', padx=50)
button_2.grid(row=2, column=0, ipadx=5, ipady=5)
button_3.grid(row=2, column=1, ipadx=5, ipady=5)

root.mainloop()
