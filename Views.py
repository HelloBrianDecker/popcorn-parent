from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


def _column_list(data):
    i = 1
    for col in range(len(list(data.columns))):
        print('{}: {}\n'.format(i, list(data.columns.values)[col]))
        i += 1
    ans = input('Which column would you like to select?\n')
    return int(ans) - 1


def view_data(data):
    display(data)
    ans = input('Would you like to view all graphs?\n1: All Graphs\n2: Select Graph\n3: Exit\n')
    if ans == '1':
        for col in range(len(list(data.columns))):
            column = data.iloc[:, col]
            print('Column: {}\n'.format(list(data.columns.values)[col]))
            print(column.describe())
            try:
                sns.distplot(column)
                plt.show()
                print('Skewness: {}\n'.format(column.skew()))
                print('Kurtosis: {}\n'.format(column.kurt()))
            except TypeError:
                print('Qualitative values cannot be show on distplot.  '
                      'Once data is converted they will have distplots\n')
                continue
    elif ans == '2':
        ans = _column_list(data)
        column = data.iloc[:, ans]
        print('Column: {}\n'.format(list(data.columns.values)[ans]))
        print(column.describe())
        try:
            sns.distplot(column)
            plt.show()
            print('Skewness: {}\n'.format(column.skew()))
            print('Kurtosis: {}\n'.format(column.kurt()))
        except:
            print('Qualitative values cannot be show on distplot.  Once data is converted they will have distplots\n')
    elif ans == '3':
        return
    else:
        print('Unfortunately that is not a correct input\n')
        view_data(data)