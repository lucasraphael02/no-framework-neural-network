from back.Register import Register
from back.Multiplier import Multiplier
from back.Adder import Adder

class MacUnit:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(MacUnit, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        self.accumulator = Register()
        self.multiplier = Multiplier()
        self.adder = Adder()
        self.output = None
        
        
        
    
    def step(self, entryA, entryB):
        self.multiplier.entryA = entryA
        self.multiplier.entryB = entryB
        self.multiplier.step()
        self.adder.entryA = self.accumulator.output
        self.adder.entryB = self.multiplier.result  
        self.adder.step()
        self.accumulator.entry = self.adder.result
        self.accumulator.step()
        self.output = self.accumulator.output
        