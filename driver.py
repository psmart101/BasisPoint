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


class Portfolio:
    def __init__(self):
        self.transactions = pd.DataFrame()
        self.id = generate_id("portfolio")

    def build_transactions(self, transaction_input, input_type="ML"):
        """Generate transactions from iterable nested input and add to portfolio as attribute.
        :param transaction_input: nested list-like (read_csv format) to be processed as transactions.
        :param input_type: Code for the type of transactions to import.
        :return:
        """
        transactions = pd.DataFrame()
        # TODO: Implement support for input formats other than list.
        if type(transaction_input) == list:
            transactions = pd.DataFrame(transaction_input)
            # transactions = pd.read_csv(input_path, parse_dates=True, infer_datetime_format=True, index_col=0)

        if input_type == "ML":
            transactions = pd.DataFrame.from_records(transaction_input[1:], index='Trade Date', columns=transaction_input[0])
            transactions.index = transactions.index.to_datetime()

            # TODO: Setup exception handlers for case when keywords do not have trailing space(s)
            # Rename columns to standardized format
            transactions.rename(index=str, inplace=True,
                                columns={"Description 1 ": "Direction",
                                         "Description 1": "Direction",
                                         "Symbol/CUSIP #": "Symbol",
                                         "Price ($)": "Price",
                                         "Amount ($)": "Notional"})
            # Trim transactions to buys and sells (for now)
            # TODO: Consider other types of transactions in transaction log.
            transactions = transactions.loc[transactions['Direction'].isin(("Purchase ", "Sale "))]
            # Drop unnecessary columns
            transactions.drop(labels=["Settlement Date", "Pending/Settled", "Account Nickname", "Account Registration",
                                      "Account #", "Type", "Description 2"])

        # Convert strings to numbers where applicable
        transactions = transactions.apply(pd.to_numeric, errors='ignore')
        print(transactions.head())
        self.transactions = transactions

    def get_positions(self, asof_date=None):
        """ Quick function to find positions for a portfolio given a date.
            Does not include original trade prices for cost basis calculations.
            Must have transactions loaded to run.
        :param asof_date: Datetime-like object to compare with pd datetime index of portfolio.transactions.
        :return:
        """
        assert bool(len(self.transactions)), "No transactions."

        positions = {}

        for security in set(self.transactions['Symbol']):
            sec_transactions = self.transactions[self.transactions['Symbol'] == security &
                                                 self.transactions.index <= asof_date]
            positions[security] = sum(sec_transactions["Quantity"])

if __name__ == "__main__":
    graph_plot(None, None)
