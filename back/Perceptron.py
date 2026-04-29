from back.MacUnit import MacUnit

class Perceptron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def compute_z(self, inputs):
        mac_unit = MacUnit()
        mac_unit.accumulator.entry = self.bias
        mac_unit.accumulator.step()
        for weight, input in zip(self.weights, inputs):
            mac_unit.step(weight, input)
        return mac_unit.output
        
    