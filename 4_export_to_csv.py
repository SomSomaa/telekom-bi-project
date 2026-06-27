import sqlite3
import pandas as pd

conn = sqlite3.connect('telekom_data.db')

pd.read_sql_query("SELECT * FROM Customers", conn).to_csv('Customers.csv', index=False)
pd.read_sql_query("SELECT * FROM Fact_Call_Sentiment", conn).to_csv('Fact_Sentiment.csv', index=False)

conn.close()
print("Success! CSV files are ready for Power BI.")