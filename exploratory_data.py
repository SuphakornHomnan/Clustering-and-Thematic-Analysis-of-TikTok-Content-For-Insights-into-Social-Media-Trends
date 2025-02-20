import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

df = pd.read_excel('./tiktok_df.xlsx')

print(df.shape)

# Statistical summary of the dataset
print(df.describe().T)

print(df.describe(include= 'all').T)

#print(df.nunique())

#print(round((df.nunique()/ len(df)) * 100))

# Missing values
print(df.isnull().sum())

print(round((df.isnull().sum()/len(df)) * 100))


