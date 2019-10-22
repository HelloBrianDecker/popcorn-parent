import pandas as pd


def null_count_columns(data):
    for col in (list(data.columns)):
        if data[col].isnull().any():
            total = data[col].isnull().sum()
            percent = total / len(data[col]) * 100
            print('{}: - has {} null values.  {}% of values.\n'.format(col, total, round(percent, 2)))
            ans = input('Would you like to delete this column?\n1: Yes\n2: No\n')
            if ans == '1':
                data = data.drop([col], axis=1)
            elif ans == '2':
                continue
            else:
                print('Unfortunately that is not a valid input\n')
                continue
        else:
            continue
    return data


def null_count_rows(data):
    total = data.isnull().sum().sort_values(ascending=False)
    percent = (data.isnull().sum() / data.isnull().count()).sort_values(ascending=False)
    missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    print('Null values found: {}\n\n'.format(missing_data))
    null_counts = data.isnull().sum()
    if data.isnull().values.any():
        print(null_counts[null_counts > 0].sort_values(ascending=False), '\n')
        ans = input('Would you like to drop all null rows?\n1: Yes\n0: No\n')
        if ans == '1':
            data = data.dropna(axis=0)
            return data
        elif ans == '0':
            print('Convert all NA to *\n')
            return data
        else:
            print('Unfortunately, that is not a valid command\n')
            null_count_rows(data)
    else:
        print('No null values found\n')
        return data

#
# def null_count_check(data, dataset):
#     markers = dataset.get_preprocessing_markers()
#     total = data.isnull().sum().sort_values(ascending=False)
#     percent = (data.isnull().sum() / data.isnull().count()).sort_values(ascending=False)
#     missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
#     print(missing_data, '\n')
#     ans = input('It appears you have null values in your data-set.  Would you like to fix that now?\n1: Yes\n2: No\n')
#     if ans == '1':
#         data = null_count(data)
#         markers.set_null_marker()
#         return data
#     if ans == '2':
#         return data
#     else:
#         print('Unfortunately that is not a correct input\n')