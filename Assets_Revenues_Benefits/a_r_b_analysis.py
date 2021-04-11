"""This is the class to manage assets, benefits and revenues and gives back user friendly data for the
dashboard"""

import datetime
import numpy
import pandas
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class DataAnalysis:

    # We load the assets, revenues and benefits classes
    def __init__(self):
        self.revenues = pandas.read_excel('Assets_Revenues_Benefits/assets_data.xlsx', sheet_name='Revenues')
        self.assets = pandas.read_excel('Assets_Revenues_Benefits/assets_data.xlsx', sheet_name='Assets')
        self.benefits = pandas.read_excel('Assets_Revenues_Benefits/assets_data.xlsx', sheet_name='Benefits')

    # Method to get a dictionary with the total sum of all types of revenues
    def get_total_revenues_by_type(self):
        types_revenues = self.revenues['Description'].unique()
        revenues_by_category = dict()
        # Getting the sum of revenues for each category
        for revenue_type in types_revenues:
            revenues_by_category[revenue_type] = self.revenues['Income_Value'][self.revenues['Description'] ==
                                                                               revenue_type].sum()
        return revenues_by_category

    # Get the sum of all assets by category
    def get_total_assets_by_type(self, month=None):
        types_assets = self.assets['Description'].unique()
        # Get each unique time period in a datetime format and target for the designated month
        assets_by_category = dict()
        for asset_type in types_assets:
            assets_by_category[asset_type] = self.assets['Value'][(self.assets['Description'] ==
                                                                  asset_type)][-1:]
        return assets_by_category

    # Prepare revenues in a format that will be displayed by matplotlib on the dashboard. This function will take
    # the chronological progress of each type of income separately
    def create_presentation_format_revenues(self, specific_revenue):
        data = self.revenues[self.revenues['Description'] == specific_revenue]
        revenue_data = pandas.DataFrame(data, columns=['Timeline', 'Income_Value'])
        return revenue_data

    # Helper method to convert data from series to non mutable objects
    def convert_value_from_series(self, value, value_type=None):
        if value_type == 'float':
            return value.astype('float64')
        elif value_type == 'integer':
            return value.astype('int64')
        elif value_type == 'date':
            new_value = numpy.datetime64(value)
            return new_value.astype(datetime.datetime)
        else:
            return str(value)

    # Method to return the dataframes for each type of data
    def get_income_data(self, type_income=None):
        if type_income == 'revenues':
            self.revenues['Timeline'] = pd.to_datetime(self.revenues['Timeline']).dt.date
            return self.revenues
        elif type_income == 'assets':
            self.assets['Timeline'] = pd.to_datetime(self.revenues['Timeline']).dt.date
            return self.assets
        else:
            self.benefits['Timeline'] = pd.to_datetime(self.revenues['Timeline']).dt.date
            return self.benefits


