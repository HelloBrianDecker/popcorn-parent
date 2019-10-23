from Preprocess import Reformat as form, Standardize as st, Outliers as out, OLS, Split_Data as sd, Views as view, \
    SetTarget as tar
import ClusterAnalysis as cluster
import pandas as pd
from Preprocess.NullValues import null_count_columns, null_count_rows


class Processing:
    def __init__(self, data):
        self._observers = []
        self.data = data
        self.train_data = pd.DataFrame()
        self.target_data_name = ''
        self.target_data = pd.DataFrame()
        self.processed_data = pd.DataFrame()
        self.standardized_data = pd.DataFrame()
        self.avg = self.std = 0.
        self.train_inputs = pd.DataFrame()
        self.train_targets = pd.DataFrame()
        self.validate_inputs = pd.DataFrame()
        self.validate_targets = pd.DataFrame()
        self.test_inputs = pd.DataFrame()
        self.test_targets = pd.DataFrame()
        self.std_avg = {}
        self.column_count = 0

    def get_target_data(self):
        return self.target_data

    def get_train_data(self):
        return self.train_data

    def get_standardized_data(self):
        return self.standardized_data

    def get_avg(self):
        return self.avg

    def get_std(self):
        return self.std

    def convert_processed_data(self, data):
        self.processed_data = data
        try:
            self.target_data = self.processed_data[self.target_data_name]
        except:
            print('Could not convert the target column\n')
        try:
            self.train_data = self.processed_data.drop([self.target_data_name], axis=1)
        except:
            print('Could not convert the train columns\n')

    def set_target_train(self):
        try:
            self.target_data = self.processed_data[self.target_data_name]
        except:
            print('Could not convert the target column\n')
        try:
            self.train_data = self.processed_data.drop([self.target_data_name], axis=1)
        except:
            print('Could not convert the train columns\n')

    def view_data(self):
        view.view_data(self.processed_data)
        OLS.ols(self.target_data, self.train_data)

    def set_column_count(self):
        return len(self.processed_data.columns)

    def null_count(self):
        self.processed_data = null_count_columns(self.processed_data)
        self.processed_data = null_count_rows(self.processed_data)
        self.set_target_train()
        self.standardize()
        self.column_count = self.set_column_count()

    def cluster_analysis(self):
        cluster.cluster_analysis(self.train_data, self.target_data)

    def outlier_detection(self):
        self.processed_data = out.outlier_detection(self.processed_data, self.std_avg)
        self.set_target_train()

    def separate(self):
        self.target_data = form.convert_target(self.target_data)
        self.train_data = form.label_encoder(self.train_data)
        self.processed_data = pd.concat([self.train_data, self.target_data], axis=1)
        self.set_target_train()

    def set_target(self):
        self.target_data_name = tar.set_target(self.data)

    # def standardize(self):
    #     self.standardized_data, self.avg, self.std = st.standardize(self.train_data)

    def standardize(self):
        self.std_avg = st.row_mean_array(self.train_data)
        print(self.std_avg)

    def split_data(self):
        if not self.processed_data.empty:
            self.train_inputs, self.train_targets, self.validate_inputs, self.validate_targets, self.test_inputs, \
            self.test_targets = sd.split_data(self.processed_data, self.target_data_name)
            print('Train Inputs:\n{}'.format(self.train_inputs))
            print('Train Targets:\n{}'.format(self.train_targets))
            print('Validate Inputs:\n{}'.format(self.validate_inputs))
            print('Validate Targets:\n{}'.format(self.validate_targets))
            print('Test Inputs:\n{}'.format(self.test_inputs))
            print('Test Targets:\n{}'.format(self.test_targets))
        else:
            print('Not ready to be split.  Remove null and outlier values.\n')

    def manipulate_dataset(self):
        ans = input('Would you like to drop Rows or Columns\n1: Rows\n2: Columns\n')
        data = self.processed_data
        if ans == '1':
            pass
        elif ans == '2':
            for columns in data:
                i = 1
                print('{}: {}\n'.format(i, columns))
                i += 1
            ans = input('Which column would you like to drop?\n')
            self.processed_data = data.drop(data.columns[int(ans)-1], axis=1)
            self.set_target_train()
            # return data.drop(data.columns[int(ans)-1], axis=1)
        else:
            print('Unfortunately that is not a valid input\n')