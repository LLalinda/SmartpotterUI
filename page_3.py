from tkinter import *
from tkinter import filedialog

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
      
    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)


root = Tk()
root.geometry('800x450')
root.title('Smart Potter')

# Add image file
bg = PhotoImage(file = "Input Design.png")


# Show image using label
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0, relwidth=1, relheight=1)

# Create a File Explorer label
label_file_explorer = Label(root,
                            text = "File Explorer using Tkinter",
                            width = 100, height = 4,
                            fg = "brown",bg= "#FAEDCB")
label_file_explorer.place(x=50, y=120)


def nextPage():
    root.destroy()
    import page_5


def prevPage():
    root.destroy()
    import page_2_p1






# Creating a photoimage object to use image
Bt_Photo1 = PhotoImage(file = r"back.png")
Bt_Photo2 = PhotoImage(file = r"cancel.png")
Bt_Photo3 = PhotoImage(file = r"add.png")
Bt_Photo4 = PhotoImage(file = r"next.png")


# set image on button

backBt = Button(root, image = Bt_Photo1,width=50, height=50, bg="#F2E3B7", activebackground="#F2E3B7", borderwidth=0, command=prevPage)
backBt.place(x=650, y=35)

exitBt = Button(root, image = Bt_Photo2,width=50, height=50, bg="#F2E3B7", activebackground="#F2E3B7", borderwidth=0, command=root.destroy)
exitBt.place(x=700, y=35)

addBt = Button(root, image = Bt_Photo3,width=400, height=100, bg="#F2E3B7", activebackground="#F2E3B7", borderwidth=0, command = browseFiles)
addBt.place(x=200, y=200)

nextBt = Button(root, image = Bt_Photo4,width=50, height=50, bg="#F2E3B7", activebackground="#F2E3B7", borderwidth=0, command=nextPage)
nextBt.place(x=380, y=320)





root.mainloop()