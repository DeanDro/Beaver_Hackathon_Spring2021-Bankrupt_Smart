# Author: Konstantinos Drosos
# Date: 04/08/2021
# Description: Bankrupt_Smart is a smart personal finance assistant created for the purpose of participating
#              in the Beaver Hack Spring 2021 Hackathon

import tkinter as tk


class BankruptSmart(tk.Frame):

    # Initialize the app
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.graphics_design()

    # Method to control colors
    def graphics_design(self):
        self.master.geometry('1000x600')
        # create an rbg color for the window background
        background_color = '#%02x%02x%02x' % (242, 240, 240)
        self.master.configure(background=background_color)
        self.master.title('Bankrupt Smart')


root = tk.Tk()
test_app = BankruptSmart(root)
test_app.mainloop()
