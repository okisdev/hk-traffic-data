import pandas as pd

# Read the JSON file
df = pd.read_json("data.json")

# Write the CSV file
df.to_csv("data.csv", index=False)
