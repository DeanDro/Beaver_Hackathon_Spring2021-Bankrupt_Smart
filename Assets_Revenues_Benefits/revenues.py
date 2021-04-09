"""Revenues class is tracking all incomes generated from the user and feeds total income in the
recommendations output"""

from tkinter import messagebox


class Revenues:

    # Constructor class
    def __init__(self):
        self.revenues_dict = dict()
        self.total_revenues = 0

    # Add income in the revenues dictionary
    def add_revenue(self, income_value, income_description, frequency, timeline, category_revenue):
        income_input = dict()
        try:
            income_input['Description'] = income_description
            income_input['Income'] = float(income_value)
            income_input['Frequency'] = frequency
            income_input['Timeline'] = int(timeline)
            income_input['Category'] = category_revenue
            self.revenues_dict[income_description] = income_input
        except ValueError:
            print('You entered wrong value')
            messagebox.showerror('Wrong value', 'You entered an incompatible value')

    # Method to remove revenues
    def remove_revenues(self, income_description):
        try:
            del self.revenues_dict[income_description]
        except ValueError:
            messagebox.showerror('Key error', 'No such income currently exists in your records')

    # Method to calculate total revenues
    def get_total_monthly_revenues(self):
        try:
            for key in self.revenues_dict.keys():
                current_record = self.revenues_dict[key]
                self.total_revenues += current_record['Income']
        except ValueError:
            messagebox.showerror('Error', 'An error occurred during calculation of total revenues')
