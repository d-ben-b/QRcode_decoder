from tkinter import *
from tkinter import filedialog,ttk
from PIL import Image
import webbrowser
from pyzbar.pyzbar import decode

def submit():
    style = ttk.Style()
    style.theme_use("clam") 
    return filedialog.askopenfilename(title="Select a QRcode")

def QRcode_decoder():
    # Open the image file
    image = Image.open(submit())
    
    # Decode the QR code
    decoded_objects = decode(image)
    
    # Extract and print the URL (assuming the QR code contains a URL)
    for obj in decoded_objects:
        decoded_data =  obj.data.decode("utf-8")
    
    if decoded_data.startswith("https://") or decoded_data.startswith("https://"):
        webbrowser.open(decoded_data)
    else:
        print(decoded_data)
window = Tk()
window.title("QRcode Decoder")
window.geometry("200x200")
window.call('tk', 'scaling', 2)

button = Button(window, text="QRcode", command=QRcode_decoder,padx=20,pady=20)

button.pack()

window.mainloop()