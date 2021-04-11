"""Class to analyze all expenses"""

import pandas as pd
from tkinter import messagebox


class ExpensesAnalysis:

    def __init__(self):
        self.bills = pd.read_excel('Bills_Debt/bills_debt_data.xlsx', sheet_name='Bills')
        self.debt = pd.read_excel('Bills_Debt/bills_debt_data.xlsx', sheet_name='Debt')

    # Method to return the dataframe with bills or debt
    def get_type_expense(self, type_expense):
        try:
            if type_expense == 'bills':
                self.bills['Month_Year'] = pd.to_datetime(self.bills['Month_Year']).dt.date
                return self.bills
            else:
                self.debt['Month_Year'] = pd.to_datetime(self.debt['Month_Year']).dt.date
                return self.debt
        except FileNotFoundError:
                messagebox.showerror('Error', 'File not found')
