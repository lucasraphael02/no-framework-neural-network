class Register:
    
    def __init__(self, entry=0):
        self.entry = entry
        self.output = None

    def step(self):
        self.output = self.entry