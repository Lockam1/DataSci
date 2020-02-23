from sklearn.datasets import load_iris
iris = load_iris()

iris.keys()

n_samples, n_features = iris.data.shape
print (n_samples, n_features)

#shows how many records(samples) there are in the table (first number printed), second number shows how many features are recorded.
print(iris.data[0])

print(iris.target.shape)

#prints first instance from the target list
print(iris.target[0])

#prints all items in the target as result - what the outcome will be. The number the indicates what the outcome is.
print(iris.target)

#Block of code used to display a scatter plot of the data set outcome based of 2 paramiters.
import numpy as np
import matplotlib.pyplot as plt

def plot_iris_projection(x_index, y_index):
    # this formatter will label the colorbar with the correct target names
    formatter = plt.FuncFormatter(lambda i, *args: iris.target_names[int(i)])

    plt.scatter(iris.data[:, x_index], iris.data[:, y_index],
                c=iris.target)
    plt.colorbar(ticks=[0, 1, 2], format=formatter)
    plt.xlabel(iris.feature_names[x_index])
    plt.ylabel(iris.feature_names[y_index])

x_index=3
y_index=2
plot_iris_projection(x_index,y_index)

