CREATE TABLE db_stocks.td_price_history (
	symbol varchar(10) NULL,
	"date" date NULL,
	volume float8 NULL,
	"close" float8 NULL,
	low float8 NULL,
	"open" float8 NULL,
	high float8 NULL,
	adjclose float8 NULL,
	dividends float8 NULL,
	splits float8 NULL
);
