import os
import json

# Define the path to the data directory
data_dir = "data"


# Function to get the directory structure
def get_directory_structure(dir_path):
    dir_structure = []
    for root, dirs, _ in os.walk(dir_path):
        if root == dir_path:
            dir_structure.extend({"method": dir, "data": []} for dir in dirs)
        else:
            parent_dir = os.path.basename(root)
            for item in dir_structure:
                if item["method"] == parent_dir:
                    item["data"].extend(dirs)
                    break
    return dir_structure


# Get the directory structure of the data directory
data_structure = get_directory_structure(data_dir)

# Write the dictionary to a JSON file
with open("data-structure.json", "w") as f:
    json.dump(data_structure, f, indent=4)
