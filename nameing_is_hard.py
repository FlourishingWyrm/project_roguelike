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
class dim():
    def __init__(self, root_size:float=...):
        self.frac = str(Fraction(root.winfo_screenwidth(), root.winfo_screenheight())).split("/")
        self.height = int(self.frac[1])*root_size
        self.width = int(self.frac[0])*root_size
class fix():
    def r(self,n):
        return int(round(n))
class MENU():
    def __init__(self):


        root.attributes("-fullscreen",True)
        self.photo = PhotoImage(file='/home/nate/school/long_image.png')
        self.backdrop = Label(root, image=self.photo)
        self.backdrop.place(relx=0.5, rely=0.5,anchor="center")
        self.button_list = [
            ["Play", self.loading_menu,dim(0.052).height],
            ["Menu", self.settings, dim(0.064).height],
            ["quit", root.destroy,dim(0.076).height],
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
        self.buttons[2].config(state="normal")
        self.set_list = []

        self.set_back_image = PhotoImage(file='/home/nate/school/settings.png')
        self.set_back = Label(root, image=self.set_back_image,borderwidth=0)
        self.set_back.place(relx=0.5, rely=0.5,anchor="center")
        self.set_list.append(self.set_back)

        self.set_button = [
            ["Gameplay",self.settings_gameplay,dim(0.024).height,dim(0.024).width],
            ["  Audio  ",self.settings_audio,dim(0.024).height,dim(0.0315).width],
            ["  Extra  ",self.settings_extra,dim(0.024).height,dim(0.039).width],
            ["Close",root.destroy,dim(0.05).height,dim(0.05).width]
        ]
        self.butts = []
        for butt in self.set_button:
            self.make_butt = Button(root, text=butt[0], font=("arial", 16, "bold"),fg="#FFFFFF",bg="#604330", height=fix().r(dim(0.2).height),command=butt[1],padx=fix().r(dim(1.5).width))
            self.make_butt.place(relx=butt[3], rely=butt[2],anchor="center")
            self.butts.append(self.make_butt)
            self.set_list.append(self.make_butt)
        self.settings_gameplay()
    def settings_gameplay(self):
        self.butts[1].config(state="normal")
        self.butts[2].config(state="normal")
        self.butts[0].config(state="disabled")
        self.gameplay = []
    def settings_audio(self):
        return ""
    def settings_extra(self):
        return ""
    def change_setting(self):
        return ""



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