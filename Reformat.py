import pandas as pd


def label_encoder(data_processing):
    data_processing = pd.get_dummies(data_processing)
    return data_processing


def convert_target(data_processing):
    if len(list(set(data_processing))) == 2:
        set_columns = list(set(data_processing))
        data_processing = data_processing.map({set_columns[1]: 0, set_columns[0]: 1})
        print('{}: has been set to 0\n{}: has been set to 1\n'.format(set_columns[0], set_columns[1]))
        return data_processing
    else:
        ans = input('It seems that this is not a Logistic Regression Model.\n'
                    'If the target values are categorical they can be OneHotEncoded\n'
                    'Would you like to OneHotEncode your targets?\n'
                    'This is not suggested if you are running Linear Regression\n\n1: Yes\n2: No\n')
        if ans == '1':
            data_processing = label_encoder(data_processing)
            return data_processing
        if ans == '2':
            return data_processing
        else:
            print('Unfortunately that is not a valid input\n')
            return data_processing


# def separate(data):
#     qual_cols = [col for col in data.columns if data[col].dtype in ['object', 'str']]
#     quan_cols = [col for col in data.columns if data[col].dtype not in ['object', 'str']]
#     print('Qualitative columns ({} columns):\n{}\n'.format(len(qual_cols), data[qual_cols].columns))
#     print('Quantitative columns ({} columns):\n{}\n'.format(len(quan_cols), data[quan_cols].columns))
#     if len(qual_cols) > 0:
#         ans = input('Would you like to onehotencode the qualitative columns?\n1: Yes\n2: No\n')
#         if ans == '1':
#             data = labelencoder(data)
#             # reformat_columns(data, qual_cols)
#         elif ans == '2':
#             pass
#         else:
#             print('Unfortunately that is not a correct input\n')
#     else:
#         pass
#     return data
#
#
# def reformat_columns(data, qual_cols):
#     for columns in qual_cols:
#         set_columns = list(set(data[columns]))
#         print('Qualitative column values ({}:\n{}\n'.format(columns, set_columns))
#         if len(set_columns) == 2:
#             data[columns] = data[columns].map({set_columns[1]: 0, set_columns[0]: 1})
#             print('{}: has been set to 0\n{}: has been set to 1\n'.format(set_columns[0], set_columns[1]))
#         else:
#             print('have to separate into vector and still let it be inside the dataset\n')
#     return data


