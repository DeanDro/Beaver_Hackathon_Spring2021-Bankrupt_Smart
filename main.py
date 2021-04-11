# Author: Konstantinos Drosos
# Date: 04/08/2021
# Description: Bankrupt_Smart is a personal finance assistant created for the purpose of participating
#              in the Beaver Hack Spring 2021 Hackathon

import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Assets_Revenues_Benefits.a_r_b_analysis import DataAnalysis
from Bills_Debt.b_d_analysis import ExpensesAnalysis


class BankruptSmart(tk.Frame):

    # Initialize the app
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame2 = tk.Frame(self.master)
        self.frame.grid(column=1, row=1)
        self.frame2.grid(column=1, row=2)
        self.graphics_design()
        self.revenue_data = DataAnalysis()
        self.expenses_data = ExpensesAnalysis()
        self.design_revenue_charts('revenues')
        self.design_assets_charts()
        self.design_benefits_charts()
        self.design_bills_charts()
        self.design_debt_charts()

    # Method to control colors
    def graphics_design(self):
        self.master.geometry('1000x600')
        # create an rbg color for the window background
        background_color = '#%02x%02x%02x' % (242, 240, 240)
        self.frame.configure(background=background_color)
        self.master.title('Bankrupt Smart')

    # Method to design the revenue charts
    def design_revenue_charts(self, wealth):
        data = self.revenue_data.get_income_data(wealth)
        figure = plt.Figure(figsize=(4, 4), dpi=100)
        ax1 = figure.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure, self.frame)
        bar1.get_tk_widget().grid(column=0, row=0)
        df1 = data[['Timeline', 'Income_Value']].groupby('Timeline').sum()
        df1.plot(kind='bar', legend=True, ax=ax1)
        ax1.set_title('Monthly Income')

    # Method to design the assets charts
    def design_assets_charts(self):
        data = self.revenue_data.get_income_data('assets')
        figure = plt.Figure(figsize=(4, 4), dpi=100)
        ax1 = figure.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure, self.frame)
        bar1.get_tk_widget().grid(column=1, row=0)
        df1 = data[['Timeline', 'Value']].groupby('Timeline').sum()
        df1.plot(kind='line', legend=True, ax=ax1)
        ax1.set_title('Value of Assets')

    # Method to design the benefits charts
    def design_benefits_charts(self):
        data = self.revenue_data.get_income_data()
        figure = plt.Figure(figsize=(4, 4), dpi=100)
        ax1 = figure.add_subplot(111)
        bar = FigureCanvasTkAgg(figure, self.frame)
        bar.get_tk_widget().grid(column=2, row=0)
        df1 = data[['Time', 'Value']].groupby('Time').sum()
        df1.plot(kind='bar', legend=True, ax=ax1)
        ax1.set_title('Value of Benefits')

    # Method to plot the bills chart on the frame
    def design_bills_charts(self):
        data = self.expenses_data.get_type_expense('bills')
        figure = plt.Figure(figsize=(4, 4), dpi=100)
        ax1 = figure.subplots()
        bar = FigureCanvasTkAgg(figure, self.frame2)
        bar.get_tk_widget().grid(column=0, row=0)
        df1 = data[['Month_Year', 'Monthly Cost']].groupby('Month_Year').sum()
        df1.plot(kind='bar', legend=True, ax=ax1)
        ax1.set_title('Value of Bills')

    # Method to plot the debt chart
    def design_debt_charts(self):
        data = self.expenses_data.get_type_expense('debt')
        figure = plt.Figure(figsize=(4, 4), dpi=100)
        ax1 = figure.subplots()
        bar = FigureCanvasTkAgg(figure, self.frame2)
        bar.get_tk_widget().grid(column=1, row=0)
        df1 = data[['Month_Year', 'Total Cost']].groupby('Month_Year').sum()
        df1.plot(kind='line', legend=True, ax=ax1)
        ax1.set_title('Value of Debt')


root = tk.Tk()
test_app = BankruptSmart(root)
test_app.mainloop()
