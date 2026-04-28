class Perceptron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def compute_z(self, inputs):
        total = self.bias
        for i in range(len(inputs)):
            total += inputs[i] * self.weights[i]
        return total
    