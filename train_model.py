import numpy as np
import os
from sklearn.utils import shuffle


def augment_data(npz_folder, output_folder, augmentation_factor=5):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(npz_folder):
        if filename.endswith(".npz"):
            filepath = os.path.join(npz_folder, filename)
            print(f"Processing file: {filepath}")
            try:
                data = np.load(filepath)
                drawings = data['data']

                if drawings.size == 0:
                    print(f"Warning: {filename} contains no data. Skipping.")
                    continue

                augmented_drawings = []
                for i in range(drawings.shape[0]):
                    drawing = drawings[i].reshape(28, 28)

                    for _ in range(augmentation_factor):
                        augmented_drawings.append(drawing)

                if len(augmented_drawings) == 0:
                    print(f"Warning: No augmented drawings created for {filename}")
                    continue

                augmented_drawings = np.array(augmented_drawings)
                augmented_drawings = shuffle(augmented_drawings)

                augmented_filename = os.path.join(output_folder, f"augmented_{filename}")
                np.savez_compressed(augmented_filename, data=augmented_drawings)
                print(f"Saved augmented data to {augmented_filename}")

            except KeyError:
                print(f"Error: 'data' key not found in {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")


if __name__ == "__main__":
    augment_data("/mnt/c/Users/rleop/Downloads/drawing_project/processed_data", "/mnt/c/Users/rleop/Downloads/drawing_project/augmented_data", augmentation_factor=5)
