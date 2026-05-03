import pandas as pd

df = pd.read_csv("poke_data.csv",index_col=0)

print(df.to_string())

#print(df[["Name","Height"]].to_string())