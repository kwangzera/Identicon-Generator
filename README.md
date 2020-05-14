# Identicon Generator  
Open the folder pfp_maker and double click pfp_maker.py to run the program.  
Made using Python Tkinter.  

### Basics
This program generates symmetrical 7 by 7 identicons.  
The "New Patten" and "New Colour" buttons generate a random pattern and a random colour respectively.  
The "Custom" button brings up a dialog that allows you to import and export identicons.  

### Importing and Exporting
Each pattern displayed can be represented by ID in the format of `#colour_pattern`.  
`#colour` is a 6 character long hex value representing a colour.  
`pattern` is a 7-length list of 7-length binary strings, joined by `_`.  
In the pattern, `0` represents an empty tile (white) and `1` represents a filled tile (coloured).  

### Example IDs
`#d8b016_1100011_1101011_0000000_1001001_1001001_1011101_1101011`
`#fb50d5_1111111_1111111_0100010_1101011_1000001_1100011_1001001`
`#17ca0c_1001001_1000001_0111110_1101011_0010100_0101010_0011100`
