import pandas as pd
f = pd.read_csv("products.csv")
print(f.head())

print(f.describe(include = 'all'))

missing_data = f.isnull()
for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print('')

print(f.duplicated())                      #Duplicados del DataFrame
#f['Case Number'].duplicated().sum()
#duplicates = f[f['Case Number'].duplicated(keep=False)]['Case Number'].tolist()
#duplicates[:10]

#print(duplicates)