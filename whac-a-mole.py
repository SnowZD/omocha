import tkinter.font as tkFont
from tkinter import *
import random
from PIL import Image, ImageTk
from threading import Timer
import datetime

window = Tk()
window.title("YTC")

w = 360
h = 400
x = 300
y = 200
window.geometry("%dx%d+%d+%d" % (w, h, x, y))
window.resizable(False, False)

fontStyle = tkFont.Font(size=24)

point_frame = Frame(window, width=0, height=0)
point_frame.grid(row=0, column=0, padx=10, pady=0)
row1_frame = Frame(window, width=0, height=0)
row1_frame.grid(row=1, column=0, padx=10, pady=5)
row2_frame = Frame(window, width=0, height=0)
row2_frame.grid(row=2, column=0, padx=10, pady=5)
row3_frame = Frame(window, width=0, height=0)
row3_frame.grid(row=3, column=0, padx=10, pady=5)

point = 0
point_text = StringVar()
point_text.set("Point:" + str(point))
point_label = Label(point_frame, font=fontStyle, textvariable=point_text)
point_label.pack(side=LEFT)
E1 = Spinbox(point_frame, from_=1, to=60, increment=1, width=5)
E1.pack(side=LEFT)
Start_Button = Button(point_frame, font=fontStyle, text="START")
Start_Button.pack(side=LEFT)

row1_label1 = Label(row1_frame, width=15, height=7, bg="blue")
row1_label1.pack(padx=5, side=LEFT)
row1_label2 = Label(row1_frame, width=15, height=7, bg="blue")
row1_label2.pack(padx=5, side=LEFT)
row1_label3 = Label(row1_frame, width=15, height=7, bg="blue")
row1_label3.pack(padx=5, side=LEFT)

row2_label1 = Label(row2_frame, width=15, height=7, bg="blue")
row2_label1.pack(padx=5, side=LEFT)
row2_label2 = Label(row2_frame, width=15, height=7, bg="blue")
row2_label2.pack(padx=5, side=LEFT)
row2_label3 = Label(row2_frame, width=15, height=7, bg="blue")
row2_label3.pack(padx=5, side=LEFT)

row3_label1 = Label(row3_frame, width=15, height=7, bg="blue")
row3_label1.pack(padx=5, side=LEFT)
row3_label2 = Label(row3_frame, width=15, height=7, bg="blue")
row3_label2.pack(padx=5, side=LEFT)
row3_label3 = Label(row3_frame, width=15, height=7, bg="blue")
row3_label3.pack(padx=5, side=LEFT)

label_array = [
    row1_label1,
    row1_label2,
    row1_label3,
    row2_label1,
    row2_label2,
    row2_label3,
    row3_label1,
    row3_label2,
    row3_label3,
]

photo = ImageTk.PhotoImage(Image.open("icon/ghost.png"))
withoutphoto = ImageTk.PhotoImage(Image.open("icon/withoutghost.png"))


def on_label_click(event):
    global point
    if Start_Button.cget("state") == "disabled":
        clicked_label = event.widget
        if clicked_label.cget("image") == "pyimage1":  # default
            point = point + 10
            point_text.set("Point:" + str(point))
            clicked_label.config(image=withoutphoto, width=100, height=100)
            # Generate_Random()


i = 0
while i < len(label_array):
    label_array[i].config(image=withoutphoto, width=100, height=100)
    label_array[i].bind("<Button-1>", on_label_click)
    i = i + 1


def timer_counter():
    global t, m, start_time
    t = Timer(1, timer_counter)
    cur_time = datetime.datetime.now()
    dif = cur_time - start_time
    t.start()
    try:
        if dif.seconds > int(E1.get()):
            t.cancel()
            Start_Button.config(state=NORMAL)
            i = 0
            while i < len(label_array):
                label_array[i].config(image=withoutphoto, width=100, height=100)
                i = i + 1
        else:
            Generate_Random(dif)
    except:
        t.cancel()


t = Timer(0, timer_counter)


def Game_Start():
    global t, start_time, point
    start_time = datetime.datetime.now()
    t = Timer(0, timer_counter)
    point = 0
    point_text.set("Point:" + str(point))
    t.start()
    Start_Button.config(state=DISABLED)


def Generate_Random(dif):
    i = 0
    while i < len(label_array):
        label_array[i].config(image=withoutphoto, width=100, height=100)
        i = i + 1
    num = random.randint(0, len(label_array) - 1)
    label_array[num].config(image=photo, width=100, height=100)
    if dif.seconds > int(E1.get()) / 2:
        num = random.randint(0, len(label_array) - 1)
        label_array[num].config(image=photo, width=100, height=100)
    # label_array[num].config(bg="Red")


Start_Button.config(command=Game_Start)

if __name__ == "__main__":
    window.mainloop()
