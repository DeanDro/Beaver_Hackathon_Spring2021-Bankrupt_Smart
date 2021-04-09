"""Class to hold all assets in your portfolio"""

from tkinter import messagebox


class Assets:

    # Costructor method
    def __init__(self):
        self.total_assets_value = 0
        self.total_cashflow_assets = 0
        self.portfolio_assets = dict()
        self.credit_cards = dict()

    # Method to add assets in portfolio
    def add_asset(self, asset_description, asset_value, cashflow):
        assets_input = dict()
        try:
            self.total_assets_value += asset_value
            self.total_cashflow_assets += cashflow
            assets_input['Description'] = asset_description
            assets_input['Value'] = asset_value
            assets_input['Cashflow'] = cashflow
            self.portfolio_assets[asset_description] = assets_input
        except ValueError:
            messagebox.showerror('Error', 'Key value error')

    # Method to remove assets
    def remove_asset(self, asset_description):
        try:
            asset = self.portfolio_assets[asset_description]
            value = asset['Value']
            cash_flow = asset['Cashflow']
            del self.portfolio_assets[asset_description]
            self.total_cashflow_assets -= cash_flow
            self.total_assets_value -= value
        except ValueError:
            messagebox.showerror('Key Error', 'This asset doesn\'t exists in your portfolio')

