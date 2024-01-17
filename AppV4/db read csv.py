import pandas as pd
import sqlite3

# Assuming your database is located at C:\Users\bhara\Desktop\myworks\AppV4\MASTER.db
db_path = r"C:\Users\bhara\Desktop\myworks\AppV4\MASTER.db"

# Establish a connection to the SQLite database
conn = sqlite3.connect(db_path)

# Define your SQL query
query = "SELECT * FROM MASTER"

# Use pandas to read the query results into a DataFrame
df = pd.read_sql_query(query, conn)



# Close the database connection
conn.close()

# Display the DataFrame
print(df)
