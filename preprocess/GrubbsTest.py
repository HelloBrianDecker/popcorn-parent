import numpy as np
import scipy.stats as stats


def _grubbs_test(data):
    alpha = 0.5
    i = 0
    ans = input('What degree of certainty would you like?\n1: 90%\n2: 95%\n3: 99%\n'
                'Standard is 95%\n')
    if ans == '1':
        alpha = 0.1
    elif ans == '2':
        alpha = 0.05
    elif ans == '3':
        alpha = 0.01
    else:
        print('Unfortunately that is not a valid input\n')
    for col in range(len(list(data.columns))):
        try :
            y = data.iloc[:, col]
            size = len(y)
            # x = np.arange(len(y))
            # plt.scatter(x, y)
            # plt.show()
            y_hat = np.mean(y)
            std = np.std(y)
            abs_val_minus_y_hat = abs(y - y_hat)
            max_deviation = max(abs_val_minus_y_hat)
            g_calculated = max_deviation / std
            t_dist = stats.t.ppf(1 - alpha / (2 * size), size - 2)
            numerator = (size - 1) * np.sqrt(np.square(t_dist))
            denominator = np.sqrt(size) * np.sqrt(size - 2 + np.square(t_dist))
            g_critical = numerator / denominator
            i += 1
            if g_calculated > g_critical:
                print(i, ': {}'.format(list(data.columns.values)[col]))
                print('According to Grubb\'s Test for Outlier Detection:' + '\n' +
                      'the null hypothesis that there are no outliers in the data, can be rejected' + '\n' +
                      'the alternative hypothesis is accepted with a significance of ' + str(alpha))
                print('Mean of data set: ' + str(y_hat) + '\n')
                print('Standard deviation: ' + str(std) + '\n')
                print('Max deviation from rest: ' + str(max_deviation) + '\n')
                print('G_Calculated: ' + str(g_calculated) + '\n')
                print("Grubb\'s Critical Value: {}".format(g_critical) + '\n')
                print("Grubb\'s Test has been created using a alpha with a value of {}\n".format(alpha))
            else:
                print(i, ': {}'.format(list(data.columns.values)[col]))
                print('According to Grubb\'s Test for Outlier Detection:' + '\n' +
                      'the null hypothesis that there are no outliers in the data, cannot be rejected\n')
        except:
            (print('String values found, once they are converted into numeric values you can run the test again\n'))