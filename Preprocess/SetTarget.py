def set_target(data):
    i = 0
    print('Which column will be used as the target column?\n')
    headers = list(data.columns.values)
    for col in headers:
        print(i, ': {}'.format(col))
        i += 1
    target = int(input(''))
    target_data_name = data.columns.values[target]
    return target_data_name