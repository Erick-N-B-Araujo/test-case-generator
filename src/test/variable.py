class Variable:
    def __init__(self, key, value, var_type):
        self.key = key
        self.value = value
        self.var_type = var_type

    def __str__(self):
        return f'key: {self.key}, value: {self.value}, var_type: {self.var_type}'