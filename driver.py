from bokeh.plotting import figure, output_file, show, save
from bokeh.layouts import row

import pandas as pd
import os


def call_input(input_path="input/SettledActivity_092017_092017.csv"):
    transactions = pd.read_csv(input_path, parse_dates=True, infer_datetime_format=True, index_col=0)
    pricing = pd.read_csv("input/sec data.csv", parse_dates=True, infer_datetime_format=True, index_col=0)
    # pricing = pd.read_csv('input/sec data.csv')

    spy = pricing['SPY'] #frame
    dates = pricing.index
    return dates, spy


def graph_plot(df_input, data_col, save_name='plot test.html'):
    """
    :param df_input: Timeseries dataframe with datetime index values to be plotted.
    :param data_col: The name of the column with data to be plotted.
    :param save_name: Name by which to save the plot.
    :return:
    """
    width = 500
    height = 400
    dir = os.getcwd()
    plot_title = "SPY Price"

    x, y = call_input()

    fig = figure(plot_width=width, plot_height=height, x_axis_type='datetime')
    fig.line(x, y, line_width=2)  # Can pass x, y values as first and second args.
    output_file(save_name, title=plot_title)
    save(fig, dir+"\output\\"+save_name)


def generate_id(id_type):
    """ Generate a unique ID for object of type specified in id_typ parameter.
    :param id_type: The type of object for which to generate an id.
    :return: Unique ID (int) for object.
    """

    # TODO: Implement actual id-generating logic.
    return 1


class portfolio:
    def __init__(self):
        self.transactions = pd.DataFrame()
        self.id = generate_id("portfolio")

    def build_transactions(self, transaction_input, input_type="RH"):
        """

        :param transaction_input:
        :param input_type: Code for the type of transactions to import.
        :return:
        """
        transactions = pd.DataFrame()
        transactions = pd.read_csv(input_path, parse_dates=True, infer_datetime_format=True, index_col=0)


if __name__ == "__main__":
    graph_plot(None, None)
