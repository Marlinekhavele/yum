import pandas as pd

df = pd.read_excel("data_test.xlsx")
print(df.DataFrame.sort_values(by=['Harvesting date'], ascending=True))