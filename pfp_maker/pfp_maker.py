import os
import re
import tkinter as tk
from random import randint, choice
from PIL import Image, ImageDraw

"""
add better comments
reformat code
"""

def create_new_window():
    global pattern_id
    global new_window
    global import_prompt

    new_window = tk.Toplevel(master)
    new_window.title("Import and Export")
    new_window.iconbitmap("pfp_icon.ico")

    # Import and Export Labels
    tk.Label(new_window, text="Export ID: ").grid(row=0, column=0, sticky="e")
    tk.Label(new_window, text="Import ID: ").grid(row=1, column=0, sticky="e")
    tk.Label(new_window, text="Save As: ").grid(row=2, column=0, sticky="e")

    # Displaying text in an input box to allow text selection
    display = tk.StringVar()
    display.set(pattern_id)

    # Entry object acting like a label
    export_text = tk.Entry(new_window, relief="flat", textvariable=display, state="readonly", fg="blue", width=70)
    export_text.grid(row=0, column=1, padx=1, pady=1)

    # Entry object to allow user to input an ID
    import_prompt = tk.Entry(new_window, fg="blue")
    import_prompt.grid(row=1, column=1, sticky="ew", padx=1, pady=1)
    import_prompt.bind("<Return>", import_check)

    # Save image promtp (add comment later)
    save_button = tk.Button(new_window, text="Click to save Identicon as PNG", command=lambda: save_image(pattern_id))  # add command later
    save_button.grid(row=2, column=1, padx=1, pady=1, sticky="ew")

    # Only allowing the opening of one new window and doesn't allow access to features in master
    new_window.transient(master)
    new_window.grab_set()

    new_window.resizable(False, False)
    new_window.mainloop()


def rand_hex():
    return f"#{randint(0, 0xFFFFFF):06x}"


def save_image(pattern_id):  # -> uses pattern
    print(pattern_id)
    split_hex(pattern_id)
    # hex_val = pattern_id[:7]
    # pattern = pattern_id[8:].split("_")
    new_window.destroy()

    image1 = Image.new("RGB", (420, 420), hex_val)
    draw = ImageDraw.Draw(image1)

    x1, y1 = 35, 35
    x2, y2 = 85, 85

    for r in range(7):
        for c in range(7):
            dx = c * 50
            if pattern[r][c] == "1":
                draw.rectangle((x1+dx, y1, x2+dx, y2), fill=hex_val)
            else:
                draw.rectangle((x1+dx, y1, x2+dx, y2), fill="#FFFFFF")

        y1 += 50
        y2 += 50

    filename = f"{pattern_id}.png"
    image1.save(filename)
    os.startfile(filename)


def split_hex(import_id):
    global hex_val
    global pattern    

    hex_val = import_id[:7]
    pattern = import_id[8:].split("_")

def valid_id(import_id):  # -> uses pattern
    split_hex(import_id)

    # If pattern is not a valid ID
    if not re.match(r"^#[0-9a-fA-F]{6}(_[01]{7}){7}$", import_id):
        return False

    # If pattern is a valid ID, extract the hex and binary parts
    else:
        # hex_val = import_id[:7]
        # pattern = import_id[8:].split("_")
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


def read_id(import_id):  # -> uses pattern
    global colour

    for r in range(7):
        for c in range(7):
            # Display a white coloured tile
            if pattern[r][c] == "0":
                grid[r][c] = "#FFFFFF"
                tk.Canvas(main_canvas, width=50, height=50, bg="#FFFFFF", highlightthickness=0).grid(row=r, column=c)

            # Display a coloured tile
            else:
                grid[r][c] = hex_val
                tk.Canvas(main_canvas, width=50, height=50, bg=hex_val, highlightthickness=0).grid(row=r, column=c)

    # Updates border colour, sets new id and colour based on current colour
    master.config(bg=hex_val)
    generate_id(hex_val)
    colour = hex_val


def generate_id(hex_val):
    global pattern_id
    
    # First part of the pattern is the hex value
    pattern_id = f"{hex_val}"

    for r in range(7):
        # Separate values by an underscore
        pattern_id += "_"

        # Adding each row's binary strings to the pattern
        for c in range(7):
            if grid[r][c] == "#FFFFFF":
                pattern_id += "0"
            else:
                pattern_id += "1"


def new_pfp_colour(hex_val):
    global colour

    for r in range(7):
        for c in range(7):
            # Overwrite the current colour with a new colour if the current tile is not white0
            if grid[r][c] != "#FFFFFF":
                tk.Canvas(main_canvas, width=50, height=50, bg=hex_val, highlightthickness=0).grid(row=r, column=c)

    master.config(bg=hex_val)
    generate_id(hex_val)
    colour = hex_val


def new_patt(hex_val):
    for r in range(7):
        
        # Columns 1-3 = rows 5-7 (horizontally symmetrical)
        for c in range(3):
            temp = choice([hex_val, "#FFFFFF"])
            grid[r][c] = temp
            grid[r][6-c] = grid[r][c]

        # Column 4 is random on its own
        grid[r][3] = choice([hex_val, "#FFFFFF"])

    for r in range(7):
        for c in range(7):
            tk.Canvas(main_canvas, width=50, height=50, bg=grid[r][c], highlightthickness=0).grid(row=r, column=c)

    master.config(bg=hex_val)
    generate_id(hex_val)


master = tk.Tk()
master.title("Identicon Generator")
master.iconbitmap("pfp_icon.ico")

# 7 by 7 array to store hex values of each grid value of the pattern
grid = [["" for _ in range(7)] for _ in range(7)]

# Frame to display the buttons
buttons_frame = tk.Frame(master)
buttons_frame.pack(fill="x")

# Canvas to display the pattern
main_canvas = tk.Canvas(master, height=350, width=350, bg="#000000")
main_canvas.pack(fill="x", padx=35, pady=35)

# New Pattern button
b1 = tk.Button(buttons_frame, text="New Pattern", command=lambda: new_patt(colour))
b1.pack(side="left", fill="x", expand=1)
b1.config(width=1)

# New Colour button
b2 = tk.Button(buttons_frame, text="New Colour", command=lambda: new_pfp_colour(rand_hex()))
b2.pack(side="left", fill="x", expand=1)
b2.config(width=1)

# Custom button
b3 = tk.Button(buttons_frame, text="Custom", command=lambda: create_new_window())
b3.pack(side="left", fill="x", expand=1)
b3.config(width=1)

# Generates a random colour with a random pattern on startup
colour = rand_hex()
new_patt(colour)

# saves current image
# save_image(colour)


master.resizable(False, False)
master.mainloop()