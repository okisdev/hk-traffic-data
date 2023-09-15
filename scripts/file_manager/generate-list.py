import os
import json

# Define the path to the data directory
data_dir = "data"

# Get a list of all the directories in the data directory
directories = [
    d for d in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, d))
]

# Create a list of dictionaries to store the method names
transportation_method_list = [{"method": d} for d in directories]

# Write the dictionary to a JSON file
with open("transportation_list.json", "w") as f:
    json.dump(transportation_method_list, f)
