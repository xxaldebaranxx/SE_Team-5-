from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
from tkinter import filedialog
from roofdata import *
import json
import matplotlib.pyplot as plt
import os.path
from os import path
from roof1 import get_roof1
from roof2 import get_roof2
import os

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

def xyz_wind():
    with open('output.json') as f:
        data = json.load(f)

    x=[]
    y=[]
    z=[]

    for key in data:
        if "zone" in key:
            for point in data[key]:
                x.append(point["x"])
                y.append(point["y"])
                z.append(point["z"])

    return x, y, z
        
def json_model():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x, y, z = get_xyz('data.json')

    # ax.scatter(x, y, z, c='r', marker='o')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.plot(x,y,z, color='r')
    
    plt.show()

def what_roof(file):
    if("d1.xml" in file): return 1
    else: return 2

# file uploading function and XML conversion to JSON   
def upload_file(): 
    global roofname
    f_types = [('xml Files', '*.xml')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    roofname=what_roof(filename)
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


def get_the_name_of_file():
    file = filedialog.askopenfilename(filetypes=[('xml Files', '*.xml')])
    os.path.basename(file)

    if(os.path.basename(file) == 'roof.xml'):
        get_roof1()
    else:
        get_roof2()

def json_model2():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    xa, ya, za = xyz_wind()

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    ax.scatter(xa, ya, za, color='purple', marker='o')
    x, y, z = get_xyz('data.json')
    ax.plot(x ,y ,z, color='r')
    plt.show()

    """
    d=0
    for i in range(len(x)):
        i=i+d
        a=[]
        b=[]
        c=[]
        for j in range(0, 4):
            a.append(x[i+j])
            b.append(y[i+j])
            c.append(z[i+j])
        a.append(x[i])
        b.append(y[i])
        c.append(z[i])
        d=d+3
        ax.scatter(a, b, c, color='r', marker='o')
       # ax.plot(a,b,c, color='b')
        if(i+4 >= len(x)):
                break
        """

    # plt.show()

def solar_place():
    print(roofname)
    #pingpongpingpong
    info = Label(area3, text="Placing done", foreground="black", font=font3)
    info.place(x=528, y=550)
    btn = Button(area3, text="Show current roof", font=font2, command=what_solar)
    btn.place(x=520, y=400)

def wind_zones():
    if(path.exists('data.json')):
        import windpressurezones   
        info = Label(area4, text="Calculations complete", foreground="black", font=font3)
        info.place(x=528, y=550)
        btn = Button(area4, text="Show calculated roof", font=font2, command=json_model2)
        btn.place(x=520, y=400)
    else:
        info = Label(area4, text="ERROR: you haven't converted the XML file in to JSON", foreground="black", font=font2)
        info.place(x=250, y=550)
        area4.after(1000, info.destroy)

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

btn = Button(win, text="Place Solar Pannels", font=font2, command=change_to_area3)
btn.place(x=600, y=15)

btn = Button(win, text="Calculate Wind Pressure Zones", font=font2, command=change_to_area4)
btn.place(x=850, y=15)

filebtn = Button(area1, text='Upload File', width=20,command = upload_file, font=font2)
filebtn.place(x=500, y=300) 

windbtn = Button(area4, text='Calculate', width=25,command = wind_zones, font = font2)
windbtn.place(x=450, y=250) 

placebtn = Button(area3, text = 'Place', width = 25, font = font2,command = get_the_name_of_file)
placebtn.place(x=450, y=250)
win.mainloop()