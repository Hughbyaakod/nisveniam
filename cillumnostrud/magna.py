import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'points': [18, 22, 19, 14, 10, 11, 20, 28],
                   'assists': [4, 5, 5, 4, 9, 12, 11, 8],
                   'rebounds': [3, 9, 12, 4, 4, 9, 8, 2]},
                  index=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])

# Print the row located at index position 3
print(df.iloc[3])
