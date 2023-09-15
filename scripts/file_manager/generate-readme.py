import os

# Define the path to the data directory
data_dir = "data"

# Get a list of all the directories in the data directory
directories = [
    d for d in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, d))
]

# Loop through each directory and create a README.md file with the directory name as the content
for directory in directories:
    with open(os.path.join(data_dir, directory, "README.md"), "w") as f:
        f.write(f"# {directory}")
