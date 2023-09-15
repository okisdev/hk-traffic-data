import pandas as pd

# Read the CSV file
df = pd.read_csv("data.csv")

# Write the JSON file with indents
df.to_json("data.json", orient="records", indent=2)
