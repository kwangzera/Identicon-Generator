from tkinter import *
from random import randint, choice


def rand_hex():
    return f"#{randint(0, 0xFFFFFF):06x}"


def generate_code(colour):
    code = f"{colour}_"
    for i in range(7):
        for j in range(7):
            if grid[i][j] != "#FFFFFF":
                code += "0"
            else:
                code += "1"

    print(code)


def new_pfp_colour(colour):
    for i in range(7):
        for j in range(7):
            if grid[i][j] != "#FFFFFF":
                Canvas(
                    test_frame,
                    width=50,
                    height=50,
                    bg=colour,
                    highlightthickness=0
                ).grid(row=i, column=j)

    master.config(bg=colour)
    generate_code(colour)


def new_patt(colour):
    for i in range(7):
        for j in range(3):
            temp = choice([colour, "#FFFFFF"])
            grid[i][j] = temp
            grid[i][6-j] = grid[i][j]

        grid[i][3] = choice([colour, "#FFFFFF"])

    for i in range(7):
        for j in range(7):
            Canvas(
                test_frame,
                width=50,
                height=50,
                bg=grid[i][j],
                highlightthickness=0
            ).grid(row=i, column=j)

    master.config(bg=colour)
    generate_code(colour)


# global code
code = ""

master = Tk()
master.minsize(0, 0)

colour = rand_hex()
grid = [[-1 for i in range(7)] for i in range(7)]

buttons_frame = Frame(master, height=40)
buttons_frame.pack(fill=X)

test_frame = Frame(
    master,
    height=420,
    width=420,
    bg="#000000"
)
test_frame.pack(fill=X, padx=35, pady=35)

b1 = Button(
    buttons_frame,
    text="New Pattern",
    command=lambda: new_patt(colour)
)
b1.pack(side=LEFT, fill=X, expand=1)

b2 = Button(
    buttons_frame,
    text="New Colour",
    command=lambda: new_pfp_colour(rand_hex())
)
b2.pack(side=RIGHT, fill=X, expand=1)

new_patt(colour)

master.resizable(False, False)
master.mainloop()
