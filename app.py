import pandas as pd

#read data from CSV file into a dataframe
#df =pd.read_csv("sample_Data.csv",encoding="latin1")
#df =pd.read_excel("SampleSuperstore.xlsx")
df=pd.read_json("sample_Data.json")
print(df) 