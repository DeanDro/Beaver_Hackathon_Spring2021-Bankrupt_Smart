"""Revenues class is tracking all incomes generated from the user and feeds total income in the
recommendations output"""

from tkinter import messagebox


class Revenues:

    # Constructor class
    def __init__(self):
        self.revenues_dict = dict()
        self.total_revenues = 0

    # Add income in the revenues dictionary
    def add_revenue(self, income_value, income_description, frequency, timeline):
        income_input = dict()
        try:
            income_input['Description'] = income_description
            income_input['Income'] = float(income_value)
            income_input['Frequency'] = frequency
            income_input['Timeline'] = int(timeline)
        except ValueError:
            print('You entered wrong value')
            messagebox.showerror('Wrong value', 'You entered an incompatible value')

