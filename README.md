# treasury_data_backup
Backup of treasury data for zipline backtesting.

Occasionally the Fed's website is down for downloading treasury data for Sharpe ratios.  The link is here:

https://www.federalreserve.gov/datadownload/Output.aspx?rel=H15&series=bf17364827e38702b42a58cf8eaa3f78&lastObs=&from=&to=&filetype=csv&label=include&layout=seriescolumn&type=package

Last time it looked like this when it was down, and it was down for 2 days:

![fed_down.png]

This seemed to mainly be an issue for custom CSV data.

To fix this issue, run the `fix_treasury_data.py` file from within this repo.  You may want to change the input_filename to be your existing treasury_curves.csv file if you've run a backtest more recently than 2-15-2019.  If you are installing the library from scratch, you have to use this to generate the csv file with the 2-15-2019 data.
