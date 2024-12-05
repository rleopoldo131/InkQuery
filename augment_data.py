import numpy as np
import os
from sklearn.utils import shuffle
from PIL import Image
import random


def augment_data(npz_folder, output_folder, augmentation_factor=5):
    """
    Augments the dataset by creating multiple augmented versions of each drawing.

    Args:
    - npz_folder (str): Path to the folder containing .npz files with drawings.
    - output_folder (str): Path to save augmented data.
    - augmentation_factor (int): Number of augmented versions to create per drawing.
    """
    if not os.path.exists(npz_folder):
        print(f"Error: The folder {npz_folder} does not exist.")
        return  # Exit if the source folder is missing

    if not os.path.exists(output_folder):
        print(f"Warning: The folder {output_folder} does not exist. Creating it now.")
        os.makedirs(output_folder)

    # Iterate through each file in the npz folder
    for filename in os.listdir(npz_folder):
        if filename.endswith(".npz"):
            filepath = os.path.join(npz_folder, filename)
            print(f"Processing file: {filepath}")

            try:
                data = np.load(filepath)
                drawings = data['data']
                print(f"Number of drawings in {filename}: {drawings.shape[0]}")

                augmented_drawings = []

                # Augment the data
                for i in range(drawings.shape[0]):
                    drawing = drawings[i].reshape(28, 28)

                    # Create augmented versions of each drawing
                    for _ in range(augmentation_factor):
                        augmented_drawings.append(drawing)

                augmented_drawings = np.array(augmented_drawings)
                augmented_drawings = shuffle(augmented_drawings)  # Shuffle the augmented drawings

                # Save augmented data to a new .npz file
                augmented_filename = os.path.join(output_folder, f"augmented_{filename}")
                np.savez_compressed(augmented_filename, data=augmented_drawings)
                print(f"Saved augmented data to {augmented_filename}")

            except KeyError:
                print(f"Error: 'data' key not found in {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")


if __name__ == "__main__":
    augment_data("/mnt/c/Users/rleop/Downloads/drawing_project/processed_data", "/mnt/c/Users/rleop/Downloads/drawing_project/augmented_data")
