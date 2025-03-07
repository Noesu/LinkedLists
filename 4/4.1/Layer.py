class Layer:
    def __init__(self, name="Layer"):
        self.next_layer = None
        self.name = name

    def __call__(self, layer):
        self.next_layer = layer
        return layer

class Input(Layer):
    def __init__(self, inputs: int):
        super().__init__("Input")
        self.inputs = inputs

class Dense(Layer):
    def __init__(self, inputs: int, outputs: int, activation: str):
        super().__init__("Dense")
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation

class NetworkIterator:
    def __init__(self, network):
        self.network = network

    def __iter__(self):
        layer = self.network
        while layer:
            yield layer
            layer = layer.next_layer

########################################################################################################################

nt = Input(12)
layer = nt(Dense(nt.inputs, 1024, 'relu'))
layer = layer(Dense(layer.inputs, 2048, 'relu'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))

n = 0
for x in NetworkIterator(nt):
    assert isinstance(x, Layer), "итератор должен возвращать объекты слоев с базовым классом Layer"
    n += 1

assert n == 4, "итератор перебрал неверное число слоев"

