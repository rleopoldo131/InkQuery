import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image

# Replace this with your actual model path
model_path = ""


def get_user_input():
    x_coords = [563, 563, 563, 563, 563, 563, 563, 563, 563, 563, 563, 563, 563, 563, 563, 564, 564, 564, 564, 564, 564,
                564, 564, 564, 564, 565, 565, 565, 565, 565, 565, 565, 565, 565, 565, 565, 565, 565, 565, 565, 565, 565,
                565, 565, 565, 564, 564, 564, 564, 564, 564, 564]
    y_coords = [218, 219, 220, 222, 223, 225, 226, 227, 228, 229, 230, 231, 233, 235, 236, 237, 238, 239, 240, 241, 242,
                243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263,
                264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 275]

    # Ensure both lists have the same length
    min_length = min(len(x_coords), len(y_coords))
    x_coords = x_coords[:min_length]
    y_coords = y_coords[:min_length]

    # Create a blank image (28x28) and map the points to it
    img = np.zeros((28, 28), dtype=np.uint8)

    # Normalize the x and y coordinates to fit within the 28x28 grid
    x_scaled = np.interp(x_coords, (min(x_coords), max(x_coords)), (0, 27)).astype(int)
    y_scaled = np.interp(y_coords, (min(y_coords), max(y_coords)), (0, 27)).astype(int)

    # Plot the points on the 28x28 grid
    for x, y in zip(x_scaled, y_scaled):
        img[y, x] = 255  # Mark the points as white pixels

    # Resize the image to match the expected input size (28x28)
    img_resized = Image.fromarray(img).resize((28, 28), Image.Resampling.LANCZOS)

    # Convert the image to a numpy array
    input_vector = img_to_array(img_resized)

    return input_vector


def predict_doodle(input_vector, model):
    # Reshape and scale the input image (since it's a single image, no need to batch)
    input_vector = input_vector.reshape(1, 28, 28, 1).astype('float32') / 255.0

    # Make the prediction using the model
    prediction = model.predict(input_vector)

    # Return the prediction (you can modify this to get the top class or corresponding label)
    predicted_class = np.argmax(prediction, axis=-1)
    return predicted_class


# Load your trained model
model = load_model(model_path)

# Collect the user input
input_vector = get_user_input()

# Make the prediction
prediction_result = predict_doodle(input_vector, model)

# Print the prediction result (it could be an index or a class name depending on your model)
print("Predicted class:", prediction_result)
