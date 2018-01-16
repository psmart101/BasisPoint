from bokeh.plotting import figure, output_file, show, save
from bokeh.layouts import row

import pandas as pd
import os


def call_input(input_path="input/SettledActivity_092017_092017.csv"):
    transactions = pd.read_csv(input_path, parse_dates=True, infer_datetime_format=True, index_col=0)
    pricing = pd.read_csv("input/sec data.csv", parse_dates=True, infer_datetime_format=True, index_col=0)
    pricing = pricing['SPY']
    return pricing


def graph_plot(df_input, data_col, save_name='plot test'):
    """
    :param df_input: Timeseries dataframe with datetime index values to be plotted.
    :param data_col: The name of the column with data to be plotted.
    :param save_name: Name by which to save the plot.
    :return:
    """
    width = 500
    height = 400

    fig = figure(plot_width=width, plot_height=height, x_axis_type='datetime')
    fig.line(x='datetime', line_width=2)  # Can pass x, y values as first and second args.


    return