import pandas as pd
df = pd.read_excel("data_test.xlsx")
print(df["No of plants harvest"].mean())