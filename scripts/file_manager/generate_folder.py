import os

# Define the path to the data directory
data_dir = "data"

# Get a list of all the directories in the data directory
directories = [
    d for d in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, d))
]

# Loop through each directory and create a folder named 'origin'
for directory in directories:
    os.makedirs(os.path.join(data_dir, directory, "raw"), exist_ok=True)
