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
    df = data
    gain = df.Close > df.Open
    loss = df.Open > df.Close
    width = 12 * 60 * 60 * 1000  # half day in ms
    


def on_button_clicked(ticker1, ticker2, start, end, indicators):
    df1, df2 = load_data(ticker1, ticker2, start, end)
    p1 = plot_data(df1, indicators)
    p2 = plot_data(df2, indicators, sync_axis=p1.x_range)
    curdoc.clear()
    curdoc.add_root(layout)
    curdoc.add_root(row(p1, p2))


stock1_text = TextInput(title="Stock 1")
stock2_text = TextInput(title="Stock 2")
date_picker_from = DatePicker(title="Start Date", value="2020-01-01", min_date="2000-01-01", max_date=dt.datetime.now().strftime("%Y-%m-%d"))
date_picker_to = DatePicker(title="End Date", value="2020-02-01", min_date="2000-01-01", max_date=dt.datetime.now().strftime("%Y-%m-%d"))

indicator_choice = MultiChoice(options=["100 Day SMA", "30 Day SMA", "Linear Regression"])


load_button = Button(label="Load Data", button_type="success")

load_button.on_click = (lambda: on_button_clicked(stock1_text.value, stock2_text.value, date_picker_from.value, date_picker_to.value, indicator_choice.value))

layout = column(stock1_text, stock2_text, date_picker_from, date_picker_to, indicator_choice, load_button)

curdoc().clear()
curdoc().add_root(layout)