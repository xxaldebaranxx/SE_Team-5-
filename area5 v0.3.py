# Import the required libraries
from tkinter import *
from tkinter import font

LARGEFONT =("Verdana", 25)

win = Tk()
win.geometry("1280x720")
win.title("SPPT Application")

# Create two frames in the window
home = Frame(win)
area1 = Frame(win)
area2 = Frame(win)
area3 = Frame(win)


# Define a function for switching the frames
def change_to_home():
   home.pack(fill='both', expand=1)
   area1.pack_forget()
   area2.pack_forget()
   area3.pack_forget()

def change_to_area1():
   area1.pack(fill='both', expand=1)
   area2.pack_forget()
   area3.pack_forget()
   home.pack_forget()

def change_to_area2():
   area2.pack(fill='both', expand=1)
   area1.pack_forget()
   area3.pack_forget()
   home.pack_forget()
   
def change_to_area3():
   area3.pack(fill='both', expand=1)
   area1.pack_forget()
   area2.pack_forget()
   home.pack_forget()

# Create fonts for making difference in the frame
font1 = font.Font(family='Georgia', size='22', weight='bold')
font2 = font.Font(family='Aerial', size='12')

projname = Label(win, text="SPPT", foreground="teal", font=font1)
projname.pack(pady=20)
projname.place(x=50, y=15)

home.pack(fill='both', expand=1)

# Add a heading logo in the frames
area1desc = Label(home, text="Home desctiption", foreground="black", font=font1)
area1desc.pack(pady=20)
area1desc.place(x=500, y=300)

area2desc = Label(area1, text="Area 1 description?", foreground="black", font=font1)
area2desc.pack(pady=20)
area2desc.place(x=500, y=300)

area2desc = Label(area2, text="Area 2 description :O", foreground="black", font=font1)
area2desc.pack(pady=20)
area2desc.place(x=500, y=300)

area2desc = Label(area3, text="no description fuck you", foreground="black", font=font1)
area2desc.pack(pady=20)
area2desc.place(x=500, y=300)

# Add a button to switch between two frames
btn1 = Button(win, text="Home", font=font2, command=change_to_home)
btn1.pack(pady=10)
btn1.place(x=250, y=15)

btn2 = Button(win, text="Area 1", font=font2, command=change_to_area1)
btn2.pack(pady=10)
btn2.place(x=450, y=15)

btn2 = Button(win, text="Area 2", font=font2, command=change_to_area2)
btn2.pack(pady=10)
btn2.place(x=650, y=15)

btn2 = Button(win, text="Area 3", font=font2, command=change_to_area3)
btn2.pack(pady=10)
btn2.place(x=850, y=15)

win.mainloop()