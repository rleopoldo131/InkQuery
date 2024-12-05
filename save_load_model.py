# save_load_model.py
import tensorflow as tf

def save_model(model, filename):
    model.save(filename)
    print(f"Model saved as {filename}")

def load_model(filename):
    model = tf.keras.models.load_model(filename)
    print(f"Model loaded from {filename}")
    return model

if __name__ == "__main__":
    from drawing_project.model import build_model
    from drawing_project.data_preprocessing import load_and_preprocess_data

    folder_path = '/mnt/c/Users/rleop/Downloads/numpy_bitmap'
    X_train, X_test, y_train, y_test, label_encoder = load_and_preprocess_data(folder_path)

    # Build the model
    model = build_model(X_train.shape[1])

    # Save the model
    save_model(model, 'drawing_model.h5')

    # Load the model
    model = load_model('drawing_model.h5')
