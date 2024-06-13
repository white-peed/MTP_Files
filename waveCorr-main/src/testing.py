import pandas as pd
import numpy as np
from scipy import stats
import os

path = 'data/can'

def list_all_files_and_folders(directory, files = []):
    for entry in os.listdir(directory):
        full_path = os.path.join(directory, entry)
        if os.path.isdir(full_path):
            list_all_files_and_folders(full_path, files)  # Recursive call for subdirectories
        else:
            files.append(full_path[8:])
    return files

files = list_all_files_and_folders(path)

for file in files:
    data = pd.read_csv("data/can" + file)
    x_close = data["x_close"].to_numpy()

    # Initialize arrays for skewness and kurtosis
    skewness_values = np.zeros_like(x_close)
    kurtosis_values = np.zeros_like(x_close)

    # Calculate skewness and kurtosis in groups of 10
    for i in range(0, len(x_close) - 10):
        group = x_close[i:i + 10]
        if len(group) > 1:  # Ensure at least 2 elements for valid calculation
            skewness_values[i + 10] = stats.skew(group, bias=False)  # Unbiased estimator
            kurtosis_values[i + 10] = stats.kurtosis(group, bias=False)  # Unbiased estimator

    # Insert the new columns at the desired position (between x_close and y_close)
    data.insert(loc=2, column="Skewness", value=skewness_values)  # Insert 'None' values initially
    data.insert(loc=3, column="Kurtosis", value=kurtosis_values)  # Insert 'None' values initially

    data.to_csv("data/can_new" + file, index=False)