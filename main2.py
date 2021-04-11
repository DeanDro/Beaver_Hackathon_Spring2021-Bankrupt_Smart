"""Testing file"""

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Assets_Revenues_Benefits.a_r_b_analysis import DataAnalysis
from Bills_Debt.b_d_analysis import ExpensesAnalysis


class MainApp(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.revenues = DataAnalysis()
        self.expenses = ExpensesAnalysis()
        self.master = master
        self.master.geometry('800x600')
        self.wrapper1 = tk.LabelFrame(self.master)
        self.canvas = self.create_canvas(self.wrapper1)
        self.scroller = self.create_scrollbar(self.wrapper1, self.canvas, tk.VERTICAL)
        self.canvas.configure(yscrollcommand=self.scroller.set)
        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor='nw')
        self.wrapper1.pack(fill='both', expand='yes', padx=10, pady=10)
        self.create_revenues_charts()

    # Create a canvas and add a scroller
    def create_canvas(self, label_frame):
        my_canvas = tk.Canvas(label_frame)
        my_canvas.pack(side=tk.LEFT)
        return my_canvas

    # Add scrollbar to canvas
    def create_scrollbar(self, label_frame, canvas, orientation):
        scroll = ttk.Scrollbar(label_frame, orient=orientation, command=canvas)
        scroll.pack(side=tk.RIGHT, fill='y')
        return scroll

    # Create the revenues charts
    def create_revenues_charts(self):
        data = self.revenues.get_income_data('revenues')
        figure = plt.Figure(figsize=(4, 4), dpi=100)
        ax1 = figure.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure, self.frame)
        bar1.get_tk_widget().pack(side=tk.LEFT, fill='y')
        df1 = data[['Timeline', 'Income_Value']].groupby('Timeline').sum()
        df1.plot(kind='bar', legend=True, ax=ax1)
        ax1.set_title('Monthly Income')


root = tk.Tk()
test = MainApp(root)
test.mainloop()
