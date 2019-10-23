import numpy as np


def split_data(data, target_name):
    m = len(data)
    if m < 10000:
        ans = input('It seems that you are working with a smaller data-set.  '
                    'It is suggested to use a 80/10/10 split of your data.\n'
                    '80% - Train\n10% - Validate\n10% - Test\n'
                    'Would you like to use this or select another split?\n'
                    '1: Yes\n2: No\n')
        if ans == '1':
            percent = .8
            div = ((1 - percent) / 2) + percent
            data_train, data_validate, data_test = np.split(data.sample(frac=1),
                                                            [int(percent * len(data)), int(div * len(data))])
            train_targets, train_inputs = convert_data(data_train, target_name)
            validate_targets, validate_inputs = convert_data(data_validate, target_name)
            test_targets, test_inputs = convert_data(data_test, target_name)
            return train_inputs, train_targets, validate_inputs, validate_targets, test_inputs, test_targets
        elif ans == '2':
            ans = input('How big would you like your train data-set to be?\n'
                        '1: 60%\n2: 70%\n3: 90%\n')
            if ans == '1':
                percent = .6
                div = ((1 - percent) / 2) + percent
                data_train, data_validate, data_test = np.split(data.sample(frac=1),
                                                                [int(percent * len(data)), int(div * len(data))])
                train_targets, train_inputs = convert_data(data_train, target_name)
                validate_targets, validate_inputs = convert_data(data_validate, target_name)
                test_targets, test_inputs = convert_data(data_test, target_name)
                return train_inputs, train_targets, validate_inputs, validate_targets, test_inputs, test_targets
            elif ans == '2':
                percent = .7
                div = ((1 - percent) / 2) + percent
                data_train, data_validate, data_test = np.split(data.sample(frac=1),
                                                                [int(percent * len(data)), int(div * len(data))])
                train_targets, train_inputs = convert_data(data_train, target_name)
                validate_targets, validate_inputs = convert_data(data_validate, target_name)
                test_targets, test_inputs = convert_data(data_test, target_name)
                return train_inputs, train_targets, validate_inputs, validate_targets, test_inputs, test_targets
            elif ans == '3':
                percent = .9
                div = ((1 - percent) / 2) + percent
                data_train, data_validate, data_test = np.split(data.sample(frac=1),
                                                                [int(percent * len(data)), int(div * len(data))])
                train_targets, train_inputs = convert_data(data_train, target_name)
                validate_targets, validate_inputs = convert_data(data_validate, target_name)
                test_targets, test_inputs = convert_data(data_test, target_name)
                return train_inputs, train_targets, validate_inputs, validate_targets, test_inputs, test_targets
            else:
                print('Unfortunately that is not a valid input\n')
                split_data(data, target_name)

        else:
            print('Unfortunately that is not a valid input\n')
            split_data(data, target_name)


def convert_data(data, target_name):
    data_targets = data[target_name]
    train_data = data.drop([target_name], axis=1)
    return data_targets, train_data




