class Adder:
    
    def __init__(self, entryA=0, entryB=0):
        self.entryA = entryA
        self.entryB = entryB
        self.result = None

    def step(self):
        self.result = self.entryA + self.entryB

