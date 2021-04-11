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
        self.master.title('Bankrupt Smart')
        self.master.geometry('1200x600')
        self.wrapper1 = tk.LabelFrame(self.master)
        self.canvas = self.create_canvas(self.wrapper1)
        self.scroller = self.create_scrollbar(self.wrapper1, self.canvas, tk.VERTICAL)
        self.canvas.configure(yscrollcommand=self.scroller.set)
        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor='nw')
        self.wrapper1.pack(fill='both', expand='yes', padx=10, pady=10)
        self.create_revenues_charts('revenues', 'Timeline', 'Income_Value', 'Monthly Revenues', 'Income',
                                    'Month', 0, 1)
        self.create_revenues_charts('assets', 'Time', 'Value', 'Total Assets Value', 'Assets Value',
                                    'Month', 0, 2)
        self.create_expenses_charts('bills', 'Month_Year', 'Monthly Cost', 'Monthly Bills', 'Monthly Cost',
                                    'Month', 1, 1)
        self.create_expenses_charts('debt', 'Month_Year', 'Total Cost', 'Total Debt', 'Monthly_Cost', 'Month',
                                    2, 1)

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
    def create_revenues_charts(self, category, x_val, y_val, chart_title, x_label, y_label, col_pos, row_pos):
        data = self.revenues.get_income_data(category)
        figure = plt.Figure(figsize=(4, 4), dpi=100)
        y_value = data[y_val]
        x_value = data[x_val]

        # Plotting the graph
        graph = figure.add_subplot(111)
        graph.bar(x_value, y_value, 10)
        graph.set_xlabel(x_label)
        graph.set_ylabel(y_label)
        graph.set_title(chart_title)
        graph.grid()

        # Adding everything on canvas
        chart = FigureCanvasTkAgg(figure, master=self.canvas)
        chart.draw()
        chart.get_tk_widget().grid(column=col_pos, row=row_pos, padx=10, pady=10)

    # Create expenses report
    def create_expenses_charts(self, category, x_val, y_val, chart_title, x_label, y_label, col_pos, row_pos):
        data = self.expenses.get_type_expense(category)
        figure = plt.Figure(figsize=(4, 4), dpi=100)
        y_values = data[y_val]
        x_values = data[x_val]

        # Plotting the graph
        graph = figure.add_subplot(111)
        graph.bar(x_values, y_values, 10)
        graph.set_xlabel(x_label)
        graph.set_ylabel(y_label)
        graph.set_title(chart_title)
        graph.grid()

        # adding everything in the canvas
        chart = FigureCanvasTkAgg(figure, master=self.canvas)
        chart.draw()
        chart.get_tk_widget().grid(column=col_pos, row=row_pos, padx=10, pady=10)


root = tk.Tk()
test = MainApp(root)
test.mainloop()
