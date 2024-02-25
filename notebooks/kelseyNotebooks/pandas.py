import pandas as pd

# Sample DataFrame
data = {'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]}
df = pd.DataFrame(data)

# Define a function to process column contents
def process_data(column_data):
    # Example: Just printing the column contents
    print(column_data)

# Iterate over column names and pass column contents to function
for column in df.columns:
    process_data(df[column])