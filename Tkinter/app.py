"""
Name: Abhinav Kotamreddy
Program Description: Reads a pdf and puts all the text into a text box
Date: 2/2/23
"""
from tkinter import *
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
from functions import display_logo, display_textbox, display_icon, copy_text

#global parameters
all_content = []
all_images = []
img_idx = [0]
#initiallize a Tkinter object
root = Tk()
root.geometry('+%d+%d'%(350,10)) #place GUI at x=350, y=10

#header area - logo & browse button
header = Frame(root, width=1400, height=300, bg="white")
header.grid(columnspan=3, rowspan=2, row=0)

#main content area - text and image extraction
main_content = Frame(root, width=1400, height=300, bg="#20bebe")
main_content.grid(columnspan=3, rowspan=2, row=4)

def open_file():

    #clear global list of indices
    for i in img_idx:
        img_idx.pop()
    img_idx.append(0) #set global index to 0

    browse_text.set("loading...")

    #load a PDF file
    file = askopenfile(parent=root, mode='rb', filetypes=[("Pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfReader(file)
        #select a page
        page = read_pdf.pages[0]
        #extract text content from page
        page_content = page.extract_text()

        page_content = page_content.replace('\u2122', "'")

        #clear the content of the previous PDF file
        if all_content:
            for i in all_content:
                all_content.pop()

        #extract text
        all_content.append(page_content)
     
        #display the text found on the page
        display_textbox(all_content, 4, 1, root)

        #reset the button text back to Browse
        browse_text.set("Browse")
       
        #create action buttons
        copyText_btn = Button(root, text="Copy the Text",command=lambda:copy_text(all_content, root), font=("shanti", 10), height=1, width=15)

        #place buttons on grid
        copyText_btn.grid(row=3,column=1)

#display the logo
display_logo('logo.png', 0, 0)

#instructions
instructions = Label(root, text="Select a PDF file", font=("Raleway", 10), bg="white")
instructions.grid(column=2, row=0, sticky=SE, padx=75, pady=5)

#browse button
browse_text = StringVar()
browse_btn = Button(root, textvariable=browse_text, command=lambda:open_file(), font=("Raleway",12), bg="#20bebe", fg="white", height=1, width=15)
browse_text.set("Browse")
browse_btn.grid(column=2, row=1, sticky=NE, padx=50)

root.mainloop()
