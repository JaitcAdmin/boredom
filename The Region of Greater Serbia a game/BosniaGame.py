import random
import time
from tkinter import *
import winsound

dif = random.randint(1, 6)

mines, SIZE = [], 20 # Може бити 10 до 50
SQ = 25

ss = []

winsound.PlaySound("a.wav", winsound.SND_ASYNC)


def check(x, y):
    a = 0
    if x > 0:
        if mines[x - 1][y] == -1:
            a += 1
        if y > 0:
            if mines[x - 1][y - 1] == -1:
                a += 1
    if y > 0:
        if mines[x][y - 1] == -1:
            a += 1

    if x < len(mines) - 1:
        if mines[x + 1][y] == -1:
            a += 1
        if y < len(mines[0]) - 1:
            if mines[x + 1][y + 1] == -1:
                a += 1
    if y < len(mines[0]) - 1:
        if mines[x][y + 1] == -1:
            a += 1

    if x < len(mines) - 1 and y > 0:
        if mines[x + 1][y - 1] == -1:
            a += 1

    if y < len(mines[0]) - 1 and x > 0:
        if mines[x - 1][y + 1] == -1:
            a += 1
    return a


def check2(x, y):
    printt(x, y, check(x, y))
    a = 0
    if x > 0:
        if mines[x - 1][y] == -1:
            a += 1
            mines[x - 1][y] = check2(x - 1, y + 1)
        if y > 0:
            if mines[x - 1][y - 1] == -1:
                a += 1
                mines[x - 1][y - 1] = check2(x - 1, y + 1)
    if y > 0:
        if mines[x][y - 1] == -1:
            a += 1
            mines[x][y + 1] = check2(x - 1, y + 1)

    if x < len(mines) - 1:
        if mines[x + 1][y] == -1:
            a += 1
            mines[x + 1][y] = check2(x - 1, y + 1)
        if y < len(mines[0]) - 1:
            if mines[x + 1][y + 1] == -1:
                a += 1
                mines[x + 1][y + 1] = check2(x - 1, y + 1)
    if y < len(mines[0]) - 1:
        if mines[x][y + 1] == -1:
            a += 1
            mines[x][y + 1] = check2(x - 1, y + 1)

    if x < len(mines) - 1 and y > 0:
        if mines[x + 1][y - 1] == -1:
            a += 1
            mines[x + 1][y - 1] = check2(x - 1, y + 1)

    if y < len(mines[0]) - 1 and x > 0:
        if mines[x - 1][y + 1] == -1:
            a += 1
            mines[x - 1][y + 1] = check2(x - 1, y + 1)
    return a


def print_text(x, y):
    a = check(x, y)
    if a != 0:
        c.create_text(x * SQ + int(SQ / 2), y * SQ + int(SQ / 2), text=str(check(x, y)),
                      font="Arial " + str(int(SQ / 1.5)))


def printt(x, y, text):
    c.create_text(x * SQ + int(SQ / 2), y * SQ + int(SQ / 2), text=text, font="Arial " + str(int(SQ / 1.5)))


def zero(x, y):
    c.create_rectangle(x * SQ, y * SQ, x * SQ + SQ, y * SQ + SQ, fill="grey")
    mines[x][y] = -2

    if x > 0:
        if check(x - 1, y) == 0 and mines[x - 1][y] != -2:
            r(x - 1, y)
        else:
            print_text(x - 1, y)
        if y > 0:
            if check(x - 1, y - 1) == 0 and mines[x - 1][y - 1] != -2:
                r(x - 1, y - 1)
            else:
                print_text(x - 1, y - 1)
    if y > 0:
        if check(x, y - 1) == 0 and mines[x][y - 1] != -2:
            r(x, y - 1)
        else:
            print_text(x, y - 1)

    if x < len(mines) - 1:
        if check(x + 1, y) == 0 and mines[x + 1][y] != -2:
            r(x + 1, y)
        else:
            print_text(x + 1, y)
        if y < len(mines[0]) - 1:
            if check(x + 1, y + 1) == 0 and mines[x + 1][y + 1] != -2:
                r(x + 1, y + 1)
            else:
                print_text(x + 1, y + 1)
    if y < len(mines[0]) - 1:
        if check(x, y + 1) == 0 and mines[x][y + 1] != -2:
            r(x, y + 1)
        else:
            print_text(x, y + 1)

    if x < len(mines) - 1 and y > 0:
        if check(x + 1, y - 1) == 0 and mines[x + 1][y - 1] != -2:
            r(x + 1, y - 1)
        else:
            print_text(x + 1, y - 1)

    if y < len(mines[0]) - 1 and x > 0:
        if check(x - 1, y + 1) == 0 and mines[x - 1][y + 1] != -2:
            r(x - 1, y + 1)
        else:
            print_text(x - 1, y + 1)


def r(x, y):
    print("ki")
    if check(x, y) == 0:
        zero(x, y)
    else:
        c.create_text(x * SQ + int(SQ / 2), y * SQ + int(SQ / 2), text=str(check(x, y)),
                      font="Arial " + str(int(SQ / 1.5)))


def show():
    for i in range(SIZE):
        for j in range(SIZE):
            if mines[i][j] == -1 or mines[i][j] == 0:
                c.create_rectangle(i * SQ, j * SQ, i * SQ + SQ, j * SQ + SQ)
            elif mines[i][j] == -2:
                c.create_rectangle(i * SQ, j * SQ, i * SQ + SQ, j * SQ + SQ, fill="grey")
            else:
                c.create_text(i * SQ, j * SQ, text=str(mines[i][j]), font="Arial " + str(int(SQ / 1.5)))


def attack(event):
    if f > 55:
        x, y = event.x // SQ, event.y // SQ
        if mines[x][y] == -1:
            c.create_rectangle(0, 0, SIZE * SQ, SIZE * SQ, fill="red")
            c.create_text(int(SIZE * SQ / 2), int(SIZE * SQ / 4), text="You is died",
                          font="Arial " + str(int(SQ / 1.5)))

            exit(1)
        elif check(x, y) == 0:
            zero(x, y)
        else:
            c.create_text(x * SQ + int(SQ / 2), y * SQ + int(SQ / 2), text=str(check(x, y)),
                          font="Arial " + str(int(SQ / 1.5)))


def randomise():
    for i in range(0, SIZE):
        a = []
        for j in range(0, SIZE):
            a.append(-1 * int(random.randint(0, 5) / 5))

        mines.append(a)


def red_flag(event):
    x, y = event.x // SQ, event.y // SQ
    c.create_line(x * SQ + int(SQ / 4), y * SQ + int(SQ / 4), x * SQ + int(SQ / 4), y * SQ + int((int(SQ / 4)) * 3.5))
    c.create_polygon(x * SQ + int(SQ / 4), y * SQ + int(SQ / 4),
                     x * SQ + int(SQ / 4), y * SQ + int((int(SQ / 4)) * 2.5),
                     x * SQ + int((int(SQ / 4)) * 2.5), y * SQ + int((int(SQ / 4)) * 1.5), fill='red')


tk = Tk()
tk.title('Bosnian game')
c = Canvas(tk, width=SIZE * SQ, height=SIZE * SQ + SQ)
c.pack()

tk.bind_all('<Button-1>', attack)
tk.bind_all('<Button-3>', red_flag)
tk.iconbitmap(default="i.ico")
randomise()

show()

mines[0][0] = 0

timer, f = time.time(), 0

while 1:
    if timer + 1 < time.time():
        c.create_rectangle(0, SIZE * SQ, SIZE * SQ, SIZE * SQ + SQ, fill="white")
        f += 1
        c.create_text(100, SIZE * SQ + SQ / 2, text=str((f % 600) / 10) + " seconds, " + str(f // 600) + " minutes",
                      font="Arial 10")
        if f > 55:
            c.create_text(300, SIZE * SQ + SQ / 2, text="START!",
                          font="Arial 10")
    tk.update()
    tk.update_idletasks()
    time.sleep(0.1)
