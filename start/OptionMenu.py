import sys
import pandas as pd
from start.data_variables.DataSet import DataSet
from messages.Messages import get_messages

messages = get_messages()


def main_menu():
    ans = input(messages['main_menu']['welcome'])
    if ans == '1':
        ans = input(messages['main_menu']['supervised'])
        if ans == '1':
            data = pd.read_csv('C:\\GitHub\\popcorn-parent\\csv_files\\2.02. Binary predictors.csv')
            dataset = DataSet(data)
            options(dataset)
            # file = (easygui.fileopenbox())
            # if '.csv' not in file:
            #     print(messages['errors']['csv'])
            #     main_menu()
            # else:
            #     data = pd.read_csv(file)
            #     dataset = DataSet(data)
            #     options(dataset)
        elif ans == '0':
            print('ok, well we don\'t really have anywhere else to go so....\n')
            main_menu()
        else:
            print(messages['errors']['invalid'])
            main_menu()
    elif ans == '2':
        print('Welcome to Unsupervised Machine Learning!!!\n'
              'Unfortunately this feature is not build yet so....\n')
        main_menu()
    else:
        print('Unfortunately that is not a valid input\n')
        main_menu()


def options(dataset):
    menu = input(messages['main_menu']['options'])
    if menu == '0':
        print(messages['main_menu']['autorun'])
        ans = input('1: On\n0: Off\n')
        if ans == '1':
            dataset.set_autorun(True)
            dataset.run_autorun()
            print('more to come')
        if ans == '0':
            dataset.set_autorun(False)
        options(dataset)
    elif menu == '1':
        dataset.set_preprocessing()
        process = dataset.get_preprocessing()
        print('First step is to set your target column.  '
              'This will be essential in pre-processing and analyzing your data.\n')
        process.set_target()
        process.convert_processed_data(dataset.get_data())
        print('It is best to run the first three options before visualizing your data.  '
              'It will give a clearer picture in the graphs.\n')
        preprocessing(dataset)
    elif menu == '2':
        print('Not made yet')
        options(dataset)
    elif menu == '3':
        early_choice(dataset)
    elif menu == 'x' or 'X':
        sys.exit
    else:
        print('Unfortunately, that is not a valid command\n')
        options(dataset)


def preprocessing(dataset):
    process = dataset.get_preprocessing()
    markers = dataset.get_preprocessing_markers()
    while markers.get_processed_finalized():
        menu = input(messages['main_menu']['options_processing'].format(
                                        markers.get_null_marker(),
                                        markers.get_outlier_marker(),
                                        markers.get_qualitative_marker(),
                                        markers.get_cluster_marker(),
                                        markers.get_separate_marker(),
                                        markers.get_standardize_marker()))
        if menu == '0':
            process.manipulate_dataset()
        elif menu == '1':
            process.null_count()
            markers.set_null_marker()
        elif menu == '2':
            if markers.get_null_marker() is False:
                print('Its best to remove null values before converting\n')
            else:
                process.outlier_detection()
                markers.set_outlier_marker()
        elif menu == '3':
            if markers.get_outlier_marker() is False:
                print('Its best to check for outliers before converting into numeric values\n')
            else:
                process.separate()
                markers.set_qualitative_marker()
        elif menu == '4':
            if markers.get_qualitative_marker() is False:
                print(messages['main_menu']['convert'])
            else:
                process.cluster_analysis()
                markers.set_cluster_marker()
        elif menu == '5':
            if markers.get_qualitative_marker() is False:
                print(messages['main_menu']['convert'])
            else:
                process.split_data()
                markers.set_separate_marker()
        elif menu == '6':
            if markers.get_qualitative_marker() is False:
                print(messages['main_menu']['convert'])
            else:
                process.standardize()
                markers.set_standardize_marker()
        elif menu == '7':
            if markers.get_all_markers():
                decision(dataset)
            else:
                early_choice(dataset)
        elif menu == '8':
            print(process.view_data(), '\n')
        elif menu == '99':
            print('Help Menu')
        elif menu == 'x' or 'X':
            sys.exit
        else:
            print(messages['main_menu']['invalid'])


def early_choice(dataset):
    markers = dataset.get_preprocessing_markers()
    print('It is not suggested you continue without completing these steps.\n'
          'Failure to complete these steps will most likely result in the '
          'Algorithm failing to converge or encountering an error.\n')
    for key, value in markers.get_markers().items():
        if value is False:
            print('{} is still set to False\n'.format(key))
    if markers.get_targer_marker() is True:
        ans = input(messages['main_menu']['no_target'])
        if ans == '0':
            decision(dataset)
        elif ans == '1':
            preprocessing(dataset)
        else:
            print(messages['main_menu']['invalid'])
            preprocessing(dataset)
    else:
        print('You must set the target column of your DataFrame\n')
        dataset.set_preprocessing()
        preprocessing(dataset)


def decision(dataset):
    ans = input(messages['main_menu']['algorithm'])
    if ans == '1':
        dataset.set_logistic_regression()
    elif ans == '2':
        dataset.set_linear_regression()
    elif ans == '3':
        dataset.set_neural_network()
    else:
        print('That is not a valid input\n')
        decision(dataset)


if __name__ == '__main__':
    main_menu()