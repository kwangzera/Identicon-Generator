from tkinter import *
from random import randint, choice


def rand_hex():
    return f"#{randint(0, 0xFFFFFF):06x}"


def generate_code(hex_val):
    code = f"{hex_val}_"
    for i in range(7):
        for j in range(7):
            if grid[i][j] != "#FFFFFF":
                code += "0"
            else:
                code += "1"

    print(code)


def new_pfp_colour(hex_val):
    global colour
    for i in range(7):
        for j in range(7):
            if grid[i][j] != "#FFFFFF":
                Canvas(
                    test_frame,
                    width=50,
                    height=50,
                    bg=hex_val,
                    highlightthickness=0
                ).grid(row=i, column=j)

    master.config(bg=hex_val)
    generate_code(hex_val)
    colour = hex_val


def new_patt(hex_val):
    for i in range(7):
        for j in range(3):
            temp = choice([hex_val, "#FFFFFF"])
            grid[i][j] = temp
            grid[i][6-j] = grid[i][j]

        grid[i][3] = choice([hex_val, "#FFFFFF"])

    for i in range(7):
        for j in range(7):
            Canvas(
                test_frame,
                width=50,
                height=50,
                bg=grid[i][j],
                highlightthickness=0
            ).grid(row=i, column=j)

    master.config(bg=hex_val)
    generate_code(hex_val)


master = Tk()
master.minsize(0, 0)

colour = rand_hex()
grid = [[-1 for i in range(7)] for i in range(7)]

buttons_frame = Frame(master, height=40)
buttons_frame.grid(row=0, column=0, sticky=N+E+S+W)
buttons_frame.grid_columnconfigure(0, minsize=1, weight=1)
buttons_frame.grid_columnconfigure(1, minsize=1, weight=1)
buttons_frame.grid_columnconfigure(2, minsize=1, weight=1)

test_frame = Frame(
    master,
    height=420,
    width=420,
    bg="#000000"
)
test_frame.grid(row=1, column=0, sticky=N+E+S+W)

b1 = Button(
    buttons_frame,
    text="New Pattern",
    command=lambda: new_patt(colour)
)
b1.grid(row=0, column=0, sticky=N+E+S+W)

b2 = Button(
    buttons_frame,
    text="New Colour",
    command=lambda: new_pfp_colour(rand_hex())
)
b2.grid(row=0, column=1, sticky=N+E+S+W)

b3 = Button(
    buttons_frame,
    text="More",
)
b3.grid(row=0, column=2, sticky=N+E+S+W)

new_patt(colour)

master.resizable(False, False)
master.mainloop()
