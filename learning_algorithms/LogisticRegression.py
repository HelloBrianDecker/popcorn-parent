import numpy as np
import statsmodels.api as sm
import seaborn as sns
from learning_algorithms.support_algorithms import SupportAlgorithms as sa, GraphHyperparameters as graph

sns.set()



print('Logistic Regression')
class LogisticRegression:
    def __init__(self, target_data, train_data):
        self.target_data = target_data
        self.train_data = train_data
        self.final_theta = self.manipulate()

    def get_final_theta(self):
        return self.final_theta

    def termination(self, cost_array, cost):
        if cost_array[-1] - .001 < cost:
            print('early termination')
            return True
        else:
            return False

    def manipulate(self):
        train_data = self.train_data
        m = train_data.shape[0]
        train_data = np.append(np.ones((m, 1)), train_data, axis=1)
        target_data = np.array(self.target_data)
        rows = target_data.shape[0]
        target_data = target_data.reshape(rows, 1)
        theta = np.ones((train_data.shape[1], 1), dtype=float)
        cost_array = [999999.]
        e = []
        iterations = 100
        alpha = 0.1
        lambda_expression = 10
        for epoch in range(iterations):
            theta = sa.gradient_descent(train_data, target_data, theta, alpha, m)
            cost = sa.logistic_cost_function(train_data, target_data, theta, lambda_expression, m)
            if self.termination(cost_array, cost):
                print('epoch: ' + str(epoch) + ' theta')
                print(theta)
                break
            cost_array.append(float(cost[0]))
            e.append(epoch)
            epoch += 1
        del cost_array[0]
        print(graph.plot_cost_function(e, cost_array))
        reg_log = sm.Logit(target_data, train_data)
        print(reg_log)
        results_log = reg_log.fit()
        print(results_log.summary())
        return theta
