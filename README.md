# Identicon Generator
This program generates symmetrical 7 by 7 identicons and allows to use to create their own identicons via import and export codes.

### Setup
Once downloaded, double click `run.bat` to start the program.  
All necessary libraries will be installed in a virtual environment.  

### Basics
The `New Patten` and `New Colour` buttons generate a random pattern and a random colour respectively.  
The `Custom` button brings up a dialog that allows you to import, export, and save identicons with a pattern ID.  

### Importing and Exporting
Each pattern displayed can be represented by ID in the format of `#colour_pattern`.  
`#colour` is a 6 character long hex value representing a colour.  
`pattern` is a 7-length list of 7-length binary strings, joined by `_`.  
In the pattern, `0` represents an empty tile (white) and `1` represents a filled tile (coloured).  

### Saving an Identicon as PNG
You also have to option to save an identicon as a PNG, after clicking the `Custom` button.  
The image will be saved as `pattern_id.png` in the same file location as run.bat.  
(Windows exclusive) A prompt will then appear to let you preview the image after it has been successfully saved.  
The identicons located in `assets/demo` are the ones matching the Example IDs below.  

### Example IDs
`#17ca0c_1001001_1000001_0111110_1101011_0010100_0101010_0011100`
`#d8b016_1100011_1101011_0000000_1001001_1001001_1011101_1101011`
`#fb50d5_1111111_1111111_0100010_1101011_1000001_1100011_1001001`

### Todo
- Fix up function order
- Add better comments
- Continue to reformat code
- Variable renaming operation
