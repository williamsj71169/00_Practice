from tkinter import *
from functools import partial  # to prevent unwanted windows
import random


class Converter:
    def __init__(self):

        # formatting variables
        background_colour = "light blue"

        # converter Frame
        self.converter_frame = Frame(width=300, height=300, bg=background_colour, pady=10)
        self.converter_frame.grid()

        # temperature converter heading (row 0)
        self.temp_heading_label = Label(self.converter_frame, text="Temperature Converter", font="Arial 19 bold",
                                        bg=background_colour, padx=10, pady=10)
        self.temp_heading_label.grid(row=0)

        # Export Button (row 1)
        self.export_button = Button(self.converter_frame, text="Export", font=("Arial", "14"),
                                    padx=10, pady=10, command=self.export)
        self.export_button.grid(row=1)

    def export(self):
        get_export = Export(self)


class Export:
    def __init__(self, partner):

        background = "#a9ef99"   # pale green

        # disabled export button
        partner.export_button.config(state=DISABLED)

        # sets up child window
        self.export_box = Toplevel()

        # if user press cross at top, closes export and 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW',
                                 partial(self.close_export, partner))

        # set up gui frame
        self.export_frame = Frame(self.export_box, width=300, bg=background)
        self.export_frame.grid()

        # set up export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export / Instructions",
                                 font="arial 14 bold", bg=background)
        self.how_heading.grid(row=0)

        # export instructions
        self.export_text = Label(self.export_frame, justify=LEFT, width=40, bg=background,
                                 wrap=250, text="Enter a filename in the box below and press"
                                                "the Save button to save your calculation"
                                                "history to a text file.")
        self.export_text.grid(row=1)

        # warning text (label, row 2)
        self.export_text = Label(self.export_frame, text="If the filename you enter below already exists, "
                                                         "its content will be replaced with your calculation history",
                                 justify=LEFT, bg="#ffafaf", fg="maroon", font="Arial 10 italic",
                                 wrap=225, padx=10, pady=10)
        self.export_text.grid(row=2, pady=10)

        # filename entry box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20, font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, column=0)

        # Save / cancel frame (row4)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and Cancel Buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save")
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def close_export(self, partner):
        # put export button back to normal
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
