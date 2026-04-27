import pandas as pd

data = {'Name': ['Joe','Nat'], 'Age':[20,21], 'Marks':[85,77]}
df = pd.DataFrame(data)

df['Grade'] = ['A','B']

print(df)

print("\nGroupBy Mean:")
print(df.groupby('Grade').mean(numeric_only=True))