import sqlite3
import pandas as pd
from textblob import TextBlob

conn = sqlite3.connect('telekom_data.db')

query = """
SELECT c.Customer_ID, c.Contract_Type, l.Log_ID, l.Complaint_Text, l.Call_Duration_Min
FROM Customers c
JOIN Call_Logs l ON c.Customer_ID = l.Customer_ID
"""
df = pd.read_sql_query(query, conn)

def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0.1:
        return 'Positive'
    elif analysis.sentiment.polarity < -0.1:
        return 'Negative'
    else:
        return 'Neutral'

df['AI_Sentiment'] = df['Complaint_Text'].apply(analyze_sentiment)

df['Churn_Risk_Flag'] = ((df['AI_Sentiment'] == 'Negative') & (df['Call_Duration_Min'] > 10)).astype(int)


df.to_sql('Fact_Call_Sentiment', conn, if_exists='replace', index=False)

conn.close()
print("Success! ETL process and AI Sentiment Analysis completed. 'Fact_Call_Sentiment' table created.")