"""This is the class to manage assets, benefits and revenues and gives back user friendly data for the
dashboard"""
import datetime

import numpy
import pandas
from assets import Assets
from benefits import Benefits
from revenues import Revenues


class DataAnalysis:

    # We load the assets, revenues and benefits classes
    def __init__(self):
        self.revenues = pandas.read_excel('assets_data.xlsx', sheet_name='Revenues')
        self.assets = pandas.read_excel('assets_data.xlsx', sheet_name='Assets')
        self.benefits = pandas.read_excel('assets_data.xlsx', sheet_name='Benefits')

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


test = DataAnalysis()
test.get_total_assets_by_type()