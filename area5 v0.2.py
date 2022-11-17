import tkinter as tk
from tkinter import *

# setting parameters for main menu
main_menu = tk.Tk()
main_menu.title("SPPT Application")
main_menu.geometry("1280x720")
main_menu.resizable(False, False)

# placing labels and buttons
label = tk.Label(main_menu, text='SPPT', font=("Montserrat", 25, 'bold'))
label['foreground'] = '#445964'
label.place(x=20, y=10)


def openNewWindow():
    main_menu.withdraw()
    newWindow = Toplevel(label)
    newWindow.title("Main menu")
    newWindow.geometry("200x200")
    Label(newWindow, text="Main menu").pack()

#def  replace_window(root):
#    global current_window
#   if current_window is not None:
#       current_window.destroy()
#   current_window = tk.Toplevel(root)
#   current_window.wm_protocol("WM_DELETE_WINDOW", root.destroy)
#
#   return current_window

#buttonHome = replace_window(root)
buttonHome = Button(main_menu, text = 'Home', font=("Montserrat", 15, 'bold'), command = openNewWindow)
buttonHome['foreground'] = '#263138'
buttonHome.place(x=200, y=15)

#func to open Area 1 window
def openWindowAreaOne():
    main_menu.withdraw()
    AreaOneWindow = Toplevel(main_menu)
    AreaOneWindow.title("SPPT Application")
    AreaOneWindow.geometry("1280x720")

buttonAreaOne = Button(main_menu, text = 'Area 1', font=("Montserrat", 15, 'bold'), command = openWindowAreaOne)
buttonAreaOne['foreground'] = '#445964'
buttonAreaOne.place(x=380, y=15)
# buttonAreaOne.pack()

buttonAreaTwo = Button(main_menu, text = 'Area 2', font=("Montserrat", 15, 'bold') )
buttonAreaTwo['foreground'] = '#445964'
buttonAreaTwo.place(x=560, y=15)

buttonAreaThree = Button(main_menu, text = 'Area 3', font=("Montserrat", 15, 'bold') )
buttonAreaThree['foreground'] = '#445964'
buttonAreaThree.place(x=740, y=15)

main_menu.mainloop()