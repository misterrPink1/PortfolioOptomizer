'''
The purpose of this function is to simulate and assess the perormance of a 4 stock portfolio
Inputs: 
	- Start Date
	- End Date
	- Symbols for the equities (eg. GOOG, AAPL, GLD, XOM)
	- Allocations to the equities at the beginning of the simulation (e.g. 0.2, 0.3, 0.4, 0.1)
Outputs:
	- Standard deviation of daily returns of the total portfolio 
	- Average daily return of the total portfolio
	- Sharpe ratio (252 trading days in a year at risk free rate = 0) of the total portfolio
	- Cumulative return of the total portfolio
	
Example execution:
vol, daily_ret, sharpe, cum_ret = simulate(startdate, enddate, ['GOOG', 'AAPL', 'GLD', 'XOM'), [0.2, 0.3. 0.4, 0.1])

'''

import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd


ls_symbols = ["GOOG", "APPL", "GLD", "XOM"]
dt_start = dt.datetime(2006, 1, 1)
dt_end = dt.datetime(2010, 12, 31)
dt_timeofday = dt.timedelta(hours=16)
ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)

print ldt_timestamps