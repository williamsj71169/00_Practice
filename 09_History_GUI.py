from tkinter import *
from functools import partial  # to prevent unwanted windows
import random

if __name__ == '__main__':
    class Converter:
        def __init__(self):

            # formatting variables..
            background_colour = "light blue"

            # in actual program this is blank an dis populated with user calculations
            self.all_calc_list = ['hello']

            # Converter Main Screen GUI
            self.converter_frame = Frame(width=600, height=600, bg=background_colour,
                                         pady=10)
            self.converter_frame.grid()

            # Temperature Conversion Heading (row 0)
            self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                              font=("Arial", "16", "bold"),
                                              bg=background_colour, padx=10, pady=10)

            self.temp_converter_label.grid(row=0)

            # History Button (row 1)
            self.history_button = Button(self.converter_frame, text="History",
                                         font=("Arial", "14"),
                                         padx=10, pady=10, command=self.history)

            self.history_button.grid(row=1)

        def history(self):
            print("You asked for history")
            get_history = History(self)
            get_history.history_text.configure(text="History text goes here")


class History:
    def __init__(self, partner):

        background = "#a9ef99"  # pale orange

        # disable history button
        partner.history_button.config(state=DISABLED)

        # sets up child window (ie: history box)
        self.history_box = Toplevel()

        # if users pres cross at top, closes history and 'releases' history button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        # set up GUI frame
        self.history_frame = Frame(self.history_box, width=300, bg=background)
        self.history_frame.grid()

        # set ip History heading (row 0)
        self.how_heading = Label(self.history_frame, text="Calculation History",
                                 font="arial 19 bold", bg=background)
        self.how_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame,
                                  text="Here are your most recent calculations, "
                                       "Please ues the export button to create "
                                       "a text file of all your calculations for "
                                       "this session", wrap=250,
                                  font="arial 10 italic", fg="maroon",
                                  justify=LEFT, width=40, bg=background,
                                  padx=10, pady=10)
        self.history_text.grid(row=1)

        # history output goes here (row 2)

        # export / dismiss button frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # export button
        self.export_button


    def close_history(self, partner):
        # put history button back to normal
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
