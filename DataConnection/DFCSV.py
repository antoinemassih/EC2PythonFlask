import pandas as pd


class DFCSV:
    data = pd.DataFrame()
    filename = ""

    def __init__(self, filename):
        self.filename = filename
        self.data = pd.read_csv(filename)
