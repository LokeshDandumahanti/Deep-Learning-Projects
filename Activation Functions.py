import math

def sigmoid(x):
    return 1 (1 + math.exp(-x))

a = sigmoid(20)
b = sigmoid(100)

print(a)
print(b)

def tanh(x):
    return (math.exp(x) - math.exp(-x))/(math.exp(x) + math.exp(-x))

c = tanh(20)
d = tanh(100)

print(c)
print(d)

def relu(x):
    return max(0,x)

e = relu(40)
d = relu(-10)

def leaky_relu(x):
    return max(0.1*x, x)

f = leaky_relu(-39)
g = leaky_relu(90)

print(f)
print(g)