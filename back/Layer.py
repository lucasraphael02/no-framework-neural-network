import math

class Layer:
    def __init__(self, neurons, activation_function):
        self.neurons = neurons
        self.activation_function = activation_function

    def forward(self, inputs):
        z_values = [neuron.compute_z(inputs) for neuron in self.neurons]

        if self.activation_function == "relu":
            return [self.relu(z) for z in z_values]

        elif self.activation_function == "softmax":
            return self.softmax(z_values)

        else:
            return z_values  # linear

    def relu(self, x):
        return x if x > 0 else 0

    def softmax(self, z_values):
        exp_values = [math.exp(z) for z in z_values]
        soma = sum(exp_values)
        return [v / soma for v in exp_values]