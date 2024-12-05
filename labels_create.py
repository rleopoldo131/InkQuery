import os

# Path to the directory where the .npz files are located
data_directory = "/mnt/c/Users/rleop/Downloads/drawing_project/processed_data"

# Path to save the labels file
labels_file_path = "/mnt/c/Users/rleop/Downloads/drawing_project/labels.txt"

# Get a list of all .npz files in the directory
npz_files = [f for f in os.listdir(data_directory) if f.endswith('.npz')]

# Writing the filenames (without extensions) to the labels file
with open(labels_file_path, 'w') as file:
    for npz_file in npz_files:
        # Write the filename without the .npz extension
        label = os.path.splitext(npz_file)[0]
        file.write(f"{label}\n")

print(f"Labels have been written to {labels_file_path}")
