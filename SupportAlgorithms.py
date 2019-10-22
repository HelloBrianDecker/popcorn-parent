import numpy as np


def gradient_descent(train_data, target_data, theta, alpha, m):
    hyp = sigmoid(train_data, theta)
    theta = theta - (alpha / m) * np.dot(train_data.T, (hyp - target_data))
    return theta


def sigmoid(train_data, theta):
    z = np.dot(train_data, theta)
    hyp = 1 / (1 + np.exp(-z))
    return hyp


def logistic_cost_function(train_data, target_data, theta, lambda_expression, m):
    theta[0] = 1
    hyp = sigmoid(train_data, theta)
    error = (np.dot(target_data.T, np.log(hyp))) + (np.dot((1 - target_data).T, np.log(1 - hyp)))
    regularization = (lambda_expression / (2 * m)) * sum(theta ** 2)
    cost = (-(1 / m) * error) + regularization
    return cost


def sigmoid_gradient(self):
    pass