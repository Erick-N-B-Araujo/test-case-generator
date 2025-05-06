from src.test.variable import Variable

class Variables:
    def __init__(self):
        self.variables = []

    def add_variable(self, key, value, var_type):
        variable = Variable(key, value, var_type)
        self.variables.append(variable)