import h5py
import csv
import json
import os
import tensorflow as tf
import numpy as np
from NeuralNetwork import NeuralNetwork
from Layer import Layer
from Perceptron import Perceptron

activation_functions = []
# Abrir o arquivo de configuração json e extrair as funções de ativação das camadas densas
with open('modelo_extraido\\config.json', 'r') as f:
    
    config = json.load(f)
    layers_config = config['config']['layers']
    for layer_iterator in range(len(layers_config)):
        layer_config = layers_config[layer_iterator]
        if layer_config['class_name'] == 'Dense':
            activation_functions.append(layer_config['config']['activation'])

# Abrir o arquivo h5
with h5py.File('modelo_extraido\\model.weights.h5', 'r') as f:
    
    layers_contents = f.get('layers')
    print("Quantidade de camadas:", len(layers_contents))
    layers = []
    for layer_iterator in range(len(list(layers_contents.keys()))):
        layer_name = list(layers_contents.keys())[layer_iterator]
        weights = layers_contents[layer_name]['vars']['0'][:]
        bias = layers_contents[layer_name]['vars']['1'][:]
        neurons = []
        for neuron_iterator in range(len(bias)):
            weight = []
            for weight_iterator in range(len(weights)):
                weight.append(float(weights[weight_iterator][neuron_iterator]))
            neurons.append(Perceptron(weights=weight, bias=float(bias[neuron_iterator])))
        layers.append(Layer(neurons=neurons, activation_function=activation_functions[layer_iterator]))
        
neuralNetwork = NeuralNetwork(layers=layers)        

inputs = []
with open('x_test.csv', mode='r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    inputs = list(leitor)

for i in range(len(inputs)):
    for j in range(len(inputs[i])):
        inputs[i][j] = float(inputs[i][j])

outputs = []
for input in inputs:
    outputs.append(neuralNetwork.feedforward(input))   

inputs_model = np.array(inputs)
model = tf.keras.models.load_model('model.keras')
outputs_keras = model.predict(inputs_model)

for i in range(len(outputs_keras)):
    print(f"{np.argmax(outputs_keras[i])}  ;  {np.argmax(outputs[i])}  ;  {np.argmax(outputs_keras[i]) == np.argmax(outputs[i])}")

