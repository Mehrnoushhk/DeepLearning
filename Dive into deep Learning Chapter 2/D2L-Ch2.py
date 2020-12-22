from mxnet import np, npx

# When using tensors, we almost always invoke the set_np function: this is for compatibility of tensor processing by other components of MXNet.
npx.set_np()
x = np.arange(0, 12)
print(x)
print(x.shape)
X = x.reshape(3,4)
print(X)

# Fortunately, tensors can automatically work out one dimension given the rest. We invoke this capability by placing -1 for the dimension that we would like tensors to automatically infer
Y = x.reshape(-1, 4)
print(Y)

# We can create a tensor representing a tensor with all elements set to 0 and a shape of (2, 3, 4) as follows
X = np.zeros((2, 3, 4))
print(X)

# Each of its elements is randomly sampled from a standard Gaussian (normal) distribution with a mean of 0 and a standard deviation of 1
X = np.random.normal(0, 1, size=(3, 4))
print(X)

# We can also specify the exact values for each element in the desired tensor by supplying a Python list (or list of lists) containing the numerical values.
X = np.array([[2, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
print(X)

