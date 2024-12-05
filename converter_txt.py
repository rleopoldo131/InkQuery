import numpy as np

# Load the test data from the text file
test_data_file = "/mnt/c/Users/rleop/Downloads/drawing_project/test_data.txt"

# Open the text file and clean the data (remove unwanted characters)
with open(test_data_file, 'r') as file:
    lines = file.readlines()

# Clean each line: remove unwanted characters like '[' ']' '{', '}', and ',' from the line
cleaned_data = []
for line in lines:
    # Remove unwanted characters like '{', '}', ',', '[' and ']' from the line
    line = line.strip().replace('{', '').replace('}', '').replace(',', '').replace('[', '').replace(']', '')

    # Convert to list of numbers by splitting by spaces
    try:
        cleaned_data.append(list(map(float, line.split())))
    except ValueError as e:
        print(f"Skipping line due to error: {line} \nError: {e}")

# Convert the cleaned data into a numpy array
data_array = np.array(cleaned_data)

# Print the shape of the data
print(f"Data array shape: {data_array.shape}")

# Check if the data can be reshaped into a square shape
num_elements = data_array.size
sqrt_elements = int(np.sqrt(num_elements))

# Try reshaping if the number of elements is a perfect square
if sqrt_elements * sqrt_elements == num_elements:
    images = data_array.reshape(-1, sqrt_elements, sqrt_elements)
    print(f"Data reshaped into {images.shape}")
else:
    print(f"Cannot reshape into a perfect square. Keeping original shape.")

    # Optionally, you can save the raw data without reshaping
    images = data_array

# Save the data as a .npz file
np.savez("/mnt/c/Users/rleop/Downloads/drawing_project/processed_data/test_data.npz", arr_0=images)
print(f"Data successfully saved to 'test_data.npz'")
