from random import randint, choice
from tkinter import *
import re


def create_new_window():
    global pattern_id
    global new_window
    global import_prompt

    new_window = Toplevel(master)
    new_window.title("Import and Export")
    new_window.iconbitmap("pfp_icon.ico")

    # Import and Export Labels
    Label(new_window, text="Export ID: ").grid(row=0, column=0, sticky=E)
    Label(new_window, text="Import ID: ").grid(row=1, column=0, sticky=E)

    # Displaying text in an input box to allow text selection
    display = StringVar()
    display.set(pattern_id)

    # Entry object acting like a label
    export_text = Entry(new_window, relief='flat', textvariable=display, state='readonly', fg="blue", width=70)
    export_text.grid(row=0, column=1, padx=1)

    # Entry object to allow user to input an ID
    import_prompt = Entry(new_window, fg="blue")
    import_prompt.grid(row=1, column=1, sticky=E+W, padx=1, pady=1)
    import_prompt.bind('<Return>', import_check)

    # Only allowing the opening of one new window and doesn't allow access to features in master
    new_window.transient(master)
    new_window.grab_set()

    new_window.resizable(False, False)
    new_window.mainloop()


def rand_hex():
    return f"#{randint(0, 0xFFFFFF):06x}"


def valid_id(import_id):
    global hex_val
    global pattern

    # If pattern is not a valid ID
    if not re.match(r"^#[0-9a-fA-F]{6}(_[01]{7}){7}$", import_id):
        return False

    # If pattern is a valid ID, extract the hex and binary parts
    else:
        hex_val = import_id[:7]
        pattern = import_id[8:].split("_")
        return True


def import_check(event):
    fetched_id = import_prompt.get().lower()

    # Close the new window if the ID is valid
    if valid_id(fetched_id):
        new_window.destroy()
        read_id(fetched_id)

    # Else, clear the input prompt to try again
    else:
        import_prompt.delete(0, "end")


def read_id(import_id):
    global colour

    for i in range(7):
        for j in range(7):
            # Display a white coloured tile
            if pattern[i][j] == "0":
                grid[i][j] = "#FFFFFF"
                Canvas(main_canvas, width=50, height=50, bg="#FFFFFF", highlightthickness=0).grid(row=i, column=j)

            # Display a coloured tile
            else:
                grid[i][j] = hex_val
                Canvas(main_canvas, width=50, height=50, bg=hex_val, highlightthickness=0).grid(row=i, column=j)

    # Updates border colour, sets new id and colour based on current colour
    master.config(bg=hex_val)
    generate_id(hex_val)
    colour = hex_val


def generate_id(hex_val):
    global pattern_id
    
    # First part of the pattern is the hex value
    pattern_id = f"{hex_val}"

    for i in range(7):
        # Separate values by an underscore
        pattern_id += "_"

        # Adding each row's binary strings to the pattern
        for j in range(7):
            if grid[i][j] == "#FFFFFF":
                pattern_id += "0"
            else:
                pattern_id += "1"


def new_pfp_colour(hex_val):
    global colour
    for i in range(7):
        for j in range(7):
            # Overwrite the current colour with a new colour if the current tile is not white0
            if grid[i][j] != "#FFFFFF":
                Canvas(main_canvas, width=50, height=50, bg=hex_val, highlightthickness=0).grid(row=i, column=j)

    master.config(bg=hex_val)
    generate_id(hex_val)
    colour = hex_val


def new_patt(hex_val):
    for i in range(7):
        # Columns 1-3 = rows 5-7 (horizontally symmetrical)
        for j in range(3):
            temp = choice([hex_val, "#FFFFFF"])
            grid[i][j] = temp
            grid[i][6 - j] = grid[i][j]

        # Column 4 is random on its own
        grid[i][3] = choice([hex_val, "#FFFFFF"])

    for i in range(7):
        for j in range(7):
            Canvas(main_canvas, width=50, height=50, bg=grid[i][j], highlightthickness=0).grid(row=i, column=j)

    master.config(bg=hex_val)
    generate_id(hex_val)


master = Tk()
master.title("Identicon Generator")
master.iconbitmap("pfp_icon.ico")

# 7 by 7 array to store hex values of each grid value of the pattern
grid = [["" for _ in range(7)] for _ in range(7)]

# Frame to display the buttons
buttons_frame = Frame(master)
buttons_frame.pack(fill=X)

# Canvas to display the pattern
main_canvas = Canvas(master, height=350, width=350, bg="#000000")
main_canvas.pack(fill=X, padx=35, pady=35)

# New Pattern button
b1 = Button(buttons_frame, text="New Pattern", command=lambda: new_patt(colour))
b1.pack(side=LEFT, fill=X, expand=1)
b1.config(width=1)

# New Colour button
b2 = Button(buttons_frame, text="New Colour", command=lambda: new_pfp_colour(rand_hex()))
b2.pack(side=LEFT, fill=X, expand=1)
b2.config(width=1)

# Custom button
b3 = Button(buttons_frame, text="Custom", command=lambda: create_new_window())
b3.pack(side=LEFT, fill=X, expand=1)
b3.config(width=1)

# Generates a random colour with a random pattern on startup
colour = rand_hex()
new_patt(colour)

master.resizable(False, False)
master.mainloop()
