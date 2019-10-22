import statsmodels.api as sm


def ols(target_data, train_data):
    train_data = sm.add_constant(train_data)
    print(target_data)
    print(train_data)
    try:
        results = sm.OLS(target_data, train_data).fit()
        print(results.summary())
    except:
        print('OLS not working with these dataframes\n')