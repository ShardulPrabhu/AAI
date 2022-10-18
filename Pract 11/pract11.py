from math import exp
from random import seed
from random import random
print("Performed By Shardul Prabhu. ROll no: 27 ");
# Initialize a network
def initialize_network(n_inputs, n_hidden, n_outputs):
    Network = list()
    Hidden_layer = [{'weights':[random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
    Network.append(Hidden_layer)
    Output_layer = [{'weights': [random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
    Network.append(Output_layer)
    return Network

# Calculate neuron activation for an input
def activate(Weights, Inputs):
    Activation = Weights[-1]
    for i in range(len(Weights)-1):
        Activation += Weights[i] * Inputs[i]
    return Activation

# Transfer neuron activation
def transfer(Activation):
    return 1.0 / (1.0 + exp(-Activation))


# Forward propagate input to a network output
def forward_propagate(Net, Row):
    Inputs = Row
    for layer in Net:
        New_inputs = []
        for neuron in layer:
            Activation = activate(neuron['weights'], Inputs)
            neuron['output'] = transfer(Activation)
            New_inputs.append(neuron['output'])
        Inputs = New_inputs
    return Inputs

# Make a prediction with a network
def predict(Net, Row):
    Outputs = forward_propagate(Net, Row)
    return Outputs.index(max(Outputs))

# Test making predictions with the network
ds = [[2.7810836,2.550537003,0],
    [1.465489372,2.362125076,0],
    [3.396561688,4.400293529,0],
    [1.38807019,1.850220317,0],
    [3.06407232,3.005305973,0],
    [7.627531214,2.759262235,1],
    [5.332441248,2.088626775,1],
    [6.922596716,1.77106367,1],
    [8.675418651,-0.242068655,1],
    [7.673756466,3.508563011,1]]
Net = [[{'weights': [-1.482313569067226, 1.8308790073202204, 1.078381922048799]},
    {'weights': [0.23244990332399884, 0.3621998343835864, 0.40289821191094327]}],
    [{'weights': [2.5001872433501404, 0.7887233511355132, -1.1026649757805829]},
    {'weights': [-2.429350576245497, 0.8357651039198697, 1.0699217181280656]}]]
for Row in ds:
    pred = predict(Net, Row)
    print('Expected=%d, Got=%d' % (Row[-1], pred))

# Calculate the derivative of an neuron output
def transfer_derivative(Output):
    return Output * (1.0 - Output)

# Backpropagate error and store in neurons
def backward_propagate_error(Net, Exp):
    for i in reversed(range(len(Net))):
        layer1 = Net[i]
        errors1 = list()
        if i != len(Net)-1:
            for j in range(len(layer1)):
                err = 0.0
                for neuron1 in Net[i + 1]:
                    err += (neuron1['weights'][j] * neuron1['delta'])
                errors1.append(err)
        else:
            for j in range(len(layer1)):
                neuron1 = layer1[j]
                errors1.append(Exp[j] - neuron1['output'])
        for j in range(len(layer1)):
            neuron1 = layer1[j]
            neuron1['delta'] = errors1[j] * transfer_derivative(neuron1['output'])

# Update network weights with error
def update_weights(Net, Row, learn_rate):
    for i in range(len(Net)):
        Inputs1 = Row[:-1]
        if i != 0:
            Inputs1 = [neuron1['output'] for neuron1 in Net[i - 1]]
        for neuron1 in Net[i]:
            for j in range(len(Inputs1)):
                neuron1['weights'][j] += learn_rate * neuron1['delta'] * Inputs1[j]
            neuron1['weights'][-1] += learn_rate * neuron1['delta']


# Train a network for a fixed number of epochs
def train_network(Net, train, learn_rate, n_Epoch, n_Outputs):
    for Epoch in range(n_Epoch):
        Total_error = 0
        for row in train:
            outputs1 = forward_propagate(Net, Row)
            expect = [0 for i in range(n_Outputs)]
            expect[row[-1]] = 1
            Total_error += sum([(expect[i] - outputs1[i]) ** 2 for i in range(len(expect))])
            backward_propagate_error(Net, expect)
            update_weights(Net, Row, learn_rate)
        print('>epoch=%d, learnrate=%.3f, error=%.3f' % (Epoch, learn_rate,Total_error))


# Test training backprop algorithm
seed(1)
dataset = [[2.7810836,2.550537003,0],
    [1.465489372,2.362125076,0],
    [3.396561688,4.400293529,0],
    [1.38807019,1.850220317,0],
    [3.06407232,3.005305973,0],
    [7.627531214,2.759262235,1],
    [5.332441248,2.088626775,1],
    [6.922596716,1.77106367,1],
    [8.675418651,-0.242068655,1],
    [7.673756466,3.508563011,1]]
n_inputs = len(dataset[0]) - 1
n_outputs = len(set([row[-1] for row in dataset]))
network = initialize_network(n_inputs, 2, n_outputs)
train_network(network, dataset, 0.5, 20, n_outputs)
for layer in network:
    print(layer)
