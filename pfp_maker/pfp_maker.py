from tkinter import *
from random import randint, choice
import re

def createNewWindow():
    global code
    global top2
    global doodoobro

    top2 = Toplevel(master)
    top2.title("Import and Export")
    top2.iconbitmap("pfp_icon.ico")

    Label(top2, text="Export ID: ").grid(row=0, column=0, sticky=E)
    omkapoor = Entry(top2, relief='flat',  state='readonly', fg="blue", width=70)

    var = StringVar()
    var.set(code)
    omkapoor.config(textvariable=var)
    omkapoor.grid(row=0, column=1, padx=1)


    Label(top2, text="Import ID: ").grid(row=1, column=0, sticky=E)
    doodoobro = Entry(top2, fg="blue")
    doodoobro.grid(row=1, column=1, sticky=E+W, padx=1, pady=1)
    doodoobro.bind('<Return>', import_check)


    top2.resizable(False, False)    
    top2.transient(master)
    top2.grab_set()
    master.wait_window(top2)

        
def rand_hex():
    return f"#{randint(0, 0xFFFFFF):06x}"


def valid_code(import_code):
    global hex_val
    global pattern

    hex_val = import_code[:7]
    pattern = import_code[8:].split("_")
    bin_check = True

    if len(pattern) == 7:
        for i in pattern:
            if len(i) == 7:
                for j in i:
                    if j not in {"0", "1"}:
                        bin_check = False
            else:
                bin_check = False
    else:
        bin_check = False

    return bin_check and bool(re.match("^#[0-9a-fA-F]{6}$", hex_val.upper()))


def import_check(event):
    global a
    a = doodoobro.get()

    if valid_code(a):
        top2.destroy()
        read_code(a)
    else:
        doodoobro.delete(0, "end")


def read_code(import_code):
    global colour

    for i in range(7):
        for j in range(7):
            if pattern[i][j] == "0":
                grid[i][j] = "#FFFFFF"
                Canvas(test_frame, width=50, height=50, bg="#FFFFFF",highlightthickness=0).grid(row=i, column=j)
            else:
                grid[i][j] = hex_val
                Canvas(test_frame, width=50, height=50, bg=hex_val, highlightthickness=0).grid(row=i, column=j)


    master.config(bg=hex_val)
    generate_code(hex_val)
    colour = hex_val


def generate_code(hex_val):
    global code
    code = f"{hex_val}"

    for i in range(7):
        code += "_"

        for j in range(7):
            if grid[i][j] == "#FFFFFF":
                code += "0"
            else:
                code += "1"


def new_pfp_colour(hex_val):
    global colour
    for i in range(7):
        for j in range(7):
            if grid[i][j] != "#FFFFFF":
                Canvas(test_frame, width=50, height=50, bg=hex_val, highlightthickness=0).grid(row=i, column=j)
        
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
            Canvas(test_frame, width=50, height=50, bg=grid[i][j], highlightthickness=0).grid(row=i, column=j)

    master.config(bg=hex_val)
    generate_code(hex_val)


master = Tk()
master.title("Identicon Generator")
master.iconbitmap("pfp_icon.ico")

colour = rand_hex()
grid = [[-1 for i in range(7)] for i in range(7)]

buttons_frame = Frame(master, height=40)
buttons_frame.pack(fill=X)

# width messed up maybe (fix later)
test_frame = Frame(master, height=420, width=420, bg="#000000")
test_frame.pack(fill=X, padx=35, pady=35)

b1 = Button(buttons_frame, text="New Pattern", command=lambda: new_patt(colour))
b1.pack(side=LEFT, fill=X, expand=1)
b1.config(width=1)

b2 = Button(buttons_frame, text="New Colour", command=lambda: new_pfp_colour(rand_hex()))
b2.pack(side=LEFT, fill=X, expand=1)
b2.config(width=1)

b3 = Button(buttons_frame, text="Custom", command=lambda: createNewWindow())
b3.pack(side=LEFT, fill=X, expand=1)
b3.config(width=1)

new_patt(colour)

master.resizable(False, False)
master.mainloop()
