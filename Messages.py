messages = {
    'main_menu': {
            'welcome': 'Welcome to your Machine Learning!!!\n\n'
                       'Are you working on Supervised or Unsupervised Machine Learning?\n'
                       '1: Supervised Machine Learning\n2: Unsupervised Machine Learning\n',

            'supervised': 'Welcome to Supervised Machine Learning!!!\n\n'
                          'The first step will be collecting a .csv file\n'
                          'Are you ready to input a file?\n1: Yes\n0: No\n',

            'options':  'Options:\n'
                        '0: Turn On or Off AutoRun - Off by Default\n'
                        '1: Preprocess Data\n'
                        '2: Manipulate Data\n'
                        '3: Choose Algorithm\n'
                        'X: Exit\n',

            'autorun': 'If On AutoRun will make almost all the decisions for you,'
                       ' you just sit back and see what comes\n'
                       'If Off AutoRun you will be in the drivers seat where you '
                       'will be helping to improve the preprocessing of the data.\n'
                       'This is a very important part of statistics and machine learning\n',

            'target': 'First step is to set your target column.  This will be essential '
                      'in pre-processing and analyzing your data.\n',

            'options_processing': 'Options: \n'
                                  '0: Drop Rows or Columns\n'
                                  '1: Check for null values - {}\n'
                                  '2: Check for Outliers - {}\n'
                                  '3: Convert Qualitative values - {}\n'
                                  '4: Cluster Analysis - {}\n'
                                  '5: Separate data into Train, Validate, and Test - {}\n'
                                  '6: Standardize Data - {}\n'
                                  '7: Set Learning Algorithms\n'
                                  '8: View Data\n'
                                  '99: Help\n'
                                  'X: Exit\n\n',

            'convert': 'Its best to convert data into numeric values first or you will run into problems\n',

            'algorithm': 'Which type of Learning Algorithms would you like to use:\n\n'
                         '\n1: Logistic Regression'
                         '\n2: Linear Regression'
                         '\n3: Neural Network\n',

            'no_target': 'If you have set the target you can continue to assigning an Algorithm, '
                         'unless your data is already preprocessed this '
                         'will most likely result in errors\n''Would you still like to continue?\n''0: Yes\n''1: No\n'
         },
    "errors": {
            'csv': 'Unfortunately, that doesn\'t seem to be a .csv file\n',

            'invalid': 'Unfortunately that is not a valid input\n'
     }
}


def get_messages():
    return messages

    #     print('It is best to run the first three options before visualizing your data.  '
    #           'It will give a clearer picture in the graphs.\n')
    #
    #
    #
    #
    #     if markers.get_null_marker() is False:
    #         print('Its best to remove null values before converting\n')
    #
    #         print('Its best to check for outliers before converting into numeric values\n')
    #
    #
    # print('It is not suggested you continue without completing these steps.\n'
    #       'Failure to complete these steps will most likely result in the '
    #       'Algorithm failing to converge or encountering an error.\n')
    #
    #         print('{} is still set to False\n'.format(key))
    #
    #     print()
    #
    # else:
    #     print('You must set the target column of your DataFrame\n')
    #
