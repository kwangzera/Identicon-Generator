from tkinter import *
from random import randint, choice


def createNewWindow():
    global code
    top2 = Toplevel(master)
    top2.title("Import and Export")

    Label(top2, text="Export ID: ").grid(row=0, column=0)
    Label(top2, text=code, fg="blue").grid(row=0, column=1)
    
    Label(top2, text="Import ID: ").grid(row=1, column=0)
    Entry(top2, text=code, fg="blue").grid(row=1, column=1, sticky=E+W, padx=2, pady=2)

    top2.resizable(False, False)    
    top2.transient(master)
    top2.grab_set()
    master.wait_window(top2)

        
def rand_hex():
    return f"#{randint(0, 0xFFFFFF):06x}"


def generate_code(hex_val):
    global code
    code = f"{hex_val}"

    for i in range(7):
        code += "_"

        for j in range(7):
            if grid[i][j] != "#FFFFFF":
                code += "0"
            else:
                code += "1"

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
master.title("Identicon Generator")
# master.iconbitmap("pfp_icon.ico")
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
b1.config(width=1)

b2 = Button(
    buttons_frame,
    text="New Colour",
    command=lambda: new_pfp_colour(rand_hex())
)
b2.pack(side=LEFT, fill=X, expand=1)
b2.config(width=1)

b3 = Button(
    buttons_frame,
    text="Custom",
    command=lambda: createNewWindow()
)
b3.pack(side=LEFT, fill=X, expand=1)
b3.config(width=1)

new_patt(colour)

master.resizable(False, False)
master.mainloop()
