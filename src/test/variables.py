class Variable:
    def __init__(self, key, value, var_type):
        self.key = key
        self.value = value
        self.var_type = var_type

    def __str__(self):
        return f'key: {self.key}, value: {self.value}, var_type: {self.var_type}'

class Variables:
    def __init__(self):
        self.variables = []

    def add_variable(self, key, value, var_type):
        variable = Variable(key, value, var_type)
        self.variables.append(variable)