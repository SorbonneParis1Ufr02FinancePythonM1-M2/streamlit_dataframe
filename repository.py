import pandas as pd


def get_data():
    headers = ['id', 'product', 'underlying', 'strike', 'spot', 'maturity date', 'way', 'amount', 'currency']

    df = pd.DataFrame([['tot254', 'call', 'total', 41.83, 43.56, '2022-08-23', 1, 100000, 'EUR'],
                       ['goo149', 'put', 'google', 3002.09, 2898.23, '2023-06-01', -1, 50000, 'USD'],
                       ['viv983', 'call', 'vivendi', 10, 11.36, '2022-10-16', -1, 1500000, 'EUR'],
                       ['viv984', 'call', 'vivendi', 12.12, 11.36, '2022-10-16', 1, 1500000, 'EUR'],
                       ['saf461', 'call', 'safran', 112.96, 111.23, '2024-02-24', 1, 100000, 'EUR'],
                       ['air123', 'put', 'airbus', 109.40, 108.12, '2023-01-13', 1, 50000, 'EUR']
                       ]
                      , columns=headers)

    df.set_index('id', inplace=True)

    return df
