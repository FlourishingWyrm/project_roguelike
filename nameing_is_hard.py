from tkinter import *
import time
import math
from functools import partial
import random
import os
from PIL import Image
from fractions import Fraction
# future move list
moves = [
    [10,0,"fisticuffs","attack",10,"doubles next action"],
    [10,30,"psychic","mental",1,"perplexed"],
    []
]
# potential use for dictonary
name_search={
    "tense":0,
    "mind ray":1,

}


if not os.path.exists("{}.txt".format("game_data")):
    # creates a file if the file doesn't exist so no additional installs are required
    text_file = open("{}.txt".format("game_data"), "w+")
    # varibles stored in the game data
    presets = ("presetsettings = [1,2,4,6,8,10,11,13,15]\n" #
               "active_game = 'no'\n"
               "players_unlocked = []\n"
               "invintory = []\n"
               "current_moves = []\n"
               "")
    text = str(presets)
    # removes the quotes for the code to run
    text = text.strip("")
    open("game_data.txt", "w+").write(text)
# place variables here
presetsettings = []
active_game = ""
players_unlocked = []
invintory = []
current_moves = []
start = 900
might = start
mighty = 750
grid = []
for five in range(25):
    if might == 1100:
        might = start
        mighty += 50
    else:
        might+= 50
    grid.append([might, mighty])
font = ("arial", 16, "bold")
# https://stackoverflow.com/questions/4719438/editing-specific-line-in-text-file-in-python
with open('game_data.txt') as f:
    # seperates the code by lines and removes the spaces
    para_list = [i.strip() for i in f.readlines()]
    for para in para_list:
        # sets all the variables
        exec(para)
class dim():
    """this is used to convert numbers so the screen is constant regardless of resolution"""
    def __init__(self, root_size:float=...):
        try:
            self.frac = str(Fraction(root.winfo_screenwidth(), root.winfo_screenheight())).split("/")
            self.height = int(self.frac[1])*root_size
            self.width = int(self.frac[0])*root_size
        except TclError:
            # avoids a error message that occurs when the game is ended
            print("game closed successfully")
            quit()
class fix():
    """rounding"""
    def r(self,n):
        return int(round(n))
def start_drag(event):
    global des
    # Store the initial position of the widget when dragging starts
    event.widget.startX = event.x  # Store initial X position
    event.widget.startY = event.y  # Store initial Y position
    options = [[0,0],[50,0],[50,50],[0,50],[-50,0],[0,-50],[-50,-50],[-50,50],[50,-50]]
    des = []
    for i in options:
        rat = [event.widget.winfo_x() + i[0], event.widget.winfo_y() + i[1]]
        print(rat)
        if rat in grid:
            des.append(rat)



clock = 0
widget = ""
drop = [0, 0]
def on_drag(event):
    global clock,widget,drop
    clock +=1
    # Update widget position as it's dragged
    widget = event.widget  # Get reference to the dragged widget

    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    most = 100000000000000000000000

    for i in des:
        print(des)
        if sum(i)-(x+y)<most:
            most = sum(i)-(x+y)
            drop = i
    widget.place(x=x, y=y)  # Move the widget
    print(clock)
    print(x,y)
    clock-=1
    widget.bind("<ButtonRelease-1>", snap)
def snap(event):
    print(grid)
    widget = event.widget  # Get reference to the dragged widget

    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    most = 10000000000000000000000000000000000000000

    for i in des:
        print(des,[x,y])
        if math.sqrt(((i[0]-x)*(i[1]-y))+((i[1]-y)*(i[1]-y)))< most:
            most = math.sqrt(((i[0]-x)*(i[1]-y))+((i[1]-y)*(i[1]-y)))
            drop = i
    print(most,"hiee")
    widget.place(x=drop[0], y=drop[1])
class MENU():
    def __init__(self):

        self.buttons = []
        # makes the screen full
        root.attributes("-fullscreen",True)
        # gets the background image
        self.photo = PhotoImage(file='long_image.png')
        # puts the background image
        self.backdrop = Label(root, image=self.photo)
        self.backdrop.place(relx=0.5, rely=0.5,anchor="center")
        # instates a button list
        self.button_list = [
            ["Play", self.loading_menu,dim(0.052).height],
            ["Menu", self.settings, dim(0.064).height],
            ["Quit", root.destroy,dim(0.076).height],
        ]

        for item in self.button_list:
            # creates the startmenu options
            self.button_make = Button(root, text=item[0],font=font, fg="#FFFFFF",bg="#0057D8",width=fix().r(dim(2.5).width), height=fix().r(dim(0.22).height), command=item[1])
            self.button_make.place(relx=0.5, rely=item[2],anchor="center")
            self.buttons.append(self.button_make)
    def loading_menu(self):
        # sets up the clear of all things on the menu
        self.backdrop.destroy()
        for item in self.buttons:
            item.destroy()
        if presetsettings[6] == 13:
            Loading()
        else:
            map()
    def settings(self):
        settings("menu")
class settings():
    def __init__(self,type,bar=[]):
        self.presetsettings = presetsettings
        self.set_list = []
        self.bar=bar
        for i in self.bar:
            i.config(state="disabled")
        self.set_back_image = PhotoImage(file='setting.png')
        self.set_back = Label(root, image=self.set_back_image,borderwidth=0)
        self.set_back.place(relx=0.5, rely=0.5,anchor="center")
        self.set_list.append(self.set_back)

        self.set_button = [
            ["Gameplay",lambda : self.clear_settings_options(0),dim(0.024).height,dim(0.024).width],
            ["  Audio  ",lambda :self.clear_settings_options(1),dim(0.024).height,dim(0.0315).width],
            ["  Extra  ",lambda :self.clear_settings_options(2),dim(0.024).height,dim(0.039).width],
            ["Close",self.un_setting,dim(0.09).height,dim(0.0402).width]
        ]
        if type == "game":
            # gives a quit to title screen option for in game settings
            self.set_button.append(["Main Menu",lambda :MENU(),dim(0.09).height,dim(0.0235).width])
        self.butts = []
        # adds the tab settings buttons to a list and places them
        for butt in self.set_button:
            self.make_butt = Button(root, text=butt[0], font=font,fg="#FFFFFF",bg="#604330", height=fix().r(dim(0.2).height),command=butt[1],padx=fix().r(dim(1.5).width))
            self.make_butt.place(relx=butt[3], rely=butt[2],anchor="center")
            self.butts.append(self.make_butt)
            self.set_list.append(self.make_butt)
        self.current_set_tab = []
        self.clear_settings_options(0)
        if type == "game":
            # makes the menu button close the menu if the menu is open in the game section
            self.make_butt = Button(bg="#604330", width=fix().r(dim(0.6).width), height=fix().r(dim(0.6).height),command=lambda: self.un_setting())
            self.make_butt.place(relx=dim(0.0025).width, rely=dim(0.009).height, anchor="center")
            self.set_list.append(self.make_butt)
    def clear_settings_options(self,tab):
        # removes all things in the current display menu
        for item in self.current_set_tab:
            item.destroy()
        for item in self.butts:
            if item == self.butts[tab]:
                # disables the current tab
                self.butts[tab].config(state="disabled")
            else:
                item.config(state="normal")
        for item in [
            ["Battle Animations                           ", 0, 0.9, dim(0.045).height, self.presetsettings[0]],
            ["Auto End Turn                               ", 2, 2.5, dim(0.065).height, self.presetsettings[1]],
            ["New Games Start With A Tutorial             ", 4.3, 4.9, dim(0.085).height, self.presetsettings[2]],
            ["All Sound                                   ", 6.3, 6.9, dim(0.045).height, self.presetsettings[3]],
            ["Player Sounds                               ", 8.3, 8.9, dim(0.065).height, self.presetsettings[4]],
            ["Music                                       ", 10.3, 10.9, dim(0.085).height, self.presetsettings[5]],
            ["Loading Screens                             ", 12.3, 12.9, dim(0.045).height, self.presetsettings[6]],
            ["Credits                                     ", 14.3, 14.9, dim(0.065).height, self.presetsettings[7]],
            ["Reset Settings                              ", 16.3, 16.9, dim(0.085).height, self.presetsettings[8]]
        ][tab*3:tab*3+3]:
            # takes the current items in the tab and displays them
            self.current_set_tab_option = Scale(root, from_=item[1], to=item[2], orient="horizontal", showvalue=False,
                                                command=self.change_setting, variable=IntVar(value=item[4]))
            self.current_set_tab_option.place(relx=0.6, rely=item[3], anchor="center")
            self.current_set_tab_option_text = Label(text=item[0], font=font, fg="#FFFFFF",
                                                     bg="#754525", justify="left")
            self.current_set_tab_option_text.place(relx=0.45, rely=item[3], anchor="center", )
            self.current_set_tab.append(self.current_set_tab_option)
            self.current_set_tab.append(self.current_set_tab_option_text)
        for item in self.current_set_tab:
            self.set_list.append(item)
    def change_setting(self,change):
        # edits the setting and writes the edit to file
        source = round(float(change)/2.1)
        change = int(change)
        with open('game_data.txt', 'r') as file:
            # read a list of lines into data
            data = file.readlines()
        if source == 8:
            self.presetsettings = [1,2,5,7,9,11,13,14,16]
            self.clear_settings_options(2)
            # and write everything back
        else :
            self.presetsettings[source] = change
        data[0] = "presetsettings = " + str(self.presetsettings) + "\n"
        with open('game_data.txt', 'w') as file:
            file.writelines(data)

    def un_setting(self):
        # closes the menu
        for i in self.bar:
            i.config(state="normal")
        for item in self.set_list:
            item.destroy()




class Loading():
    """loading bar"""
    # credit to https://devhubcommunity.hashnode.dev/displaying-gifs-in-tkinter-python?__cf_chl_f_tk=rY.jHPCFPHRvxYg1Pxc0gYmI8mk0.291TAYfHCYhAJQ-1771967830-1.0.1.1-Bx3kTWEOHwG7G9vLJ13no9jxQB2aVjFjpnvr0UuJ9W8
    # and https://www.geeksforgeeks.org/python/how-to-use-images-as-backgrounds-in-tkinter/
    def __init__(self):
        # gets the file for the background of the gif
        self.photo = PhotoImage(file="bar.gif")
        # defines the canvas and its background
        self.canvas = Canvas(root, width=dim(120).width, height=dim(120).height,bg="#262626")
        self.canvas.pack(fill="both", expand=True)


        # learns about the length of the gif
        self.info = Image.open('bar.gif')
        # sets the frames
        self.frames = self.info.n_frames
        self.photoimage_objects = []
        # stores the invidual frames
        # starts the animation
        self.frames-=1
        self.animation(1)
        root.mainloop()
    def animation(self,current_frame=0):
        global loop
        self.image = PhotoImage(file='bar.gif', format=f'gif -index {current_frame}')
        # reprints background and then foreground overtop
        self.canvas.create_image(950, 860, image=self.photo)
        self.canvas.create_image(950, 860, image=self.image)
        # increments the frame
        current_frame = current_frame + 1

        if current_frame == self.frames:
            self.canvas.destroy()
            # loads the map
            map()
            root.mainloop()


        loop = root.after(random.randint(60, 150), lambda: self.animation(current_frame))

class map():
    # will allow players to select options for the story
    def __init__(self):
        self.canvas = Canvas(root, width=dim(120).width, height=dim(120).height, bg="#262626")
        self.canvas.pack(fill="both", expand=True)
        # temparary load button
        self.level_load_button = Button(root,text="Battle",font=font, fg="#FFFFFF",bg="#0057D8",width=fix().r(dim(2.5).width), height=fix().r(dim(0.22).height), command=lambda: self.load_level())
        self.level_load_button.place(relx=0.5,rely=0.5,anchor="center")
    def load_level(self):
        # preps the level
        self.canvas.destroy()
        self.level_load_button.destroy()
        load_level()
        menu_bar()
class load_level():
    def __init__(self):
        # the level
        self.canvas = Canvas(root, width=dim(120).width, height=dim(120).height, bg="#262626")
        self.canvas.pack(fill="both", expand=True)
class menu_bar():
    # a bar for the menu
    def __init__(self):

        self.canvas = Canvas(root, width=dim(120).width, height=180, bg="#754525")
        self.canvas.pack(fill="both")
        self.menu_bar = Label(bg="#754525",width=dim(120).width,height=fix().r(dim(0.75).height))
        self.menu_bar.place(relx=0.5, rely=dim(0.009).height, anchor="center")
        self.menu_button = Button(bg="#604330",width=fix().r(dim(0.6).width),height=fix().r(dim(0.6).height),command=lambda: settings("game",self.menubar_list))
        self.menu_button.place(relx=dim(0.0025).width, rely=dim(0.009).height, anchor="center")
        self.invintory = Button(bg="#604330", width=fix().r(dim(0.009).width), height=fix().r(dim(0.6).height),command=lambda: magic())#invintory(self.menubar_list)
        self.invintory.place(relx=dim(0.05).width, rely=dim(0.01).height, anchor="center")
        self.menubar_list = [self.menu_button, self.invintory,self.canvas]
# not done
class invintory():
    def __init__(self,bar):
        self.bar = bar
        for i in self.bar:
            i.config(state="disabled")
        self.canvas = Canvas(root, width=dim(120).width, height=180, bg="#FFFFFF")
        self.canvas.pack(fill="both", expand=True)
        self.invintory = PhotoImage(file='invintory.png')
        self.set = Label(root, image=self.invintory,borderwidth=0)
        self.set.place(relx=0.5, rely=0.5, anchor="center")
        self.exit = Button(root, text="Close",command=lambda :self.go())
        self.exit.place(relx=dim(0.0402).width, rely=dim(0.093).height, anchor="center")
        self.end = [self.set, self.exit, self.canvas,]

        root.mainloop()
# not done /////////////////////////////\\\\\\\\\\\\\\/\/\/\\\\\\\\\\\\\\\\\////////////////////////////////////
    def go(self):
        for i in self.end:
            i.destroy()
        for i in self.bar:
            i.config(state="normal")
class magic():
    def __init__(self):
        start = 900
        might = start
        mighty = 750
        grid = []
        for five in range(25):
            label = Label(root, bg=f"#{str(random.randint(100000,999999))}", height=2, width=4,padx=0, pady=0)
            label.place(x=might, y=mighty,)  # Place the label at initial position
            grid.append([might, mighty])
            if might == 1100:
                might = start
                mighty += 50
            else:
                might+= 50

        # Bind mouse events to the label for dragging functionality
            label.bind("<ButtonPress-1>", start_drag)  # Detect mouse press to start dragging
            label.bind("<B1-Motion>", on_drag)  # Move label while dragging
    def relocate(self, event):
        print(self.canvas.winfo_pointerxy())
        x0, y0 = self.canvas.winfo_pointerxy()
        x0 -= self.canvas.winfo_rootx()
        y0 -= self.canvas.winfo_rooty()
        self.canvas.coords(self.id_cLabel, x0, y0)



if __name__ == '__main__':
    """who knows what this does"""
    root = Tk()
    root.title("Colour Quest")
    MENU()
    root.mainloop()
# settings
a = [
["Skip battle animations                      ", 0, 0.9, dim(0.04).height],
["Auto end turn                               ", 2, 2.5, dim(0.06).height],
["New games start with a tutorial             ", 4.3, 4.9, dim(0.08).height],
["All Sound                                   ", 6.3, 6.9, dim(0.04).height],
["Player Sounds                               ", 8.3, 8.9, dim(0.06).height],
["Music                                       ", 10.3, 10.9, dim(0.08).height],
["Disable Loading Screens                     ", 6.3, 6.9, dim(0.04).height],
["Credits                                     ", 8.3, 8.9, dim(0.06).height],
["Music                                       ", 10.3, 10.9, dim(0.08).height]
]