import pandas as pd

data={
    "Name": ['Arun','Varun','Karun','Tarun','Sam'],
    "Age": [28,34,22,34,28],
    "Salary": [10000,20000,30000,35000,65000]
}

df=pd.DataFrame(data)
grouped= df.groupby('Age')["Salary"].sum()
print('\nGrouped data by Age with sum of Salary:')
print(grouped)
grouped= df.groupby(["Age","Name"])["Salary"].sum()
print('\nGrouped data by Age and Name with sum of Salary:')
print(grouped)