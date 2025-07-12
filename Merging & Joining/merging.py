# pd.merge(df1, df2, on="column_name", how="type of join")
# Joins types---- inner,cross,left,right,outer
import pandas as pd

# customer dataframe----

df_customers=pd.DataFrame({
    "CustomerID": [1, 2, 3, 4],
    "CustomerName": ["Alice", "Bob", "Charlie", "David"]
})

# orders dataframe----
df_orders=pd.DataFrame({
    "OrderID": [101, 102, 103, 104],
    "CustomerID": [1, 2, 4, 5],
    "OrderAmount": [250, 150, 300, 200]
})

# Merging the dataframes on CustomerID using inner join
df_merged=pd.merge(df_customers, df_orders, on="CustomerID", how="outer")
print("Merged DataFrame using inner join:")
print(df_merged)