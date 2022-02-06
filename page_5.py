from tkinter import *
from tkinter import messagebox


root = Tk()
root.geometry('800x450')
root.title('Smart Potter')

# Add image file
bg = PhotoImage(file = "Confirm Design.png")


# Show image using label
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0, relwidth=1, relheight=1)

# Creating a photoimage object to use image
Bt_Photo1 = PhotoImage(file = r"start.png")

# Define a function to show the popup message
def show_msg():
   messagebox.showinfo("Message","Thank You! Your order is being processed. It may take some time.")


# set image on button

startBt = Button(root, image = Bt_Photo1,width=200, height=90, bg="#F2E3B7", activebackground="#F2E3B7", borderwidth=0, command=show_msg)
startBt.place(x=280, y=200)









root.mainloop()