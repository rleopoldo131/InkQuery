import numpy as np

def preprocess_input(input_vector):
    input_vector = np.array(input_vector).squeeze()

    if input_vector.shape == (22, 22):
        input_vector_resized = np.expand_dims(input_vector, axis=-1)
    else:
        return None

    input_vector_resized = np.pad(input_vector_resized, ((0, 6), (0, 6), (0, 0)), mode='constant')
    input_vector_resized = input_vector_resized / 255.0
    input_vector_reshaped = np.expand_dims(input_vector_resized, axis=0)
    return input_vector_reshaped
