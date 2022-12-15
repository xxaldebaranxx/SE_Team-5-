from tkinter import *
from tkinter import font
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from roofdata import *
import os.path


win = Tk()
win.geometry("1280x720")
win.resizable(False, False)
win.title("SPPT Application")

# Create tabs in the window
home = Frame(win)
area1 = Frame(win)
area3 = Frame(win)
area4 = Frame(win)
area5 = Frame(win)

# Functions for switching between tabs
def change_to_home():
    home.pack(fill='both', expand=1)
    area1.pack_forget()
    area5.pack_forget()
    area3.pack_forget()
    area4.pack_forget()

def change_to_area1():
    area1.pack(fill='both', expand=1)
    area5.pack_forget()
    area3.pack_forget()
    home.pack_forget()
    area4.pack_forget()

def change_to_area3():
    area3.pack(fill='both', expand=1)
    area1.pack_forget()
    area5.pack_forget()
    home.pack_forget()
    area4.pack_forget()
   
def change_to_area4():
    area4.pack(fill='both', expand=1)
    area1.pack_forget()
    area3.pack_forget()
    home.pack_forget()
    area5.pack_forget()

def change_to_area5():
    area5.pack(fill='both', expand=1)
    area1.pack_forget()
    area4.pack_forget()
    home.pack_forget()
    area3.pack_forget()
   
# file uploading function and XML conversion to JSON   
xml2json = int(0)
def upload_file(): 
    f_types = [('xml Files', '*.xml')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    if(cf(filename) == "False"):
        info = Label(area1, text="ERROR: this file format is not accepted", foreground="black", font=font1)
        descriptions.place(x=250, y=550)
    else: 
        erd(xtj(filename))
        info = Label(area1, text="Conversion complete", foreground="black", font=font3)
        info.place(x=528, y=550)
    
# temp function for dropdown menus
def temp_dropdown_func():
    label1.config( text = roofset1.get() )
    label2.config( text = roofset2.get() )
    label3.config( text = roofset3.get() )

def wind_zones():
    if(os.path.isfile("data.json")):
        import windpressurezones    
        info = Label(area4, text="Calculations complete", foreground="black", font=font3)
        info.place(x=528, y=550)
    else:
        info = Label(area4, text="ERROR: you haven't converted the XML file in to JSON", foreground="black", font=font1)
        info.place(x=250, y=550)
        area4.after(1000, info.destroy)

# Custom fonts (why not)
font1 = font.Font(family='Georgia', size='22', weight='bold')
font2 = font.Font(family='Aerial', size='12')
font3 = font.Font(family='Aerial', size='14', weight='bold')


projname = Label(win, text="SPPT", foreground="teal", font=font1)
projname.place(x=50, y=13)

line =Frame(win, bg='black', height=2,width=2000)
line.place(x=0, y=57)

home.pack(fill='both', expand=1)

# Each area descriptions
descriptions = Label(home, text="Home desctiption", foreground="black", font=font1) # home desc
descriptions.place(x=500, y=300)
descriptions = Label(area1, text="Area 1: takes a 3D model XML file produced by RoofOrders company and converts it in to a JSON file", foreground="black", font=font1, wraplength=420, justify="center") # area1 desc
descriptions.place(x=427, y=300)
descriptions = Label(area1, text="Upload an XML file below", foreground="black", font=font2) # area1 desc
descriptions.place(x=535, y=550)
descriptions = Label(area3, text="Area 3: creates an addition to the main system which will optimize the placement of solar panels on our customer's roof by following requirements specified by the manufacturer of said panels", foreground="black", font=font1, wraplength=500, justify="center") # area3 desc
descriptions.place(x=400, y=220)
descriptions = Label(area4, text="Area 4: determines the exact areas for each wind pressure zone on a given roof face", foreground="black", font=font1, wraplength=420, justify="center") # area4 desc
descriptions.place(x=450, y=300)
descriptions = Label(area5, text="Area 5 description", foreground="black", font=font1, wraplength=420, justify="center") # area5 desc
descriptions.place(x=500, y=300)

# Buttons of each tabs
btn = Button(win, text="Home", font=font2, command=change_to_home)
btn.place(x=250, y=15)

btn = Button(win, text="Area 1", font=font2, command=change_to_area1)
btn.place(x=450, y=15)

btn = Button(win, text="Area 3", font=font2, command=change_to_area3)
btn.place(x=650, y=15)

btn = Button(win, text="Area 4", font=font2, command=change_to_area4)
btn.place(x=850, y=15)

btn = Button(win, text="Area 5", font=font2, command=change_to_area5)
btn.place(x=1050, y=15)

filebtn = Button(area1, text='Upload File', width=20,command = upload_file)
filebtn.place(x=550, y=600) 

windbtn = Button(area4, text='Calculate wind pressure zones', width=25,command = wind_zones)
windbtn.place(x=545, y=600) 

# Dropdown menu options
options = [
    "Roof Face",
    "Solar Panels",
    "Wind Pressure Zones",
    "Wind Zone Calculation"
]

# Roof labels
rooflabel1 = Label(area3 , text = "Roof #1")
rooflabel1.place(x=300, y=480)

rooflabel2 = Label(area3 , text = "Roof #2")
rooflabel2.place(x=500, y=480)

rooflabel3 = Label(area3 , text = "Roof #3")
rooflabel3.place(x=700, y=480)

# Datatype of menus text
roofset1 = StringVar()
roofset2 = StringVar()
roofset3 = StringVar()

# Initial menus text
roofset1.set( "Select a Component" )
roofset2.set( "Select a Component" )
roofset3.set( "Select a Component" )
  
# Create Dropdown menus
dropRoof1 = OptionMenu(area3 , roofset1 , *options )
dropRoof1.place(x=300, y=500)

dropRoof2 = OptionMenu(area3 , roofset2 , *options )
dropRoof2.place(x=500, y=500)

dropRoof3 = OptionMenu(area3 , roofset3 , *options )
dropRoof3.place(x=700, y=500)
  
# Create button, it will change labels text (labels text is for the temp function)
dropdownBtn = Button(area3 , text = "Click me" , command = temp_dropdown_func )
dropdownBtn.place(x=570, y=600)
  
# Create Labels (temp function, might not be needed)
label1 = Label(area3 , text = " " )
label1.place(x=300, y=550)

label2 = Label(area3 , text = " " )
label2.place(x=500, y=550)

label3 = Label(area3 , text = " " )
label3.place(x=700, y=550)

win.mainloop()