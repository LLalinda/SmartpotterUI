from tkinter import *


root = Tk()
root.geometry('800x450')
root.title('Smart Potter')

# Add image file
bg = PhotoImage(file = "Select Design.png")


# Show image using label
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0, relwidth=1, relheight=1)


def nextPage():
    root.destroy()
    import page_5


def prevPage():
    root.destroy()
    import page_2_p2





# Creating a photoimage object to use image
Bt_Photo1 = PhotoImage(file = r"back.png")
Bt_Photo2 = PhotoImage(file = r"cancel.png")
Bt_Photo3 = PhotoImage(file = r"D1.png")
Bt_Photo4 = PhotoImage(file = r"D2.png")
Bt_Photo5 = PhotoImage(file = r"D3.png")

# set image on button

backBt = Button(root, image = Bt_Photo1,width=50, height=50, bg="#F2E3B7", activebackground="#F2E3B7", borderwidth=0, command=prevPage)
backBt.place(x=650, y=35)

exitBt = Button(root, image = Bt_Photo2,width=50, height=50, bg="#F2E3B7", activebackground="#F2E3B7", borderwidth=0, command=root.destroy)
exitBt.place(x=700, y=35)

D1Bt = Button(root, image = Bt_Photo3,width=180, height=180, bg="#F2E3B7", activebackground="#F2E3B7", borderwidth=0, command=nextPage)
D1Bt.place(x=110, y=170)

D2Bt = Button(root, image = Bt_Photo4,width=180, height=180, bg="#F2E3B7", activebackground="#F2E3B7", borderwidth=0, command=nextPage)
D2Bt.place(x=313, y=170)

D3Bt = Button(root, image = Bt_Photo5,width=180, height=180, bg="#F2E3B7", activebackground="#F2E3B7", borderwidth=0, command=nextPage)
D3Bt.place(x=515, y=170)


root.mainloop()