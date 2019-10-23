import numpy as np


# The Processing Data and Dictionary containing the row, average and standard deviation
# are passed into the outlier_detection function.  Each node in the array will be checked if
# they are 3 standard deviations away from the norm.


def outlier_detection(data_processing, std_average_array):
    print('Outliers will be detected using 3 standard deviations away form the norm.  You will have '
          'the ability to use Grubb\'s test for outliers as well.\n')
    for column, standard_values_dictionary in std_average_array.items():
        outliers_array = []
        for node in data_processing[column]:
            if calculate_z_score(node, list(standard_values_dictionary)[0], list(standard_values_dictionary)[1]):
                outliers_array.append([node, list(data_processing[column]).index(node)])
        if len(outliers_array) > 0:
            data_processing = handle_outliers(data_processing, column, outliers_array)
            continue
        else:
            continue
    return data_processing


# Z-Score is calculated as:
# the value in the array x - the average of the array x_bar / the standard deviation of the array
def calculate_z_score(node, standard_deviation, average):
    threshold = 3
    z_score = ((node - average) / standard_deviation)
    if np.abs(z_score) > threshold:
        return True
    else:
        return False


def handle_outliers(data_processing, column, outliers_array):
    print('Outliers detected in {}\nValues: {}\n'.format(column, list(map(lambda outlier: outlier[0], outliers_array))))
    ans = input('Options:\n0: View Column\n1: View Outlier Rows\n'
                '2: Delete Outlier Rows\n3: Keep Outliers\n\n')
    if ans == '0':
        print('{}:\n{}\n'.format(column, data_processing[column]))
        return data_processing
    elif ans == '1':
        data_processing = view_outlier_rows(data_processing, column, outliers_array)
        return data_processing
    elif ans == '2':
        data_processing = delete_outlier_rows(data_processing, outliers_array)
        return data_processing
    elif ans == '3':
        return data_processing
    else:
        print('Unfortunately that is not a valid input\n')
        return data_processing


def view_outlier_rows(data_processing, column, outliers_array):
    i = 1
    print(outliers_array)
    for row in outliers_array:
        print('{}: {}\n'.format(i, data_processing.iloc[row[1], :]))
        i += 1
    ans = input('Options:\n0: Delete All Rows\nn: Delete Specific Row\n')
    if ans == '0':
        data_processing = delete_all_rows(data_processing, outliers_array)
        return data_processing
    elif 0 < int(ans) < len(outliers_array) + 1:
        data_processing = delete_specific_rows(data_processing, column, ans, outliers_array)
        return data_processing
    else:
        print('Unfortunately that is not a valid input\n')
        return data_processing


def delete_all_rows(data_processing, outliers_array):
    index = 0
    for row in outliers_array:
        data_processing = data_processing.drop(data_processing.index[row[1] - index])
        index += 1
    return data_processing


def update_outlier_array(data_processing, column, outliers_array):
    temp_array = []
    for outlier_values in outliers_array:
        temp_array.append([outlier_values[0], list(data_processing[column]).index(outlier_values[0])])
    return temp_array


def delete_specific_rows(data_processing, column, ans, outliers_array):
    data_processing = data_processing.drop(data_processing.index[outliers_array[int(ans) - 1][1]])
    del outliers_array[int(ans) - 1]
    if len(outliers_array) > 0:
        ans = input('Would you like to drop any more outliers\n1: Yes\n2: No\n')
        if ans == '1':
            outliers_array = update_outlier_array(data_processing, column,  outliers_array)
            data_processing = view_outlier_rows(data_processing, column, outliers_array)
            return data_processing
        elif ans == '2':
            return data_processing
        else:
            print('Unfortunately that is not a valid input\n')
            return data_processing
    return data_processing


def delete_outlier_rows(data_processing, outliers):
    index = 0
    for row in outliers:
        data_processing = data_processing.drop(data_processing.index[row[1] - index])
        index += 1
    return data_processing


# def grubbs_test(data_processing):
#     ans = input('Would you like to run Grubb\'s test for outliers?\n1: Yes\n2: No\n')
#     if ans == '1':
#         grubbsTest(data_processing)
#         return data_processing
#     elif ans == '2':
#         return data_processing
#     else:
#         print('Unfortunately that is not a valid input')
#         return data_processing

# def outlier_detection(data):
#     outliers = []
#     threshold = 3
#     for col in range(len(list(data.columns.values))):
#         if data.iloc[:, col].dtype not in ['object', 'str']:
#             print('{}'.format(data.columns.values[col]))
#             mean = np.mean(data.iloc[:, col])
#             std = np.std(data.iloc[:, col])
#             i = 0
#             for node in data.iloc[:, col]:
#                 z_score = (node - mean) / std
#                 if np.abs(z_score) > threshold:
#                     outliers.append([node, i])
#                 i += 1
#             if len(outliers) > 0:
#                 print('Outliers detected in {}\nValues: {}\n'.format(data.columns.values[col],
#                                                                      list(map(lambda outlier: outlier[0], outliers))))
#                 ans = input('Options:\n0: View Column\n1: View Outlier Rows\n'
#                             '2: Delete Outlier Rows\n3: Keep Outliers\n\n')
#                 if ans == '0':
#                     print('{}:\n{}\n'.format(data.columns.values[col], data.iloc[:, col]))
#                     continue
#                     # return outlier_detection(data)
#                 elif ans == '1':
#                     i = 1
#                     length = len(outliers) + 1
#                     for row in outliers:
#                         print('{}: {}\n'.format(i, data.iloc[row[1], :]))
#                         i += 1
#                     ans = input('Options:\n0: Delete All Rows\nn: Delete Specific Row\n')
#                     if ans == '0':
#                         index = 0
#                         for row in outliers:
#                             data = data.drop(data.index[row[1] - index])
#                             index += 1
#                     elif 0 < int(ans) < length:
#                         data = data.drop(data.index[outliers[int(ans) - 1][1]])
#                         del outliers[int(ans) - 1]
#                         if len(outliers) > 0:
#                             ans = input('Would you like to drop any more outliers\n1: Yes\n2: No\n')
#                             if ans == '1':
#                                 return outlier_detection(data)
#                             elif ans == '2':
#                                 continue
#                                 # return data
#                             else:
#                                 print('Unfortunately that is not a valid input\n')
#                                 continue
#                                 # outlier_detection(data)
#                     else:
#                         print('Unfortunately that is not a valid input\n')
#                         continue
#                 elif ans == '2':
#                     index = 0
#                     for row in outliers:
#                         data = data.drop(data.index[row[1] - index])
#                         index += 1
#                 elif ans == '3':
#                     continue
#                 else:
#                     print('Unfortunately that is not a valid input\n')
#                     outlier_detection(data)
#                 outliers = []
#             else:
#                 continue
#                 # print('No outliers detected\n')
#         ans = input('Would you like to run Grubb\'s test for outliers?\n1: Yes\n2: No\n')
#         if ans == '1':
#             _grubbs_test(data)
#             # standardize()
#             return data
#         elif ans == '2':
#             # standardize()
#             return data
#         else:
#             print('Unfortunately that is not a valid input')
#             # standardize()
#             return data

# def outlier_detection(data):
#     outliers = []
#     threshold = 3
#     for col in list(data.columns.values):
#         if data[col].dtype not in ['object', 'str']:
#             print('{}'.format(col))
#             mean = np.mean(data[col])
#             std = np.std(data[col])
#             i = 0
#             for node in data[col]:
#                 z_score = (node - mean) / std
#                 if np.abs(z_score) > threshold:
#                     outliers.append([node, i])
#                 i += 1
#             if len(outliers) > 0:
#                 print('Outliers detected in {}\nValues: {}\n'.format(data[col],
#                                                                      list(map(lambda outlier: outlier[0], outliers))))
#                 ans = input('Options:\n1: View Outlier Rows\n2: Delete Outlier Rows\n')
#                 if ans == '1':
#                     i = 1
#                     length = len(outliers) + 1
#                     for row in outliers:
#                         print('{}: {}\n'.format(i, data.iloc[row[1], :]))
#                         i += 1
#                     ans = input('Options:\n0: Delete All Rows\nn: Delete Specific Row\n')
#                     if ans == '0':
#                         index = 0
#                         for row in outliers:
#                             data = data.drop(data.index[row[1] - index])
#                             index += 1
#                     elif 0 < int(ans) < length:
#                         data = data.drop(data.index[outliers[int(ans) - 1][1]])
#                         del outliers[int(ans) - 1]
#                         if len(outliers) > 0:
#                             ans = input('Would you like to drop any more outliers\n1: Yes\n2: No\n')
#                             if ans == '1':
#                                 return outlier_detection(data)
#                             elif ans == '2':
#                                 return data
#                             else:
#                                 print('Unfortunately that is not a valid input\n')
#                                 outlier_detection(data)
#                     else:
#                         print('Unfortunately that is not a valid input\n')
#                 elif ans == '2':
#                     index = 0
#                     for row in outliers:
#                         data = data.drop(data.index[row[1] - index])
#                         index += 1
#                 else:
#                     print('Unfortunately that is not a valid input\n')
#                     outlier_detection(data)
#                 outliers = []
#             else:
#                 continue
#         # print('No outliers detected\n')
#         ans = input('Would you like to run Grubb\'s test for outliers?\n1: Yes\n2: No\n')
#         if ans == '1':
#             _grubbs_test(data)
#             # standardize()
#             return data
#         elif ans == '2':
#             # standardize()
#             return data
#         else:
#             print('Unfortunately that is not a valid input')
#             # standardize()
#             return data