"""
Fixes missing treasury data if the Fed's website is down.  This should be run from within the repo.
"""

import pandas as pd

input_filename = './FRB_H15_2-15-2019.csv'
output_filename = '~/.zipline/data/treasury_curves.csv'
# if you have a treasury_curves.csv file with more recent dates, use that one
# input_filename = output_filename
df = pd.read_csv(input_filename, parse_dates=['Time Period'], index_col=0)

today = pd.to_datetime('today').date()

df.loc[today] = df.iloc[-1]
df = df.asfreq('D')
df.ffill(inplace=True)
df.to_csv(output_filename)
