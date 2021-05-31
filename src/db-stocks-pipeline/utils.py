from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
import psycopg2


load_dotenv()

user = os.environ.get("DB_STOCKS_USER")
password = os.environ.get("DB_STOCKS_PASSWORD")
host = os.environ.get("DB_STOCKS_HOSTNAME")
port = os.environ.get("DB_STOCKS_PORT")

def create_db_stocks_conn():
    """
    Returns the connection object for the db_stocks database.
    """
    conn_string = 'postgresql://{user}:{password}@{host}:{port}/{db}'.format(
        user = user,
        password = password,
        host = host,
        port = port,
        db = 'postgres'
    )

    engine = create_engine(conn_string)

    conn = engine.connect()
    return conn

# df_tickers = conn.execute('select * from db_stocks.dim_stocks').fetchall()
