import pandas as pd


def hello_world(args):
    return "Hello, World!"


def excel_to_json(args):
    df = pd.read_excel(args.input)
    return df.to_json()
