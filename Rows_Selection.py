import pandas as pd

data={
    "Name": ["Alice", "Bob", "Charlie","John","Mark","Stokes"],
    "Age": [25, 30, 35, 28, 40, 22],
    "City": ["Haryana", "Delhi", "Maharashtra", "Jharkhand", "U.P.", "Bihar"],
    "Salary": [50000, 60000, 70000, 80000, 90000, 100000],
    "Performance": [85, 90, 95, 80, 75, 88]
}
df= pd.DataFrame(data)

high_salary= df[df['Salary']>50000]
print('# Employees with salary> 50,000:--')
print(high_salary)

#Filtering rows salary >50,000 & age> 30--
filtered_rows = df[(df['Age'] > 30) & (df['Salary'] > 50000)]
print('# Employees list Age > 30 + Salary> 50,000:--')
print(filtered_rows)

#Using OR Condition--
filtered_rows= df[(df['Age'] > 35) | (df['Performance'] > 90)]
print('# Employees older than 35 or performance score> 90:--')
print(filtered_rows)