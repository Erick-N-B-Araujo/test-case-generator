class Steps:
    def __init__(self, variable):
        self.variable = variable

    def create_steps(self, http_status, case_description):
        steps = []
        if http_status == 200 and case_description == "Decimal on integer field":
            steps = [
                'Dado que o usuário está autenticado na API de Login,',
                f'Quando Enviar a requisição com o valor “{self.variable.value}.1” no campo “{self.variable.key}”,',
                'Então a API deve aceitar a requisição e retornar o status HTTP 200.\n'
            ]
        elif http_status == 400 and case_description == "Random text on string field":
            steps = [
                'Dado que o usuário está autenticado na API de Login,',
                f'Quando Enviar a requisição com o valor “ABC” no campo “{self.variable.key}”,',
                'Então a API deve rejeitar a requisição e retornar o status HTTP 400.\n'
            ]
        elif http_status == 500 and case_description == "Nonexistent in database":
            steps = [
                'Dado que o usuário está autenticado na API de Login,',
                f'Quando Enviar a requisição com o valor “999” no campo “{self.variable.key}”,',
                'Então a API deve rejeitar a requisição e retornar o status HTTP 500.\n'
            ]
        elif http_status == 500 and case_description == "Field missing":
            steps = [
                'Dado que o usuário está autenticado na API de Login,',
                f'Quando Enviar a requisição com o campo “{self.variable.key}” faltando,',
                'Então a API deve rejeitar a requisição e retornar o status HTTP 500.\n'
            ]
        return steps