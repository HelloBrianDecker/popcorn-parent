import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


def degree_polynomial(train_data, validation_data, train_target, validation_target, degree_polynomial):
    pass


def plot_cost_function(e, cost_array):
    plt.plot(e, cost_array, 'r+')
    return plt.show()


def lambda_expression(lambda_exp, cost):
    plt.plot(lambda_exp, cost, 'r+')
    return plt.show()

def learning_curves():
    pass