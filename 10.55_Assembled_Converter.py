from tkinter import *
from functools import partial  # to prevent unwanted windows
import random

if __name__ == '__main__':
    class Converter:
        def __init__(self):

            # formatting variables
            background_colour = "light blue"

            # initialise list to hold calculation history
            self.all_calc_list = []

            # converter Frame
            self.converter_frame = Frame(bg=background_colour, pady=10)
            self.converter_frame.grid()

            # temperature converter heading (row 0)
            self.temp_heading_label = Label(self.converter_frame, text="Temperature Converter", font="Arial 19 bold",
                                            bg=background_colour, padx=10, pady=10)
            self.temp_heading_label.grid(row=0)

            # user instructions (row 1)
            self.temp_instructions_label = Label(self.converter_frame,
                                                 text="Type in the amount to be converted and push"
                                                      "one of the buttons below...",
                                                 font="Arial 10 italic", wrap=290, justify=LEFT,
                                                 bg=background_colour, padx=10, pady=10)
            self.temp_instructions_label.grid(row=1)

            # temperature entry box (row 2)
            self.to_convert_entry = Entry(self.converter_frame, width=20, font="Arial 14 bold")
            self.to_convert_entry.grid(row=2)

            # conversion buttons frame (row 3)
            self.conversion_buttons_frame = Frame(self.converter_frame)
            self.conversion_buttons_frame.grid(row=3, pady=10)

            self.to_c_button = Button(self.conversion_buttons_frame,
                                      text="To Centigrade", font="Arial 10 bold",
                                      bg="yellow", padx=10, pady=10,
                                      command=lambda: self.temp_convert(-459))
            self.to_c_button.grid(row=0, column=0)

            self.to_f_button = Button(self.conversion_buttons_frame,
                                      text="To Fahrenheit", font="Arial 10 bold",
                                      bg="#ff007f", padx=10, pady=10,
                                      command=lambda: self.temp_convert(-273))
            self.to_f_button.grid(row=0, column=1)

            # answer label (row 4)
            self.converted_label = Label(self.converter_frame, font="Arial 14 bold",
                                         fg="purple", bg=background_colour, pady=10, text="Conversion goes here")
            self.converted_label.grid(row=4)

            # history / help button frame (row 5)
            self.hist_help_frame = Frame(self.converter_frame)
            self.hist_help_frame.grid(row=5, pady=10)

            self.calc_history_button = Button(self.hist_help_frame, font="arial 12 bold",
                                              text="Calculation History", width=15,
                                              command=lambda: self.history(self.all_calc_list))
            self.calc_history_button.grid(row=0, column=0)

            if len(self.all_calc_list) == 0:
                self.calc_history_button.config(state=DISABLED)

            self.help_button = Button(self.hist_help_frame, text="Help",
                                      font=("Arial 12 bold"),
                                      command=self.help)
            self.help_button.grid(row=0, column=1)

        def history(self, calc_history):
            History(self, calc_history)

        def help(self):
            print("You asked for help")
            get_help = Help(self)
            get_help.help_text.configure(text="Help text goes here")

        def temp_convert(self, low):
            print(low)

            error = "#ffafaf"  # pale pink background for when entry box has errors

            # retrieve amount entered into entry field
            to_convert = self.to_convert_entry.get()

            try:
                to_convert = float(to_convert)
                has_errors = "no"

                # check and convert to F
                if low == -273 and to_convert >= low:
                    fahrenheit = (to_convert * 9 / 5 + 32)
                    to_convert = self.round_it(to_convert)
                    fahrenheit = self.round_it(fahrenheit)
                    answer = "{} degrees C is {} degrees F".format(to_convert, fahrenheit)

                # check and convert to C
                elif low == -459 and to_convert >= low:
                    celsius = (to_convert - 32) * 5 / 9
                    to_convert = self.round_it(to_convert)
                    celsius = self.round_it(celsius)
                    answer = "{} degrees F is {} degrees C".format(to_convert, celsius)

                else:
                    # Input is invalid (too cold)!!
                    answer = "Too Cold!"
                    has_errors = "yes"

                # display answer
                if has_errors == "no":
                    self.converted_label.configure(text=answer, fg="blue")
                    self.to_convert_entry.configure(bg="white")
                else:
                    self.converted_label.configure(text=answer, fg="red")
                    self.to_convert_entry.configure(bg=error)

                # add answer to list for history
                if has_errors != "yes":
                    self.all_calc_list.append(answer)
                    print(self.all_calc_list)
                    self.calc_history_button.config(state=NORMAL)

            except ValueError:
                self.converted_label.configure(text="Enter a number!!", fg="red")
                self.to_convert_entry.configure(bg=error)

        def round_it(self, to_round):
            if to_round % 1 == 0:
                rounded = int(to_round)
            else:
                rounded = round(to_round, 1)

            return rounded


class History:
    def __init__(self, partner, calc_history):

        background = "#a9ef99"  # pale orange

        # disable history button
        partner.calc_history_button.config(state=DISABLED)

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

        # Generate string from list of calculations
        history_string = ""

        if len(calc_history) >= 7:
            for item in range(0, 7):
                history_string += calc_history[len(calc_history)
                                               - item - 1]+"\n"

        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history) -
                                               calc_history.index(item) - 1] + "\n"
                self.history_text.config(text="Here is your calculation history."
                                              "You can use the export button to save "
                                              "this data to a text file if you want.")

        # label to display calculation history to user
        self.calc_label = Label(self.history_frame, text=history_string, bg=background,
                                font="Arial 12", justify=LEFT)
        self.calc_label.grid(row=2)

        # export / dismiss button frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # export button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="Arial 12 bold")
        self.export_button.grid(row=0, column=0)

        # Dismiss Button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                     font="Arial 12 bold", command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1)

    def close_history(self, partner):
        # put history button back to normal
        partner.calc_history_button.config(state=NORMAL)
        self.history_box.destroy()


class Help:
    def __init__(self, partner):
        background = "orange"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # sets up child window (ie: help box)
        self.help_box = Toplevel()

        # if users pres cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # set up GUI frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        # set ip Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                 font="arial 14 bold", bg=background)
        self.how_heading.grid(row=0)

        # help text (label, row 1)
        self.help_text = Label(self.help_frame, text="",
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        # dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                  width=10, bg="orange", font="arial 10 bold",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # put help button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
