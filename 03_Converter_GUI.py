from tkinter import *
from functools import partial  # to prevent unwanted windows
import random


class Converter:
    def __init__(self):

        # formatting variables
        background_colour = "light blue"

        # converter Frame
        self.converter_frame = Frame(width=300, bg=background_colour, pady=10)
        self.converter_frame.grid()

        # temperature converter heading (row 0)
        self.temp_heading_label = Label(self.converter_frame, text="Temperature Converter", font="Arial 16 bold",
                                        bg=background_colour, padx=10, pady=10)

        # user instructions (row 1)

        # temperature entry box (row 2)

        # conversion buttons frame (row 3)

        # answer label (row 4)

        # history / help button frame (row 5)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
