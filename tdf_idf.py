from text_preprocessing import text_preprocess
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


df = pd.read_excel('./tiktok_df.xlsx')
unique_df = df.drop_duplicates(subset='id')
unique_df = unique_df[unique_df['description'].notnull() & (unique_df['description'] != '')]
# Optionally, reset the index if you want a clean index in the unique DataFrame
unique_df = unique_df.reset_index(drop=True)

text_preprocess(unique_df)
# Check empty sentences
unique_df = unique_df[unique_df['sentence'].notnull() & (unique_df['sentence'] != '')]
corpus = unique_df['sentence']
print(corpus)