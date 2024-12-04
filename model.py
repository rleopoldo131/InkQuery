import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.utils import to_categorical
import os


def preprocess_data(npz_file_path, sample_limit=10000):
    npz_data = np.load(npz_file_path)
    data = npz_data['data'][:sample_limit]  # Limit to the first `sample_limit` samples
    labels = np.full(data.shape[0], os.path.basename(npz_file_path).split(".")[0])
    return data, labels


def load_all_data(npz_file_paths, sample_limit=10000):
    all_data, all_labels = [], []
    for npz_file in npz_file_paths:
        data, labels = preprocess_data(npz_file, sample_limit)
        all_data.append(data)
        all_labels.extend(labels)

    all_data = np.concatenate(all_data, axis=0)
    return all_data, np.array(all_labels)


def train_model(npz_files, sample_limit=10000, batch_size=32, epochs=20):
    # Load and preprocess data
    all_data, all_labels = load_all_data(npz_files, sample_limit)
    all_data = all_data.reshape(-1, 28, 28, 1).astype('float32') / 255.0

    # Encode labels as integers and convert to categorical
    unique_labels, encoded_labels = np.unique(all_labels, return_inverse=True)
    encoded_labels = to_categorical(encoded_labels, num_classes=len(unique_labels))

    # Define the model
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(len(unique_labels), activation='softmax')
    ])

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Train the model
    model.fit(all_data, encoded_labels, epochs=epochs, batch_size=batch_size, verbose=1)

    # Save the model
    model.save('drawing_model.h5')


if __name__ == "__main__":
    npz_directory = './processed_data/'
    npz_files = [os.path.join(npz_directory, f) for f in os.listdir(npz_directory) if f.endswith('.npz')]
    npz_files = npz_files[:10]  # Adjust the number of files to load more classes
    train_model(npz_files, sample_limit=10000, batch_size=32, epochs=20)
