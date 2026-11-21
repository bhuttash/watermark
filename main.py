from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
from image import WMImage

def pick_file(img_obj):
    file_path = filedialog.askopenfilename(
        title="Select an image file",
        initialdir=".",  # Starts in the current working directory
        filetypes=(
            ("Image files", "*.jpg"),
            ("All files", "*.*")
        )
    )
    
    # askopenfilename returns an empty string "" if the user cancels
    if file_path:
        img_obj.loc.set(file_path)
        img_obj.label.config(text=f"Selected: {file_path}")

# def getImage(*args):
#     # for arg in args:
#     #     print(arg)
#     imgobj = ImageTk.PhotoImage(Image.open(root.getvar(args[0])))
#     pic.configure(image=imgobj)
#     pic.image = imgobj

root = Tk()
root.title("Watermark-it")
# root.geometry("640x480+2500+300")
root.minsize(320, 240)

# img_loc = StringVar(value="No file selected")
# wm_loc = StringVar(value="No file selected")
# img_loc.trace_add(mode="write", callback=getImage)
# wm_loc.trace_add(mode="write", callback=getImage)

frm = ttk.Frame(root, padding=20)

img = WMImage(frm)
wm = WMImage(frm)

find_img_btn = ttk.Button(frm, text="Find an image to modify", command=lambda: pick_file(img), padding=10)
find_wm_btn = ttk.Button(frm, text="Find a watermark image", command=lambda: pick_file(wm), padding=10)

# img_label = ttk.Label(frm, text="No file selected")
# wm_label = ttk.Label(frm, text="No file selected")

welcome_label = ttk.Label(frm, text="Welcome!")
quit_button = ttk.Button(frm, text="Quit", command=root.destroy)

# img = PhotoImage()
# wm = PhotoImage()
# image = ttk.Label(frm, image=img)
# watermark = ttk.Label(frm, image=wm)

frm.grid(row=0, column=0)
welcome_label.grid(column=1, row=0)
img.grid(column=1, row=1)
wm.grid(column=2, row=1)
find_img_btn.grid(column=1, row=2)
# img_label.grid(column=1, row=5)
find_wm_btn.grid(column=2, row=2)
# wm_label.grid(column=2, row=5)
quit_button.grid(column=1, row=10)


root.mainloop()