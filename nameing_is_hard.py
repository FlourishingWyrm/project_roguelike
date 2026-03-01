from tkinter import *
import time
import random
from venv import create
from PIL import Image
from fractions import Fraction
moves = [
    [10,0,"fisticuffs","attack",10,"doubles next action"],
    [10,30,"psychic","mental",1,"perplexed"],
    []
]
name_search={
    "tense":0,
    "mind ray":1,

}
import os

if not os.path.exists("{}.txt".format("game_data")):
    text_file = open("{}.txt".format("game_data"), "w+")

    presets = ("presetsettings = [1,2,4,6,8,10,11,13,15]\n" #
               "active_game = 'no'\n"
               "players_unlocked = []\n"
               "invintory = []\n"
               "current_moves = []\n"
               "")
    text = str(presets)
    text = text.strip("")
    open("game_data.txt", "w+").write(text)
# place variables here
presetsettings = []
active_game = ""
players_unlocked = []
invintory = []
current_moves = []
# https://stackoverflow.com/questions/4719438/editing-specific-line-in-text-file-in-python
with open('game_data.txt') as f:
    para_list = [i.strip() for i in f.readlines()]
    for para in para_list:
        exec(para)
class dim():
    def __init__(self, root_size:float=...):
        try:
            self.frac = str(Fraction(root.winfo_screenwidth(), root.winfo_screenheight())).split("/")
            self.height = int(self.frac[1])*root_size
            self.width = int(self.frac[0])*root_size
        except TclError:
            print("game closed successfully")
            quit()
class fix():
    def r(self,n):
        return int(round(n))
class MENU():
    def __init__(self):
        global presetsettings

        root.attributes("-fullscreen",True)
        self.presetsettings = presetsettings
        self.photo = PhotoImage(file='/home/nate/school/long_image.png')
        self.backdrop = Label(root, image=self.photo)
        self.backdrop.place(relx=0.5, rely=0.5,anchor="center")
        self.button_list = [
            ["Play", self.loading_menu,dim(0.052).height],
            ["Menu", self.settings, dim(0.064).height],
            ["Quit", root.destroy,dim(0.076).height],
        ]
        self.buttons = []
        print(int(round(dim(2.5).width,0)))
        for item in self.button_list:
            self.button_make = Button(root, text=item[0],font=("arial", 16, "bold"), fg="#FFFFFF",bg="#0057D8",width=fix().r(dim(2.5).width), height=fix().r(dim(0.22).height), command=item[1])
            self.button_make.place(relx=0.5, rely=item[2],anchor="center")
            self.buttons.append(self.button_make)
    def loading_menu(self):
        self.backdrop.destroy()
        for item in self.buttons:
            item.destroy()
        Loading()
    def settings(self):
        for i in self.buttons:
            i.config(state="disabled")
        self.set_list = []

        self.set_back_image = PhotoImage(file='/home/nate/school/setting.png')
        self.set_back = Label(root, image=self.set_back_image,borderwidth=0)
        self.set_back.place(relx=0.5, rely=0.5,anchor="center")
        self.set_list.append(self.set_back)

        self.set_button = [
            ["Gameplay",lambda : self.clear_settings_options(0),dim(0.024).height,dim(0.024).width],
            ["  Audio  ",lambda :self.clear_settings_options(1),dim(0.024).height,dim(0.0315).width],
            ["  Extra  ",lambda :self.clear_settings_options(2),dim(0.024).height,dim(0.039).width],
            ["Close",self.un_setting,dim(0.05).height,dim(0.05).width]
        ]
        self.butts = []
        for butt in self.set_button:
            self.make_butt = Button(root, text=butt[0], font=("arial", 16, "bold"),fg="#FFFFFF",bg="#604330", height=fix().r(dim(0.2).height),command=butt[1],padx=fix().r(dim(1.5).width))
            self.make_butt.place(relx=butt[3], rely=butt[2],anchor="center")
            self.butts.append(self.make_butt)
            self.set_list.append(self.make_butt)
        self.current_set_tab = []
        self.clear_settings_options(0)
    def clear_settings_options(self,tab):
        for item in self.current_set_tab:
            item.destroy()
        for item in self.butts:
            if item == self.butts[tab]:
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
            self.current_set_tab_option = Scale(root, from_=item[1], to=item[2], orient="horizontal", showvalue=False,
                                                command=self.change_setting, variable=IntVar(value=item[4]))
            self.current_set_tab_option.place(relx=0.6, rely=item[3], anchor="center")
            self.current_set_tab_option_text = Label(text=item[0], font=("arial", 16, "bold"), fg="#FFFFFF",
                                                     bg="#754525", justify="left")
            self.current_set_tab_option_text.place(relx=0.45, rely=item[3], anchor="center", )
            self.current_set_tab.append(self.current_set_tab_option)
            self.current_set_tab.append(self.current_set_tab_option_text)
        for item in self.current_set_tab:
            self.set_list.append(item)
    def change_setting(self,change):
        source = round(float(change)/2.1)
        change = int(change)
        print(source)
        print(change)
        with open('game_data.txt', 'r') as file:
            # read a list of lines into data
            data = file.readlines()
        if source == 8:
            self.presetsettings = [1,2,5,7,9,11,13,14,16]
            print(self.presetsettings)
            self.clear_settings_options(2)
            # and write everything back
        else :
            self.presetsettings[source] = change
        data[0] = "presetsettings = " + str(self.presetsettings) + "\n"
        with open('game_data.txt', 'w') as file:
            file.writelines(data)

    def un_setting(self):
        for item in self.set_list:
            item.destroy()
        for i in self.buttons:
            i.config(state="normal")



class Loading():
    """loading bar"""
    # credit to https://devhubcommunity.hashnode.dev/displaying-gifs-in-tkinter-python?__cf_chl_f_tk=rY.jHPCFPHRvxYg1Pxc0gYmI8mk0.291TAYfHCYhAJQ-1771967830-1.0.1.1-Bx3kTWEOHwG7G9vLJ13no9jxQB2aVjFjpnvr0UuJ9W8
    # and https://www.geeksforgeeks.org/python/how-to-use-images-as-backgrounds-in-tkinter/
    def __init__(self):
        # gets the file for the background of the gif
        self.photo = PhotoImage(file="bar.gif")
        # defines the canvas and its background
        self.canvas = Canvas(root, width=1920, height=1080,bg="#262626")
        self.canvas.pack(fill="both", expand=True)


        # learns about the length of the gif
        self.info = Image.open('/home/nate/school/bar.gif')
        # sets the frames
        self.frames = self.info.n_frames
        print(self.frames)
        self.photoimage_objects = []
        # stores the invidual frames
        # starts the animation
        self.frames-=1
        print(self.frames)
        self.animation(1)
        root.mainloop()
    def animation(self,current_frame=0):
        global loop
        self.image = PhotoImage(file='/home/nate/school/bar.gif', format=f'gif -index {current_frame}')
        print(current_frame)
        # reprints background and then foreground overtop
        self.canvas.create_image(950, 860, image=self.photo)
        self.canvas.create_image(950, 860, image=self.image)
        # increments the frame
        current_frame = current_frame + 1

        if current_frame == self.frames:
            self.canvas.destroy()
            startgame()
            root.mainloop()


        loop = root.after(random.randint(60, 150), lambda: self.animation(current_frame))

class startgame():
    def __init__(self):
        self.frame = Frame(padx=0, pady=0)

if __name__ == '__main__':
    """who knows what this does"""
    root = Tk()
    root.title("Colour Quest")
    MENU()
    root.mainloop()
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