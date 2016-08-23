class calculator:

    def __init__(self, ina, inb):
        self.a = ina
        self.b = inb

    def add(self):
        return self.a + self.b

    def multiply(self):
        return self.a*self.b

    def div(self):
        return  self.a/self.b

class power_of_calculator(calculator):

    def power(self):
        return pow(self.a, self.b)
