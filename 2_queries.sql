SELECT Name, Contract_Type, Monthly_Fee
FROM Customers;

SELECT c.Name, l.Complaint_Text, l.Call_Duration_Min
FROM Customers c
JOIN Call_Logs l ON c.Customer_ID = l.Customer_ID;

SELECT c.Contract_Type, AVG(l.Call_Duration_Min) as Avg_Call_Duration
FROM Customers c
JOIN Call_Logs l ON c.Customer_ID = l.Customer_ID
GROUP BY c.Contract_Type
ORDER BY Avg_Call_Duration DESC;