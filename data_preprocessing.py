import numpy as np
import os
import psutil
from concurrent.futures import ProcessPoolExecutor, as_completed

# Directory paths
DATA_DIR = "./data"
OUTPUT_DIR = "./processed_data"

# Create output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)


# Function to check memory usage
def memory_status():
    mem = psutil.virtual_memory()
    return {
        "total": mem.total / (1024 ** 3),
        "used": mem.used / (1024 ** 3),
        "free": mem.available / (1024 ** 3),
        "percent": mem.percent,
    }


# Function to process individual files
def process_file(filepath):
    try:
        data = np.load(filepath)
        base_name = os.path.basename(filepath).replace(".npy", "")
        output_file = os.path.join(OUTPUT_DIR, f"{base_name}.npz")

        np.savez_compressed(output_file, data=data)
        mem_status = memory_status()

        return f"Processed {filepath}: Shape {data.shape}, Memory Usage {mem_status['percent']}%"

    except Exception as e:
        return f"Error processing {filepath}: {e}"


# Main processing function
def main():
    files = [os.path.join(DATA_DIR, f) for f in os.listdir(DATA_DIR) if f.endswith(".npy")]

    with ProcessPoolExecutor() as executor:
        futures = {executor.submit(process_file, file): file for file in files}

        for future in as_completed(futures):
            print(future.result())


if __name__ == "__main__":
    main()
