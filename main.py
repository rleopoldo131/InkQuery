import numpy as np
import tensorflow as tf
from preprocess_input import preprocess_input
from utils import load_labels

# Load the model
model = tf.keras.models.load_model("models/drawing_model.h5")

def predict_doodle(input_vector):
    input_vector = preprocess_input(input_vector)
    if input_vector is not None:
        predictions = model.predict(input_vector)
        predicted_class_index = np.argmax(predictions)
        confidence = predictions[0][predicted_class_index]
        return predicted_class_index, confidence
    else:
        print("Error: input preprocessing failed.")
        return None, None

def main():
    test_file = "processed_data/test_data.npz"
    labels_file = "labels.txt"
    class_labels = load_labels(labels_file)

    data = np.load(test_file)
    input_data = data['arr_0']  # Adjust based on actual key

    predicted_index, confidence = predict_doodle(input_data)
    if predicted_index is not None:
        print(f"Predicted class: {class_labels[predicted_index]} (Confidence: {confidence:.2f})")
    else:
        print("Prediction failed.")

if __name__ == "__main__":
    main()
