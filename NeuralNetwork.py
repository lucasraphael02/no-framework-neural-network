class NeuralNetwork:
    def __init__(self, layers):
        self.layers = layers

    def feedforward(self, inputs):
        for layer in self.layers:
            inputs = layer.forward(inputs)
        return inputs
    