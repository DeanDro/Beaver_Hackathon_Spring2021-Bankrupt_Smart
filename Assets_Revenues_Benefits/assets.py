"""Class to hold all assets in your portfolio"""

from tkinter import messagebox


class Assets:

    # Costructor method
    def __init__(self):
        self.total_assets_value = 0
        self.portfolio_assets = dict()
        self.credit_cards = dict()

    # Method to add assets in portfolio
    def add_asset(self, month_year, asset_description, asset_value):
        assets_input = dict()
        monthly_input = dict()
        try:
            self.total_assets_value += asset_value
            assets_input['Description'] = asset_description
            assets_input['Value'] = asset_value
            monthly_input[asset_description] = assets_input
            self.portfolio_assets[month_year] = monthly_input
        except ValueError:
            messagebox.showerror('Error', 'Key value error')

    # Method to remove assets
    def remove_asset(self, month_year, asset_description):
        try:
             del self.portfolio_assets[month_year][asset_description]
        except ValueError:
            messagebox.showerror('Key Error', 'This asset doesn\'t exists in your portfolio')

