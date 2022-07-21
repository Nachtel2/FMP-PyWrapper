import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

def get_jsonparsed_data(url): #Recommended function used by base FMP API
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)



class Symbol:
    def __init__(self, symbol, api_key):
        self.symbol = symbol
        self.api_key = api_key
        self.base_url = 'https://financialmodelingprep.com/api'

    def period_filter(self, period):
        if period != 'quarter':
            period = '' #If the default choice is not true, then the only other option is annual, which is the default if you don't specify in the url.
        else:
            period = 'period=quarter&' #Transforming the choice into a shape I can feed to the url.

        return period

class Stock(Symbol):
    def __init__(self, symbol, api_key):
        super().__init__(symbol, api_key)

    def financial_statements(self, period='quarter', limit='400', data_type=''):
        period = self.period_filter(period)

        if data_type == 'csv': 
            data_type == '&datatype=csv' #Transforming the choice into a shape I can feed to the url.

        url = f'{self.base_url}/v3/income-statement/{self.symbol}?{period}limit={limit}{data_type}&apikey={self.api_key}'
        data = get_jsonparsed_data(url)
        return data

    def sales_revenue_by_segments(self, period='quarter'):
        period = self.period_filter(period)

        url = f'{self.base_url}/v4/revenue-product-segmentation?symbol={self.symbol}&{period}structure=flat&apikey={self.api_key}'
        data = get_jsonparsed_data(url)
        return data

    def revenue_geographic_by_segments(self, period='quarter'):
        period = self.period_filter(period)

        url = f'{self.base_url}/v4/revenue-geographic-segmentation?symbol={self.symbol}&{period}structure=flat&apikey={self.api_key}'
        data = get_jsonparsed_data(url)
        return data

    def quarterly_earnings_reports(self, year='2022', period='Q1'):

        url = f'{self.base_url}/v4/financial-reports-json?symbol={self.symbol}&year={year}&period={period}&apikey={self.api_key}'
        data = get_jsonparsed_data(url)
        return data


    def shares_float(self):

        url = f'{self.base_url}/v4/shares_float?symbol={self.symbol}&apikey={self.api_key}'
        data = get_jsonparsed_data(url)
        return data

    def quote(self):

        url = f'{self.base_url}/v3/quote/{self.symbol}?apikey={self.api_key}'
        data = get_jsonparsed_data(url)
        return data
    def stock_price(self):

        url = f'{self.base_url}/v3/quote-short/{self.symbol}?apikey={self.api_key}'
        data = get_jsonparsed_data(url)
        return data

    def historical_price(self, period="1min"):

        url = f'{self.base_url}/v3/historical-chart/{period}/{self.symbol}?apikey={self.api_key}'
        data = get_jsonparsed_data(url)
        return data
