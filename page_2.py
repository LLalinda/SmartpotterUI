from tkinter import *

root = Tk()
root.geometry('800x450')
root.title('Smart Potter')

# Add image file
bg = PhotoImage(file = "Pick Choice.png")


# Show image using label
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0, relwidth=1, relheight=1)


 
def nextPage1():
    root.destroy()
    import page_3

def nextPage2():
    root.destroy()
    import page_4

def prevPage():
    root.destroy()
    import Smart_Potter





# Creating a photoimage object to use image
Bt_Photo1 = PhotoImage(file = r"back.png")
Bt_Photo2 = PhotoImage(file = r"cancel.png")
Bt_Photo3 = PhotoImage(file = r"INT_DS.png")
Bt_Photo4 = PhotoImage(file = r"DEF_DS.png")

# set image on button

backBt = Button(root, image = Bt_Photo1,width=50, height=50, bg="#F2E3B7", activebackground="#F2E3B7", borderwidth=0, command=prevPage)
backBt.place(x=650, y=35)

exitBt = Button(root, image = Bt_Photo2,width=50, height=50, bg="#F2E3B7", activebackground="#F2E3B7", borderwidth=0, command=root.destroy)
exitBt.place(x=700, y=35)

intdsBt = Button(root, image = Bt_Photo3,width=180, height=180, bg="#F2E3B7", activebackground="#F2E3B7", borderwidth=0, command=nextPage1)
intdsBt.place(x=175, y=170)

defdsBt = Button(root, image = Bt_Photo4,width=180, height=180, bg="#F2E3B7", activebackground="#F2E3B7", borderwidth=0, command=nextPage2)
defdsBt.place(x=445, y=170)

root.mainloop()