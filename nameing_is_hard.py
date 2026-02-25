from tkinter import *
import time
import random
from venv import create

from PIL import Image

moves = [
    [10,0,"fisticuffs","attack",10,"doubles next action"],
    [10,30,"psychic","mental",1,"perplexed"],
    []
]
name_search={
    "tense":0,
    "mind ray":1,

}


class MENU():
    def __init__(self):

        # root.attributes("-fullscreen",True)
        self.frame = Frame(padx=0, pady=0)
        self.frame.grid(row=0, column=0)
        self.photo = PhotoImage(file='/home/nate/school/torch.png').zoom(12).subsample(4)
        self.label = Label(self.frame, image=self.photo)
        self.label.grid(row=0, column=0,rowspan=2)
        self.start_button = Button(self.frame, text="Play", font=("arial", 16, "bold"),
                                   fg="#FFFFFF", bg="#0057D8", width=10,command=self.loading_menu)
        self.start_button.grid(row=0, column=0)
        self.start_button = Button(self.frame, text="Quit", font=("arial", 16, "bold"),
                                   fg="#FFFFFF", bg="#0057D8", width=10, command=root.destroy)
        self.start_button.grid(row=1, column=0)

    def loading_menu(self):
        self.frame.destroy()
        Loading()
class Loading():
    """laoding bar"""
    # credit to https://devhubcommunity.hashnode.dev/displaying-gifs-in-tkinter-python?__cf_chl_f_tk=rY.jHPCFPHRvxYg1Pxc0gYmI8mk0.291TAYfHCYhAJQ-1771967830-1.0.1.1-Bx3kTWEOHwG7G9vLJ13no9jxQB2aVjFjpnvr0UuJ9W8
    # and https://www.geeksforgeeks.org/python/how-to-use-images-as-backgrounds-in-tkinter/
    def __init__(self):
        # self.bar= []
        # self.frame = Frame(padx=0, pady=0)
        # self.frame.grid(row=0, column=0)
        self.time = random.randint(70,100)
        print("r")
        self.photo = PhotoImage(file="bar.gif")
        # self.backdrop = Label(image=self.photo)
        self.canvas = Canvas(root, width=1920, height=1080,bg="#262626")

        self.canvas.pack(fill="both", expand=True)

        # Display image

        self.gif_label = Label(image="")
        self.gif_label.pack(side="bottom",anchor='s')
        self.info = Image.open('/home/nate/school/bar.gif')
        self.frames = self.info.n_frames
        self.photoimage_objects = []
        for i in range(1, self.frames):
            self.obj = PhotoImage(file='/home/nate/school/bar.gif', format=f'gif -index {i}')
            self.photoimage_objects.append(self.obj)
        self.animation(current_frame=0)
        root.mainloop()
    def animation(self,current_frame=0):
        global loop
        self.image = self.photoimage_objects[current_frame]
        print(current_frame)
        self.canvas.create_image(950, 860, image=self.photo, )
        self.canvas.create_image(950, 860, image=self.image)

        current_frame = current_frame + 1

        if current_frame == self.frames:
            current_frame = 0
        random.randint(60, 150)
        loop = root.after(300, lambda: self.animation(current_frame))
        # def stop_animation():
        #     root.after_cancel(loop)
        #
        #     gif_label = Label(root, image="")
        #     gif_label.pack()
        #     start = Button(root, text="Start", command=lambda: animation())
        #     start.pack()




if __name__ == '__main__':
    """who knows what this does"""
    root = Tk()
    root.title("Colour Quest")
    MENU()
    root.mainloop()