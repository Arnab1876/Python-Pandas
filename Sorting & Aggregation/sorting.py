#sorting data
#sorting data 1 column sort_values()
# --FOR SINGLE COLUMN:  df.sort_values(by="Column_Name", ascending=True/False) , inplace=True)
# --FOR MULTIPLE COLUMNS:  df.sort_values(by=["Column_Name1","Column_Name2"], ascending=[True,False] , inplace=True)
import pandas as pd

data={
    "Name": ['Arun','Varun','Karun'],
    "Age": [28,34,22],
    "Salary": [10000,20000,30000]
}

df=pd.DataFrame(data)
df.sort_values(by="Age",ascending=False,inplace=True)
print('\nSorted age by descending order--')
print(df)


df=pd.DataFrame(data)
df.sort_values(by=["Age","Salary"],ascending=[False,False],inplace=True)
print('\nSorted age & salary by descending order--')
print(df)