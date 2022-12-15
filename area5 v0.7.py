from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
from tkinter import filedialog
from roofdata import *
import json
import matplotlib.pyplot as plt

win = Tk()
win.geometry("1280x720")
win.resizable(False, False)
win.title("SPPT Application")
win.config(bg='white')

# Create tabs in the window
background = Frame(win)
home = Frame(win)
area1 = Frame(win)
area3 = Frame(win)
area4 = Frame(win)
area5 = Frame(win)

img=Image.open('ajaj.jpg')
img2=img.resize((1300,800))
img2=ImageTk.PhotoImage(img2)

def labelfunc(area):
    label = Label(area, image=img2)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.pack()

labelfunc(home)
labelfunc(area1)
labelfunc(area3)
labelfunc(area4)

img3=Image.open('house.jpg')
img3=img3.resize((500, 250))
img3=ImageTk.PhotoImage(img3)
label5 = Button(home,image=img3) 
label5.place(x=100, y=250)


# Functions for switching between tabs
def change_to_home():
    home.pack(fill='both', expand=1)
    area1.pack_forget()
    area3.pack_forget()
    area4.pack_forget()

def change_to_area1():
    area1.pack(fill='both', expand=1)
    area3.pack_forget()
    home.pack_forget()
    area4.pack_forget()

def change_to_area3():
    area3.pack(fill='both', expand=1)
    area1.pack_forget()
    home.pack_forget()
    area4.pack_forget()
   
def change_to_area4():
    area4.pack(fill='both', expand=1)
    area1.pack_forget()
    area3.pack_forget()
    home.pack_forget()
   
def get_xyz(link):
    with open(link) as f:
        templates = json.load(f)

    x=[]
    y=[]
    z=[]

    for key, value in templates.items():
        for i in value:
            a = i["POLYGON"]["@path"]
            for j_key, j_value in a.items():
                for k_key, k_value in j_value.items():
                    if "C" in k_key:
                        x.append(k_value["X"])
                        y.append(k_value["Y"])
                        z.append(k_value["Z"])
    #print(x)
    #print(y)
    #print(z)
    return x, y, z

def json_model():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x, y, z = get_xyz('data.json')

    ax.scatter(x, y, z, c='r', marker='o')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.plot(x,y,z, color='r')
    plt.show()

# file uploading function and XML conversion to JSON   
def upload_file(): 
    f_types = [('xml Files', '*.xml')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    if(cf(filename) == "False"):
        info = Label(area1, text="ERROR: this file format is not accepted", foreground="black", font=font1)
        descriptions.place(x=500, y=500)
    else: 
        erd(xtj(filename))
        info = Label(area1, text="Conversion complete", foreground="black", font=font3)
        info.place(x=528, y=550)
        area1.after(1200, info.destroy)
        btn = Button(area1, text="Show converted roof", font=font2, command=json_model)
        btn.place(x=520, y=400)
    
# temp function for dropdown menus
def temp_dropdown_func():
    label1.config( text = roofset1.get() )
    label2.config( text = roofset2.get() )
    label3.config( text = roofset3.get() )

def wind_zones():
    info = Label(area4, text="There is no code for calculating wind pressure zones.. yet", foreground="black", font=font2)
    info.place(x=250, y=550)
   # if(cf("data.json") == "True"):
       # import windpressurezones    
       # info = Label(area4, text="Calculations complete", foreground="black", font=font3)
       # info.place(x=528, y=550)
    #else:
       # info = Label(area4, text="ERROR: you haven't converted the XML file in to JSON", foreground="black", font=font2)
       # info.place(x=250, y=550)
       # area4.after(1000, info.destroy)

# Custom fonts (why not)
#dd changed fonts
font1 = font.Font(family='Montserrat', size='22', weight='bold')
font2 = font.Font(family='Montserrat', size='12')
font3 = font.Font(family='Montserrat', size='14', weight='bold')

#dd colour of title and line
projname = Label(win, text="SPPT", foreground="grey", font=font1)
projname.place(x=50, y=13)

line =Frame(win, bg='light grey', height=2,width=2000)
line.place(x=0, y=57)

home.pack(fill='both', expand=1)

# Each area descriptions
descriptions = Label(home, text="SPPT is a simple solar panels placement tool, that was designed and created by 2nd year Vilnius University students. It allows you to upload the file with the coordinates of the roof and solar panels and get a 3D model of it, as well as calculate wind pressure zones. ", foreground="black", font=font2, justify="center", wraplength=420) # home desc
descriptions.place(x=620, y=320)
descriptions = Label(area1, text="Team #1 task was to implement logic that takes a 3D model XML file produced by RoofOrders company, read it, and extract the information needed in the further solar system design process steps.", foreground="black", font=font2, wraplength=420, justify="center") # area1 desc
descriptions.place(x=400, y=150)
# descriptions = Label(area1, text="Upload an XML file below", foreground="black", font=font3, wraplength=420, justify="center" ) # area1 desc
# descriptions.place(x=500, y=250)
descriptions = Label(area3, text="Team #3 task was to creates an addition to the main system which will optimize the placement of solar panels on our customer's roof by following requirements specified by the manufacturer of said panels", foreground="black", font=font2, wraplength=420, justify="center") # area3 desc
descriptions.place(x=400, y=150)
descriptions = Label(area4, text="Team #4 task was to determine the exact areas for each wind pressure zone on a given roof face", foreground="black", font=font2, wraplength=420, justify="center") # area4 desc
descriptions.place(x=400, y=150)

# Buttons of each tabs
#dd changed buttons names 
btn = Button(win, text="Home", font=font2, command=change_to_home)
btn.place(x=250, y=15)

btn = Button(win, text="Upload a File", font=font2, command=change_to_area1)
btn.place(x=400, y=15)

btn = Button(win, text="Select Components", font=font2, command=change_to_area3)
btn.place(x=600, y=15)

btn = Button(win, text="Calculate Wind Pressure Zones", font=font2, command=change_to_area4)
btn.place(x=850, y=15)

filebtn = Button(area1, text='Upload File', width=20,command = upload_file, font=font2)
filebtn.place(x=500, y=300) 

windbtn = Button(area4, text='Calculate', width=25,command = wind_zones, font = font2)
windbtn.place(x=450, y=250) 

# Dropdown menu options
options = [
    "Roof Face",
    "Solar Panels",
    "Wind Pressure Zones",
    "Wind Zone Calculation"
]

# Roof labels
rooflabel1 = Label(area3 , text = "Roof #1", font=font2)
rooflabel1.place(x=300, y=450)

rooflabel2 = Label(area3 , text = "Roof #2",font=font2)
rooflabel2.place(x=500, y=450)

rooflabel3 = Label(area3 , text = "Roof #3",font=font2)
rooflabel3.place(x=700, y=450)

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
dropdownBtn = Button(area3 , text = "Click_me" , command = temp_dropdown_func, font=font2 )
dropdownBtn.place(x=570, y=600)
  
# Create Labels (temp function, might not be needed)
label1 = Label(area3 , text = " " )
label1.place(x=300, y=550)

label2 = Label(area3 , text = " " )
label2.place(x=500, y=550)

label3 = Label(area3 , text = " " )
label3.place(x=700, y=550)

win.mainloop()