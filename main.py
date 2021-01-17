from tkinter import *
import time
import random
tk = Tk()
tk.title('Floppy Bird')
cv = Canvas(tk, width=500, height=500)
cv.pack()
jumpPower = 4
gravity = 5
obstaclePosition = random.randint(-100, 100)


class guy:
    def __init__(self):
        self.canvas = cv
        self.jumpPower = 4
        self.gravity = 5
        self.yMomentum = 1
        cv.bind_all('<KeyPress-Up>', self.flap)
        self.id = cv.create_oval(10, 10, 25, 25, fill='cyan')
        self.pos = self.canvas.coords(self.id)

    def flap(self, null):
        self.yMomentum = self.yMomentum - jumpPower

    def draw(self):
        self.canvas.move(self.id, 0, self.yMomentum)
        self.pos = self.canvas.coords(self.id)
        self.yMomentum = self.yMomentum + (0.01 * gravity)


class obstacle:
    def __init__(self, height, x, y):
        self.canvas = cv
        self.complete = False
        self.height = height
        self.x = x
        self.y = y
        self.coolDownTime = 4
        self.speedUpTime = 0.1
        self.counter = 0
        self.xMomentum = 0
        self.id = cv.create_rectangle(0, 0, 10, height, fill='Red')
        self.pos = self.canvas.coords(self.id)
        self.canvas.coords(self.id, self.x, self.y, self.x + 10, self.y - self.height)

    def changeLocation(self, x, y):
        self.complete = False
        self.canvas.coords(self.id, x, y, x + 10, y - self.height)

    def draw(self, position):
        self.canvas.move(self.id, self.xMomentum, 0)
        self.pos = self.canvas.coords(self.id)
        self.counter = self.counter + 0.01
        if self.collisionCheck():
            exit()
        if self.pos[0] <= 0:
            self.complete = True
            # print('got to the end')
            self.xMomentum = 0
        if self.counter >= self.coolDownTime:
            self.goForwards()
            # print('go forwards')
            self.counter = 0

    def collisionCheck(self):
        if (self.pos[0] <= bird.pos[2] <= self.pos[2]) or (self.pos[0] <= bird.pos[0] <= self.pos[2]):
            # print(bird.pos)
            # print(self.pos )
            # print( bird.pos[3],self.pos[3],self.pos[1])
            if (self.pos[1] <= bird.pos[3] <= self.pos[3]) or (self.pos[1] <= bird.pos[1] <= self.pos[3]):
                return True

    def goForwards(self):
        self.xMomentum = -3
        # print('going forwards')
        self.coolDownTime = self.coolDownTime - 0.2
        # print(self.coolDownTime)


topThing = obstacle(1000, 490, 200)
bottomThing = obstacle(1000, 490, 1300)
cv.create_text(200, 200, text='Ready?', font=('Times', 20), fill='Blue')
bird = guy()
bird.draw()
topThing.draw('top')
bottomThing.draw('bottom')
tk.update()
time.sleep(3)
cv.create_text(200, 250, text='Go!', font=('Times', 20), fill='Blue')
while True:
    time.sleep(0.01)
    bird.draw()
    topThing.draw('top')
    bottomThing.draw('bottom')
    tk.update()
    if topThing.complete:
        randomVariable = random.randint(-225, 225)
        topThing.changeLocation(490, 200 + randomVariable)
        bottomThing.changeLocation(490, 1300 + randomVariable)
