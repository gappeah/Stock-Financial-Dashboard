# Import libraies and modules
import pandas_datareader as pdr

import numpy as np
import pandas as pd

import math
import datetime as dt

import yfinance as yf

from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models import TextInput, Button, DatePicker, MultiChoice
from bokeh.layouts import column, row

def load_data(symbol, start_date, end_date):
    df1 = yf.download(symbol, start_date, end_date)
    df2 = yf.download(symbol, start_date, end_date)
    return df1, df2


def plot_data(data, indicator, sync_axis=None):
    pass


def on_button_clicked(ticker1, ticker2, start, end, indicators):
    pass

stock1_text = TextInput(title="Stock 1")
stock2_text = TextInput(title="Stock 2")
date_picker_from = DatePicker(title="Start Date", value="2020-01-01", min_date="2000-01-01", max_date=dt.datetime.now().strftime("%Y-%m-%d"))
date_picker_to = DatePicker(title="End Date", value="2020-02-01", min_date="2000-01-01", max_date=dt.datetime.now().strftime("%Y-%m-%d"))

indicator_choice = MultiChoice(options=["100 Day SMA", "30 Day SMA", "Linear Regression"])


load_button = Button(label="Load Data", button_type="success")

load_button.on_click = (lambda(label="Load Data", button_type="success")