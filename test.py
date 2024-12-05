import numpy as np

# Load the .npz file
file_path = "/mnt/c/Users/rleop/Downloads/drawing_project/processed_data/test_data.npz"
data = np.load(file_path)

# List all keys in the .npz file
print("Keys in the .npz file:", data.files)

# Display the shape and type of each array
for key in data.files:
    print(f"Key: {key}, Shape: {data[key].shape}, Type: {data[key].dtype}")
