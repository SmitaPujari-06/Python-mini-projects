import pandas as pd
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'country': ['India', 'France', 'India', 'Italy'],
    'points': [87, 92, 89, 95],
    'price': [15.0, 32.0, None, 40.0]
}, index=[10, 20, 30, 40])
df['hello']='hello'
print(df)