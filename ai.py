# -*- coding: utf-8 -*-
"""ai.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mw7hX3Yx4iylQLBe897iva-tD2WULmNp
"""

pip install numpy pandas matplotlib scikit-learn torch

from sklearn.datasets import make_regression
import pandas as pd

# Generate synthetic dataset with 500 samples and 3 features
X, y = make_regression(n_samples=500, n_features=3, noise=0.1, random_state=42)

# Convert to DataFrame for saving and handling
df = pd.DataFrame(X, columns=['x1', 'x2', 'x3'])
df['y'] = y

# Save to a CSV file for later use
df.to_csv('dataset_q2_q4.csv', index=False)

print("Dataset created and saved as 'dataset_q2_q4.csv'")

import numpy as np

# Hypothesis function
def h(theta, x1, x2):
    return 4 * theta[1] * (x1 * 3) + theta[2] * (x2 * 2) - theta[3] * theta[1] * (x2 ** 2) + theta[0]

# Cost function
def compute_cost(theta, X, y):
    m = len(y)
    total_cost = 0
    for i in range(m):
        x1, x2 = X[i]
        total_cost += (h(theta, x1, x2) - y[i]) ** 2
    return total_cost / (2 * m)

# Partial derivatives of cost function with respect to theta_0, theta_1, theta_2, theta_3
def compute_gradients(theta, X, y):
    m = len(y)
    grad = np.zeros(len(theta))

    for i in range(m):
        x1, x2 = X[i]
        error = h(theta, x1, x2) - y[i]

        # Partial derivative with respect to theta_0
        grad[0] += error

        # Partial derivative with respect to theta_1
        grad[1] += error * (12 * (x1 * 2) - theta[3] * (x2 * 2))

        # Partial derivative with respect to theta_2
        grad[2] += error * (2 * x2)

        # Partial derivative with respect to theta_3
        grad[3] += error * (-theta[1] * (x2 ** 2))

    return grad / m

# Gradient descent update rule
def gradient_descent(X, y, theta, alpha, epochs):
    cost_history = []

    for epoch in range(epochs):
        gradients = compute_gradients(theta, X, y)
        theta -= alpha * gradients

        cost = compute_cost(theta, X, y)
        cost_history.append(cost)

        if epoch % 100 == 0:
            print(f"Epoch {epoch}, Cost: {cost}")

    return theta, cost_history

# Example dataset (x1, x2, y)
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y = np.array([10, 20, 30, 40])

# Initial parameters for theta_0, theta_1, theta_2, theta_3
theta_initial = np.array([0.0, 0.0, 0.0, 0.0])

# Learning rate and number of iterations
alpha = 0.01
epochs = 1000

# Run gradient descent
theta_optimal, cost_history = gradient_descent(X, y, theta_initial, alpha, epochs)

print(f"Optimal parameters: {theta_optimal}")

import pandas as pd
from sklearn.model_selection import train_test_split

# Load the dataset
data = pd.read_csv('dataset_q2_q4.csv')

# Features (x1, x2, x3) and target (y)
X = data[['x1', 'x2', 'x3']]
y = data['y']

# Split into 60% train and 40% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

import pandas as pd
from sklearn.model_selection import train_test_split

# Load the dataset
data = pd.read_csv('dataset_q2_q4.csv')

# Features (x1, x2, x3) and target (y)
X = data[['x1', 'x2', 'x3']]
y = data['y']

# Split into 60% train and 40% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

import numpy as np

def linear_regression(X, y, learning_rate=0.01, epochs=1000):
    m, n = X.shape
    X = np.c_[np.ones(m), X]  # Adding a bias term (column of 1s)
    theta = np.zeros(n+1)  # Initialize weights (including bias)

    for epoch in range(epochs):
        predictions = X.dot(theta)
        errors = predictions - y
        gradient = (1/m) * X.T.dot(errors)
        theta -= learning_rate * gradient

    return theta

theta = linear_regression(X_train.values, y_train.values)
print(f"Optimal parameters (from scratch): {theta}")

import torch
import torch.nn as nn

# Convert data to PyTorch tensors
X_train_tensor = torch.tensor(X_train.values, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train.values, dtype=torch.float32).view(-1, 1)

# Define model
model = nn.Linear(X_train_tensor.shape[1], 1)

# Loss function and optimizer
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# Training loop
epochs = 1000
loss_values = []

for epoch in range(epochs):
    model.train()

    # Forward pass
    outputs = model(X_train_tensor)
    loss = criterion(outputs, y_train_tensor)

    # Backward pass and optimization
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    loss_values.append(loss.item())

    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item()}")

# Get the learned parameters (theta)
theta_pytorch = model.state_dict()
print(f"Optimal parameters (PyTorch): {theta_pytorch}")

from sklearn.datasets import make_regression

X, y = make_regression(n_samples=800, n_features=15, noise=0.1, random_state=10)

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

from sklearn.linear_model import Lasso

lasso = Lasso(alpha)

from sklearn.linear_model import Lasso

# Create and train the Lasso model
lasso = Lasso(alpha=0.1)
lasso.fit(X_train, y_train)

# Predict on the test set
y_pred_lasso = lasso.predict(X_test)

from sklearn.linear_model import Ridge

# Create and train the Ridge model
ridge = Ridge(alpha=0.1)
ridge.fit(X_train, y_train)

# Predict on the test set
y_pred_ridge = ridge.predict(X_test)

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Create polynomial features
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X_train)

# Create and train the model using the transformed polynomial features
model_poly = LinearRegression()
model_poly.fit(X_poly, y_train)

# Predict on the test set (with polynomial transformation)
y_pred_poly = model_poly.predict(poly.transform(X_test))

from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Calculate the Mean Squared Errors for each model
mse_linear = mean_squared_error(y_test, y_pred)
mse_lasso = mean_squared_error(y_test, y_pred_lasso)
mse_ridge = mean_squared_error(y_test, y_pred_ridge)
mse_poly = mean_squared_error(y_test, y_pred_poly)

# Print MSE values for each model
print(f"Linear Regression MSE: {mse_linear}")
print(f"Lasso Regression MSE: {mse_lasso}")
print(f"Ridge Regression MSE: {mse_ridge}")
print(f"Polynomial Regression MSE: {mse_poly}")

# Plot the MSE values
mse_values = [mse_linear, mse_lasso, mse_ridge, mse_poly]
labels = ['Linear', 'Lasso', 'Ridge', 'Polynomial']

plt.bar(labels, mse_values)
plt.ylabel('Mean Squared Error')
plt.title('Comparison of MSE for Different Models')
plt.show()

import numpy as np

def normal_equation(X, y):
    # Add a bias term (a column of ones) to X
    X_b = np.c_[np.ones((X.shape[0], 1)), X]

    # Compute the optimal values of theta using the normal equation
    theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

    return theta_best

# Compute theta using the normal equation
theta_normal = normal_equation(X_train, y_train)

print(f"Optimal parameters from Normal Equation: {theta_normal}")