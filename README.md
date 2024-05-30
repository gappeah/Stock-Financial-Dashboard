#  Stock Financial Dashboard 

This is a Bokeh application that allows you to visualise stock data for two stocks of your choice. You can select the stock tickers, date range, and technical indicators to display on the chart.

## Features

- View candlestick charts for two stocks side by side
- Select a custom date range
- Display technical indicators:
  - 30-day Simple Moving Average (SMA)
  - 100-day Simple Moving Average (SMA)
  - Linear Regression trend line
- Interactive panning and zooming on the chart

## Requirements

- Python 3.x
- pandas
- numpy
- bokeh
- yfinance
- pandas_datareader 
- math
- datetime
- setuptools


## Setup

It's recommended to create a virtual environment to manage the project dependencies. Follow these steps:

1. Create a new virtual environment: `python -m venv venv`.
2. Activate the virtual environment: `source venv/bin/activate`.
3. Install dependencies via pip.

## Usage

1. Clone or download the repository.
2. Navigate to the project directory.
3. Run the `main.py` script:
4. The application will open in your default web browser.
5. Enter the stock tickers for the two stocks you want to analyze.
6. Select the start and end dates for the date range.
7. Choose the technical indicators you want to display on the chart.
8. Click the "Load Data" button to fetch the stock data and generate the chart.

## Code Structure

- `main.py`: The main script that runs the Bokeh application.
- `load_data` function: Fetches stock data from Yahoo Finance using the `yfinance` library.
- `plot_data` function: Generates the candlestick chart and plots the selected technical indicators.
- `on_button_clicked` function: Handles the "Load Data" button click event and updates the chart with the user's selections.

