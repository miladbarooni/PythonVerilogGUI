from tkinter import *
import time
# from time import sleep

class Car:
    def __init__(self, color, x, y):
        self.color = color
        self.Init = canvas.create_rectangle(x, y, x+20, y+20, fill=self.color)
        self.x = x
        self.y = y

    def mov(self, direction):
        canvas.delete(self.Init)
        if direction == "left":
            self.x = self.x-5
        if direction == "down":
            self.y = self.y+5
        if direction == "up":
            self.y = self.y-5
        if direction == "right":
            self.x = self.x+5

        object = Car(self.color, self.x, self.y)
        self = object


def make_sides():
    canvas.create_line(0, 350, 350, 350)
    canvas.create_line(350, 350, 350, 0)
    canvas.create_line(650, 0, 650, 350)
    canvas.create_line(650, 350, 1000, 350)
    canvas.create_line(0, 650, 350, 650)
    canvas.create_line(350, 650, 350, 1000)
    canvas.create_line(650, 1000, 650, 650)
    canvas.create_line(650, 650, 1000, 650)


def make_in_lines(canvas):
    # create first side of intersection
    canvas.create_line(500, 10, 500, 50)
    canvas.create_line(500, 60, 500, 100)
    canvas.create_line(500, 110, 500, 150)
    canvas.create_line(500, 160, 500, 200)
    canvas.create_line(500, 210, 500, 250)
    canvas.create_line(500, 260, 500, 300)
    canvas.create_line(500, 310, 500, 350)
    # now to create the other side
    canvas.create_line(500, 990, 500, 950)
    canvas.create_line(500, 940, 500, 900)
    canvas.create_line(500, 890, 500, 850)
    canvas.create_line(500, 840, 500, 800)
    canvas.create_line(500, 790, 500, 750)
    canvas.create_line(500, 740, 500, 700)
    canvas.create_line(500, 690, 500, 650)
    # now to create the other side

    canvas.create_line(10, 500, 50, 500)
    canvas.create_line(60, 500, 100, 500)
    canvas.create_line(110, 500, 150, 500)
    canvas.create_line(160, 500, 200, 500)
    canvas.create_line(210, 500, 250, 500)
    canvas.create_line(260, 500, 300, 500)
    canvas.create_line(310, 500, 350, 500)
    # now to create the other side
    canvas.create_line(990, 500, 950, 500)
    canvas.create_line(940, 500, 900, 500)
    canvas.create_line(890, 500, 850, 500)
    canvas.create_line(840, 500, 800, 500)
    canvas.create_line(790, 500, 750, 500)
    canvas.create_line(740, 500, 700, 500)
    canvas.create_line(690, 500, 650, 500)

def make_pedestrian_lines(canvas):
    canvas.create_line(360, 200, 360, 350, width=20)
    canvas.create_line(400, 200, 400, 350, width=20)
    canvas.create_line(440, 200, 440, 350, width=20)
    canvas.create_line(480, 200, 480, 350, width=20)
    canvas.create_line(520, 200, 520, 350, width=20)
    canvas.create_line(560, 200, 560, 350, width=20)
    canvas.create_line(600, 200, 600, 350, width=20)
    canvas.create_line(640, 200, 640, 350, width=20)
    # now to create the other side
    canvas.create_line(360, 650, 360, 800, width=20)
    canvas.create_line(400, 650, 400, 800, width=20)
    canvas.create_line(440, 650, 440, 800, width=20)
    canvas.create_line(480, 650, 480, 800, width=20)
    canvas.create_line(520, 650, 520, 800, width=20)
    canvas.create_line(560, 650, 560, 800, width=20)
    canvas.create_line(600, 650, 600, 800, width=20)
    canvas.create_line(640, 650, 640, 800, width=20)
    # now for Hero
    canvas.create_line(200, 360, 350, 360, width=20)
    canvas.create_line(200, 400, 350, 400, width=20)
    canvas.create_line(200, 440, 350, 440, width=20)
    canvas.create_line(200, 480, 350, 480, width=20)
    canvas.create_line(200, 520, 350, 520, width=20)
    canvas.create_line(200, 560, 350, 560, width=20)
    canvas.create_line(200, 600, 350, 600, width=20)
    canvas.create_line(200, 640, 350, 640, width=20)
    # now to make other side of Hero
    canvas.create_line(650, 360, 800, 360, width=20)
    canvas.create_line(650, 400, 800, 400, width=20)
    canvas.create_line(650, 440, 800, 440, width=20)
    canvas.create_line(650, 480, 800, 480, width=20)
    canvas.create_line(650, 520, 800, 520, width=20)
    canvas.create_line(650, 560, 800, 560, width=20)
    canvas.create_line(650, 600, 800, 600, width=20)
    canvas.create_line(650, 640, 800, 640, width=20)


def set_pedestrian_lights(canvas, pedestrian_lights):
    first_four_lights = []
    # first one
    contains = []
    canvas.create_rectangle(270, 300, 290, 340)
    st_circle = canvas.create_oval(270, 300, 290, 320)
    nd_circle = canvas.create_oval(270, 320, 290, 340)
    contains.append(st_circle)
    contains.append(nd_circle)
    first_four_lights.append(contains)
    # second one
    contains = []
    canvas.create_rectangle(290, 660, 270, 700)
    st_circle = canvas.create_oval(290, 680, 270, 700)
    nd_circle = canvas.create_oval(290, 660, 270, 680)
    contains.append(st_circle)
    contains.append(nd_circle)
    first_four_lights.append(contains)
    # third one
    contains = []
    canvas.create_rectangle(730, 300, 710, 340)
    st_circle = canvas.create_oval(730, 300, 710, 320)
    nd_circle = canvas.create_oval(730, 320, 710, 340)
    contains.append(st_circle)
    contains.append(nd_circle)
    first_four_lights.append(contains)
    # forth one
    contains = []
    canvas.create_rectangle(710, 660, 730, 700)
    st_circle = canvas.create_oval(710, 680, 730, 700)
    nd_circle = canvas.create_oval(710, 660, 730, 680)
    contains.append(st_circle)
    contains.append(nd_circle)
    first_four_lights.append(contains)
    pedestrian_lights.append(first_four_lights)
    # for the second four lights works with other
    second_four_lights = []
    contains = []
    canvas.create_rectangle(300, 260, 340, 280)
    st_circle = canvas.create_oval(300, 260, 320, 280)
    nd_circle = canvas.create_oval(320, 260, 340, 280)
    contains.append(st_circle)
    contains.append(nd_circle)
    second_four_lights.append(contains)
    # the other one
    contains = []
    canvas.create_rectangle(700, 260, 660, 280)
    st_circle = canvas.create_oval(700, 260, 680, 280)
    nd_circle = canvas.create_oval(680, 260, 660, 280)
    contains.append(st_circle)
    contains.append(nd_circle)
    second_four_lights.append(contains)

    contains = []
    canvas.create_rectangle(300, 720, 340, 740)
    st_circle = canvas.create_oval(300, 720, 320, 740)
    nd_circle = canvas.create_oval(320, 720, 340, 740)
    contains.append(st_circle)
    contains.append(nd_circle)
    second_four_lights.append(contains)

    contains = []
    canvas.create_rectangle(700, 720, 660, 740)
    st_circle = canvas.create_oval(700, 720, 680, 740)
    nd_circle = canvas.create_oval(680, 720, 660, 740)
    contains.append(st_circle)
    contains.append(nd_circle)
    second_four_lights.append(contains)
    pedestrian_lights.append(second_four_lights)


def set_cars_lights(canvas, cars_lights):
    first_two_lights = []
    # first one
    contains = []
    canvas.create_rectangle(360, 455, 390, 545)
    st_circle = canvas.create_oval(360, 455, 390, 485)
    nd_circle = canvas.create_oval(360, 485, 390, 515)
    rd_circle = canvas.create_oval(360, 515, 390, 545)
    contains.append(st_circle)
    contains.append(nd_circle)
    contains.append(rd_circle)
    first_two_lights.append(contains)
    # second one
    contains = []
    canvas.create_rectangle(640, 455, 610, 545)
    st_circle = canvas.create_oval(640, 455, 610, 485)
    nd_circle = canvas.create_oval(640, 485, 610, 515)
    rd_circle = canvas.create_oval(640, 515, 610, 545)
    contains.append(st_circle)
    contains.append(nd_circle)
    contains.append(rd_circle)

    first_two_lights.append(contains)
    cars_lights.append(first_two_lights)

    # for the other side
    # first_one
    second_two_lights = []
    contains = []
    canvas.create_rectangle(455, 360, 545, 390)
    st_circle = canvas.create_oval(455, 360, 485, 390)
    nd_circle = canvas.create_oval(485, 360, 515, 390)
    rd_circle = canvas.create_oval(515, 360, 545, 390)
    contains.append(st_circle)
    contains.append(nd_circle)
    contains.append(rd_circle)
    second_two_lights.append(contains)
    # second_one
    contains = []
    canvas.create_rectangle(455, 610, 545, 640)
    st_circle = canvas.create_oval(455, 610, 485, 640)
    nd_circle = canvas.create_oval(485, 610, 515, 640)
    rd_circle = canvas.create_oval(515, 610, 545, 640)
    contains.append(st_circle)
    contains.append(nd_circle)
    contains.append(rd_circle)
    second_two_lights.append(contains)
    cars_lights.append(second_two_lights)


def make_green_for_pedestrian(canvas, pedestrian_lights):
    for i in range(4):
        canvas.itemconfig(pedestrian_lights[0][i][1], fill="green")
        canvas.itemconfig(pedestrian_lights[0][i][0], fill="white")
    for i in range(4):
        canvas.itemconfig(pedestrian_lights[1][i][1], fill="white")
        canvas.itemconfig(pedestrian_lights[1][i][0], fill="red")


def make_red_for_pedestrian(canvas, pedestrian_lights):
    for i in range(4):
        canvas.itemconfig(pedestrian_lights[0][i][1], fill="white")
        canvas.itemconfig(pedestrian_lights[0][i][0], fill="red")
    for i in range(4):
        canvas.itemconfig(pedestrian_lights[1][i][1], fill="green")
        canvas.itemconfig(pedestrian_lights[1][i][0], fill="white")


def make_red_for_cars(canvas, cars_lights):
    for i in range(2):
        canvas.itemconfig(cars_lights[0][i][0], fill="red")
        canvas.itemconfig(cars_lights[0][i][1], fill="white")
        canvas.itemconfig(cars_lights[0][i][2], fill="white")
    for i in range(2):
        canvas.itemconfig(cars_lights[1][i][0], fill="white")
        canvas.itemconfig(cars_lights[1][i][1], fill="white")
        canvas.itemconfig(cars_lights[1][i][2], fill="green")


def make_green_for_cars(canvas, cars_lights):
    for i in range(2):
        canvas.itemconfig(cars_lights[0][i][0], fill="white")
        canvas.itemconfig(cars_lights[0][i][1], fill="white")
        canvas.itemconfig(cars_lights[0][i][2], fill="green")
    for i in range(2):
        canvas.itemconfig(cars_lights[1][i][0], fill="red")
        canvas.itemconfig(cars_lights[1][i][1], fill="white")
        canvas.itemconfig(cars_lights[1][i][2], fill="white")

def make_yellow_for_cars(canvas, cars_lights):
    for i in range(2):
        canvas.itemconfig(cars_lights[0][i][0], fill="white")
        canvas.itemconfig(cars_lights[0][i][1], fill="yellow")
        canvas.itemconfig(cars_lights[0][i][2], fill="white")
    for i in range(2):
        canvas.itemconfig(cars_lights[1][i][0], fill="red")
        canvas.itemconfig(cars_lights[1][i][1], fill="white")
        canvas.itemconfig(cars_lights[1][i][2], fill="white")


filename = "/home/milord/NewProject/test.txt"
file = open(filename, "r")
file_str = file.read()
file_str.replace(" ", "")
file_arr = file_str.split("-")
file_dic ={"lk": "", "first_carsLights": "", "second_carsLights": "", "first_pedestrianLights": "", "second_pedestrianLights" : "", "reg_time":""}
list_of_dics = []
file_arr.reverse()

for moment in file_arr:
    file_dic = {}
    moment_arr = moment.split(",")
    for value in moment_arr:
        value_arr = value.split(":")
        if len(value_arr) == 1:
            continue
        file_dic[value_arr[0]] = value_arr[1]
    list_of_dics.append(file_dic)

pedestrian_lights = []
cars_lights = []
root = Tk()

root.title("Intersection")
label = Label(root, text="Hello")

canvas = Canvas(root, width=1000, height=1000)
canvas.pack()
make_sides()
make_in_lines(canvas)
make_pedestrian_lines(canvas)
set_pedestrian_lights(canvas, pedestrian_lights)
set_cars_lights(canvas, cars_lights)
make_yellow_for_cars(canvas, cars_lights)
time1 = 0
list_of_dics = list_of_dics[2:]
print (list_of_dics)
for state in list_of_dics:
    if state["first_pedestrianLights"] == "10":
        make_red_for_pedestrian(canvas, pedestrian_lights)
        print("hello")
    else:
        make_green_for_pedestrian(canvas, pedestrian_lights)
        print("Bye")
    if state["first_carsLights"] == "100":
        make_red_for_cars(canvas, cars_lights)
    elif state["first_carsLights"] == "010":
        make_yellow_for_cars(canvas, cars_lights)
    else:
        make_green_for_cars(canvas, cars_lights)
    time.sleep(1)
    time1 += 1
    print(time1)
    root.update()
root.mainloop()
