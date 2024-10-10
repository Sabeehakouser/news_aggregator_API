import pandas as pd
import os

csv_path = os.path.abspath('source\\news_csv')
news_csv_list = [os.path.abspath('source\\news_csv') + '\\' + file for file in os.listdir(csv_path)]

# Read the CSV files, skipping the header row
dfs = [pd.read_csv(f, header=None) for f in news_csv_list]

# Concatenate the dataframes, excluding the header row from all dataframes
df_concat = pd.concat(dfs[1:], ignore_index=True)

# Load the existing CSV file (if it exists)
try:
    existing_df = pd.read_csv('./news_articles.csv', header=None)
except FileNotFoundError:
    existing_df = pd.DataFrame()

# Append the new data to the existing DataFrame
existing_df = pd.concat([existing_df, df_concat], ignore_index=True)

# Save the updated DataFrame to the CSV file
existing_df.to_csv('./news_articles.csv', index=False, header=False)