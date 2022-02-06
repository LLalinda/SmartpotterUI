from tkinter import *

root = Tk()
root.geometry('800x450')
root.title('Smart Potter')

# Add image file
bg = PhotoImage(file = "home.png")


# Show image using label
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0, relwidth=1, relheight=1)


def nextPage():
    root.destroy()
    import page_2



# Creating a photoimage object to use image
Bt_Photo1 = PhotoImage(file = r"right-arrow.png")
Bt_Photo2 = PhotoImage(file = r"cancel.png")

# set image on button
Bt1 = Button(root, image = Bt_Photo1,width=50, height=50, bg="#E9D694", activebackground="#F2E3B7", command=nextPage)
Bt1.place(x=715, y=275)

exitBt = Button(root, image = Bt_Photo2,width=50, height=50, bg="#F2E3B7", activebackground="#F2E3B7", borderwidth=0, command=root.destroy)
exitBt.place(x=700, y=35)






root.mainloop()