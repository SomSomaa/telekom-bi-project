# Telekom Churn Prediction & AI Sentiment Analysis

I built this mini-project for an internship interview preparation to model a real-world Business Intelligence workflow. My goal was to connect traditional data warehousing concepts (SQL, Power BI) with modern AI/NLP capabilities.

## Project Overview
The application processes customer records and customer service call logs for a fictional telecom provider. Raw customer complaints are analyzed using a local AI model, and the enriched data is visualized in a Power BI dashboard to highlight key business metrics and churn risks.

## Technical Architecture (Data Pipeline)

1. **Database & Generation (SQL & Python):** I wrote a Python script to set up a local SQLite database from scratch. It designs a `Customers` dimension table and a `Call_Logs` table, linking them via `Customer_ID` using standard relational database logic, and populates them with 100 realistic mock records.

2. **Data Cleaning & AI (ETL Process):** Using Pandas, I extracted the raw data from the database. I passed the English call log complaints through the `TextBlob` NLP library to evaluate sentiment polarity (Positive, Negative, or Neutral). These AI-enriched records were then loaded back into a new structured fact table.

3. **Visualization & Business Logic (Power BI & DAX):** I imported the data into Power BI Desktop, where the tables are connected using a standard One-to-Many relationship. Key Performance Indicators (KPIs) were built using custom DAX expressions, including advanced filtering (`CALCULATE`) and robust division handling (`DIVIDE`) for the churn risk rate.