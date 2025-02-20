import pandas as pd

# write python code to read csv file and write it on excel file
df = pd.read_csv('./t1.csv')
df.to_excel('./t2.xlsx', index=False)
