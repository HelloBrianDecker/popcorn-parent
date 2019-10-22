import numpy as np


def standardize(data_processing):
    mean = np.mean(data_processing, axis=0)
    std = np.std(data_processing, axis=0)
    standardized_data = (data_processing - mean) / std
    return standardized_data, mean, std


def row_mean_array(data_processing):
    std_avg_array = {}
    for column in list(data_processing.columns.values):
        if data_processing[column].dtype not in ['object', 'str']:
            mean = np.mean(data_processing[column])
            std = np.std(data_processing[column])
            std_avg_array[column] = {mean, std}
    return std_avg_array

