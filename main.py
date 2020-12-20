from tkinter import *
tk = Tk()
tk.title('Floppy Bird')
cv = Canvas(tk, width=500, height=500)
cv.pack()


class guy:
    def __init__(self):
        self.canvas = cv
        self.yMomentum = 1
        cv.bind_all('<KeyPress-Right>', self.flap())
        self.id = cv.create_oval(10, 10, 25, 25)

    def flap(self):
        self.yMomentum = self.yMomentum - 1

    def draw(self):
        self.canvas.move(self.id, 0, self.yMomentum)


bird = guy()

cv.mainloop()
