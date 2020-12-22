from tkinter import *
import time
tk = Tk()
tk.title('Floppy Bird')
cv = Canvas(tk, width=500, height=500)
cv.pack()
jumpPower = 4
gravity = 5


class guy:
    def __init__(self):
        self.canvas = cv
        self.jumpPower = 4
        self.gravity = 5
        self.yMomentum = 1
        cv.bind_all('<KeyPress-Up>', self.flap)
        self.id = cv.create_oval(10, 10, 25, 25, fill='cyan')

    def flap(self, null):
        self.yMomentum = self.yMomentum - jumpPower

    def draw(self):
        self.canvas.move(self.id, 0, self.yMomentum)
        self.yMomentum = self.yMomentum + (0.01 * gravity)


class obstacle:
    def __init__(self, position):
        self.canvas = cv
        self.cooldowntime = 4
        self.counter = 0
        self.xMomentum = 0
        self.id = cv.create_rectangle(0, 0, 10, 300)
        self.pos = self.canvas.coords(self.id)
        if position == 'bottom':
            self.canvas.coords(self.id, 490, 300, 500, 500)
            print('initial resetting')
        else:
            self.canvas.coords(self.id, 490, 0, 500, 200)
            print('initial resetting')

    def draw(self, position):

        self.canvas.move(self.id, self.xMomentum, 0)
        self.pos = self.canvas.coords(self.id)
        self.counter = self.counter + 0.01
        if self.pos[0] <= 0:
            print('got to the end')
            self.xMomentum = 0
            if position == 'bottom':
                self.canvas.coords(self.id, 490, 300, 500, 500)
                print('bottom resetting ' + str(self.pos))
            else:
                self.canvas.coords(self.id, 490, 0, 500, 200)
                print('top resetting ' + str(self.pos))
        if self.counter >= 4:
            self.goforwards()
            print('go forwards')
            self.counter = 0

    def goforwards(self):
        self.xMomentum = -3
        print('going forwards')
        self.cooldowntime = self.cooldowntime - 1
        print(self.cooldowntime)


bottomThing = obstacle(position="bottom")
topThing = obstacle(position='top')
bird = guy()
while True:
    time.sleep(0.01)
    bird.draw()
    topThing.draw('top')
    bottomThing.draw('bottom')
    tk.update()
