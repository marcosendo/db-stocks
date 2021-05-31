from utils import create_db_stocks_conn
import numpy as np
import pandas as pd
from yahooquery import Ticker, Screener

conn = create_db_stocks_conn()

sql = 'select * from db_stocks.dim_stocks'
df_tickers = pd.read_sql_query(sql, conn)

symbols = df_tickers['symbol'].values

tickers = Ticker(symbols, asynchronous=True)

df_income_statement = tickers.income_statement(frequency='q', trailing=False)
print(df_income_statement.head())

df_income_statement.to_sql(name = 'db_stocks.tb_income_statement', index = True, con = conn, if_exists = 'replace', chunksize = 1000, method = 'multi')