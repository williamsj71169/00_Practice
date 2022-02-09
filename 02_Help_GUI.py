from tkinter import *
from functools import partial  # to prevent unwanted windows

import random

if __name__ == '__main__':
    class Converter:
        def __init__(self):

            # formatting variables..
            background_colour = "light blue"

            # Converter Main Screen GUI
            self.converter_frame = Frame(width=600, height = 600, bg=background_colour)
            self.converter_frame.grid()

            # Temperature Conversion Heading (row 0)
            self.temp_converter_label = Label(text="Temperature Converter", font=("Arial", "16", "bold"),
                                              bg=background_colour, padx=10, pady=10)

            self.temp_converter_label.grid(row=0)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
