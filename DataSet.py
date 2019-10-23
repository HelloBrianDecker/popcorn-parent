from Processing import *
from PreprocessingMarkers import *
from learning_algorithms.LogisticRegression import *
from learning_algorithms.LinearRegression import *
from learning_algorithms.NeuralNetwork import *
import pandas as pd


class DataSet:
    def __init__(self, data):
        self.data = data
        self.autorun = False
        self.preprocessing = Processing
        self.preprocessingMarker = PreprocessingMarkers()
        self.LogisticRegression = LogisticRegression
        self.NeuralNetwork = NeuralNetwork
        self.LinearRegression = LinearRegression
        self.target_data = pd.DataFrame()
        self.train_data = pd.DataFrame()
        self.regularized_data = pd.DataFrame()
        self.avg = self.std = 0

    def get_data(self):
        return self.data

    def get_autorun(self):
        return self.autorun

    def set_autorun(self, boolean):
        self.autorun = boolean

    def run_autorun(self):
        if self.autorun is True:
            preprocess = Processing(self.data)
            preprocess.null_count()
            preprocess.separate()
            preprocess.outlier_detection()
            preprocess.set_targets()
            preprocess.standardize()

    def set_preprocessing(self):
        self.preprocessing = Processing(self.data)

    def get_preprocessing(self):
        return self.preprocessing

    def get_preprocessing_markers(self):
        return self.preprocessingMarker

    def get_target_data(self):
        return self.target_data

    def get_train_data(self):
        return self.train_data

    def set_logistic_regression(self):
        self.LogisticRegression(self.target_data, self.train_data)

    def set_linear_regression(self):
        self.LinearRegression(self.target_data, self.train_data)

    def set_neural_network(self):
        self.NeuralNetwork(self.target_data, self.train_data)