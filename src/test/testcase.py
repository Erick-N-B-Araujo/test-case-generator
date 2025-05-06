class TestCase:
    def __init__(self, *args):
        self.title = ""
        self.steps = []
        if len(args) > 0:
            self.variable = args[0]
        else:
            self.variable = None

    def create_test(self, http_status, functionality_name, case_description, *args):
        if len(args) > 0:
            test_data = args[0]
        else:
            test_data = None
        if http_status == 200 and case_description == "Valid values":
            self.title = f'[HTTP 200] Consultar a api de {functionality_name} passando valores válidos'
            self.steps = [
                'Dado que o usuário está autenticado na API de Login,',
                f'Quando enviar a requisição com valores válidos,',
                'Então a API deve aceitar a requisição e retornar o status HTTP 200.\n'
            ]
        elif http_status == 200 and case_description == "One decimal":
            self.title = f'[HTTP 200] Consultar a api de {functionality_name} passando o valor {self.variable.value}.0 no campo {self.variable.key}'
            self.steps = [
                'Dado que o usuário está autenticado na API de Login,',
                f'Quando enviar a requisição com o valor “{self.variable.value}.0” no campo “{self.variable.key}”,',
                'Então a API deve aceitar a requisição e retornar o status HTTP 200.\n'
            ]
        elif http_status == 200 and case_description == "Decimal on integer field":
            self.title = f'[HTTP 200] Consultar a api de {functionality_name} passando o valor {self.variable.value}.1 no campo {self.variable.key}'
            self.steps = [
                'Dado que o usuário está autenticado na API de Login,',
                f'Quando enviar a requisição com o valor “{self.variable.value}.1” no campo “{self.variable.key}”,',
                'Então a API deve aceitar a requisição e retornar o status HTTP 200.\n'
            ]
        elif http_status == 200 and case_description == "Substabelecido vision":
            if test_data != None:
                self.title = f'[HTTP 200] Consultar a api de {functionality_name} com um {test_data["type"]}'
                self.steps = [
                    'Dado que o usuário está autenticado na API de Login,',
                    'Quando enviar a requisição com os valores:',
                    f'   mciAutenticado: {test_data["mci"]}',
                    f'   codigoConvenioSubstabelecidoOrigem: {test_data["substabelecidoOrigem"]}',
                    f'   codigoConvenioSubstabelecido: {test_data["substabelecido"]}',
                    'Então a API deve aceitar a requisição e retornar o status HTTP 200.\n'
                ]
        elif http_status == 200 and case_description == "Loja vision":
            if test_data != None:
                self.title = f'[HTTP 200] Consultar a api de {functionality_name} com um {test_data["type"]}'
                self.steps = [
                    'Dado que o usuário está autenticado na API de Login,',
                    'Quando enviar a requisição com os valores:',
                    f'   codigoCorrespondenteAutenticado: {test_data["mci"]}',
                    f'   codigoConvenioSubstabelecidoOrigem: {test_data["substabelecidoOrigem"]}',
                    f'   codigoConvenioSubstabelecido: {test_data["substabelecido"]}',
                    f'   codigoLoja: {test_data["loja"]}',
                    'Então a API deve aceitar a requisição e retornar o status HTTP 200.\n'
                ]
        elif http_status == 200 and case_description == "visao loja simples":
            if test_data != None:
                self.title = f'[HTTP 200] Consultar a api de {functionality_name} com um {test_data["type"]}'
                self.steps = [
                    'Dado que o usuário está autenticado na API de Login,',
                    'Quando enviar a requisição com os valores:',
                    f'   codigoCorrespondenteAutenticado: {test_data["mci"]}',
                    f'   codigoConvenioSubstabelecidoOrigem: {test_data["codigoConvenioSubstabelecidoOrigem"]}',
                    f'   codigoLojaOrigem: {test_data["codigoLojaOrigem"]}',
                    'Então a API deve aceitar a requisição e retornar o status HTTP 200.\n'
                ]
        elif http_status == 400 and case_description == "Random text on string field":
            self.title = f'[HTTP 400] Consultar a api de {functionality_name} passando o valor ABC no campo {self.variable.key}'
            self.steps = [
                'Dado que o usuário está autenticado na API de Login,',
                f'Quando enviar a requisição com o valor “ABC” no campo “{self.variable.key}”,',
                'Então a API deve rejeitar a requisição e retornar o status HTTP 400.\n'
            ]
        elif http_status == 400 and case_description == "Missing header authorization":
            self.title = f'[HTTP 400] Consultar a api de {functionality_name} sem o header Authorization'
            self.steps = [
                'Dado que o usuário está autenticado na API de Login,',
                f'Quando enviar a requisição sem o header Authorization,',
                'Então a API deve rejeitar a requisição e retornar o status HTTP 400.\n'
            ]
        elif http_status == 400 and case_description == "Missing signed certificate":
            self.title = f'[HTTP 400] Consultar a api de {functionality_name} sem o certificado assinado'
            self.steps = [
                'Dado que o usuário está autenticado na API de Login,',
                f'Quando enviar a requisição sem o certificado assinado,',
                'Então a API deve rejeitar a requisição e retornar o status HTTP 400.\n'
            ]
        elif http_status == 401 and case_description == "Invalid token in header authorization":
            self.title = f'[HTTP 401] Consultar a api de {functionality_name} passando invalid_token no header authorization'
            self.steps = [
                'Dado que o usuário está autenticado na API de Login,',
                f'Quando enviar a requisição passando "invalid_token" no header authorization,',
                'Então a API deve rejeitar a requisição e retornar o status HTTP 401.\n'
            ]
        elif http_status == 401 and case_description == "Expired token in header authorization":
            self.title = f'[HTTP 401] Consultar a api de {functionality_name} passando um token expirado no header authorization'
            self.steps = [
                'Dado que o usuário está autenticado na API de Login,',
                f'Quando enviar a requisição passando um token expirado no header authorization,',
                'Então a API deve rejeitar a requisição e retornar o status HTTP 401.\n'
            ]
        elif http_status == 403 and case_description == "Missing parameter gw-dev-app-key":
            self.title = f'[HTTP 403] Consultar a api de {functionality_name} sem o campo gw-dev-app-key'
            self.steps = [
                'Dado que o usuário está autenticado na API de Login,',
                f'Quando enviar a requisição sem o campo "gw-dev-app-key",',
                'Então a API deve rejeitar a requisição e retornar o status HTTP 403.\n'
            ]
        elif http_status == 403 and case_description == "31 characters in parameter gw-dev-app-key":
            self.title = f'[HTTP 403] Consultar a api de {functionality_name} um valor com 31 caracteres no campo gw-dev-app-key'
            self.steps = [
                'Dado que o usuário está autenticado na API de Login,',
                f'Quando enviar a requisição passando "G7XjM8Y2Vkq94LRoBzWtNc1phd5FA3T" no campo "gw-dev-app-key",',
                'Então a API deve rejeitar a requisição e retornar o status HTTP 403.\n'
            ]
        elif http_status == 403 and case_description == "33 characters in parameter gw-dev-app-key":
            self.title = f'[HTTP 403] Consultar a api de {functionality_name} um valor com 33 caracteres no campo gw-dev-app-key'
            self.steps = [
                'Dado que o usuário está autenticado na API de Login,',
                f'Quando enviar a requisição passando "G7XjM8Y2Vkq94LRoBzWtNc1phd5FA3TTT" no campo "gw-dev-app-key",',
                'Então a API deve rejeitar a requisição e retornar o status HTTP 403.\n'
            ]
        elif http_status == 403 and case_description == "32 numbers in parameter gw-dev-app-key":
            self.title = f'[HTTP 403] Consultar a api de {functionality_name} um valor com 32 números no campo gw-dev-app-key'
            self.steps = [
                'Dado que o usuário está autenticado na API de Login,',
                f'Quando enviar a requisição passando "11111111111111111111111111111111" no campo "gw-dev-app-key",',
                'Então a API deve rejeitar a requisição e retornar o status HTTP 403.\n'
            ]
        elif http_status == 403 and case_description == "Empty in parameter gw-dev-app-key":
            self.title = f'[HTTP 403] Consultar a api de {functionality_name} passando aspas no campo gw-dev-app-key'
            self.steps = [
                'Dado que o usuário está autenticado na API de Login,',
                f'Quando enviar a requisição passando "" no campo "gw-dev-app-key",',
                'Então a API deve rejeitar a requisição e retornar o status HTTP 403.\n'
            ]
        elif http_status == 422 and case_description == "Field missing":
            self.title = f'[HTTP 422] Consultar a api de {functionality_name} com o campo {self.variable.key} faltando'
            self.steps = [
                'Dado que o usuário está autenticado na API de Login,',
                f'Quando enviar a requisição com o campo “{self.variable.key}” faltando,',
                'Então a API deve rejeitar a requisição e retornar o status HTTP 422.\n'
            ]
        elif http_status == 422 and case_description == "Size limit minus one":
            var_length = len(str(self.variable.value))
            var_length -= 1
            self.title = f'[HTTP 422] Consultar a api de {functionality_name} passando um valor com {var_length} caracteres no campo {self.variable.key}'
            self.steps = [
                'Dado que o usuário está autenticado na API de Login,',
                f'Quando enviar a requisição passando um valor com "{var_length}" caracteres no campo “{self.variable.key}”,',
                'Então a API deve rejeitar a requisição e retornar o status HTTP 422.\n'
            ]
        elif http_status == 422 and case_description == "Size limit plus one":
            var_length = len(str(self.variable.value))
            var_length += 1
            self.title = f'[HTTP 422] Consultar a api de {functionality_name} passando um valor com {var_length} caracteres no campo {self.variable.key}'
            self.steps = [
                'Dado que o usuário está autenticado na API de Login,',
                f'Quando enviar a requisição passando um valor com "{var_length}" caracteres no campo “{self.variable.key}”,',
                'Então a API deve rejeitar a requisição e retornar o status HTTP 422.\n'
            ]
        elif http_status == 422 and case_description == "Nonexistent in database":
            self.title = f'[HTTP 422] Consultar a api de {functionality_name} passando um valor inexistente no campo {self.variable.key}'
            self.steps = [
                'Dado que o usuário está autenticado na API de Login,',
                f'Quando enviar a requisição passando o valor "999" no campo “{self.variable.key}”,',
                'Então a API deve rejeitar a requisição e retornar o status HTTP 422.\n'
            ]
        elif http_status == 422 and case_description == "Negative value":
            self.title = f'[HTTP 422] Consultar a api de {functionality_name} passando um valor negativo no campo {self.variable.key}'
            self.steps = [
                'Dado que o usuário está autenticado na API de Login,',
                f'Quando enviar a requisição passando o valor "-{self.variable.value}" no campo “{self.variable.key}”,',
                'Então a API deve rejeitar a requisição e retornar o status HTTP 422.\n'
            ]
        elif http_status == 422 and case_description == "Substabelecido vision":
            if test_data != None:
                self.title = f'[HTTP 422] Consultar a api de {functionality_name} com um {test_data["type"]}'
                self.steps = [
                    'Dado que o usuário está autenticado na API de Login,',
                    'Quando enviar a requisição com os valores:',
                    f'   mciAutenticado: {test_data["mci"]}',
                    f'   codigoConvenioSubstabelecidoOrigem: {test_data["substabelecidoOrigem"]}',
                    f'   codigoConvenioSubstabelecido: {test_data["substabelecido"]}',
                    'Então a API deve rejeitar a requisição e retornar o status HTTP 422.\n'
                ]
        elif http_status == 422 and case_description == "Loja vision":
            if test_data != None:
                self.title = f'[HTTP 422] Consultar a api de {functionality_name} com um {test_data["type"]}'
                self.steps = [
                    'Dado que o usuário está autenticado na API de Login,',
                    'Quando enviar a requisição com os valores:',
                    f'   codigoCorrespondenteAutenticado: {test_data["mci"]}',
                    f'   codigoConvenioSubstabelecidoOrigem: {test_data["substabelecidoOrigem"]}',
                    f'   codigoConvenioSubstabelecido: {test_data["substabelecido"]}',
                    f'   codigoLoja: {test_data["loja"]}',
                    'Então a API deve rejeitar a requisição e retornar o status HTTP 422.\n'
                ]
        elif http_status == 422 and case_description == "visao loja simples":
            if test_data != None:
                self.title = f'[HTTP 422] Consultar a api de {functionality_name} com um {test_data["type"]}'
                self.steps = [
                    'Dado que o usuário está autenticado na API de Login,',
                    'Quando enviar a requisição com os valores:',
                    f'   codigoCorrespondenteAutenticado: {test_data["mci"]}',
                    f'   codigoConvenioSubstabelecidoOrigem: {test_data["codigoConvenioSubstabelecidoOrigem"]}',
                    f'   codigoLojaOrigem: {test_data["codigoLojaOrigem"]}',
                    'Então a API deve rejeitar a requisição e retornar o status HTTP 422.\n'
                ]
        elif http_status == 500 and case_description == "Three decimal":
            self.title = f'[HTTP 500] Consultar a api de {functionality_name} passando o valor {self.variable.value}.000 no campo {self.variable.key}'
            self.steps = [
                'Dado que o usuário está autenticado na API de Login,',
                f'Quando enviar a requisição com o valor “{self.variable.value}.000” no campo “{self.variable.key}”,',
                'Então a API deve rejeitar a requisição e retornar o status HTTP 500.\n'
            ]
        elif http_status == 500 and case_description == "Random text on string field":
            self.title = f'[HTTP 500] Consultar a api de {functionality_name} passando o valor ABC no campo {self.variable.key}'
            self.steps = [
                'Dado que o usuário está autenticado na API de Login,',
                f'Quando enviar a requisição com o valor “ABC” no campo “{self.variable.key}”,',
                'Então a API deve rejeitar a requisição e retornar o status HTTP 500.\n'
            ]
        elif http_status == 500 and case_description == "Nonexistent in database":
            self.title = f'[HTTP 500] Consultar a api de {functionality_name} passando o valor 999 no campo {self.variable.key}'
            self.steps = [
                'Dado que o usuário está autenticado na API de Login,',
                f'Quando enviar a requisição com o valor “999” no campo “{self.variable.key}”,',
                'Então a API deve rejeitar a requisição e retornar o status HTTP 500.\n'
            ]
        elif http_status == 500 and case_description == "Field missing":
            self.title = f'[HTTP 500] Consultar a api de {functionality_name} com o campo {self.variable.key} faltando'
            self.steps = [
                'Dado que o usuário está autenticado na API de Login,',
                f'Quando enviar a requisição com o campo “{self.variable.key}” faltando,',
                'Então a API deve rejeitar a requisição e retornar o status HTTP 500.\n'
            ]
        elif http_status == 500 and case_description == "Random text in number field":
            self.title = f'[HTTP 500] Consultar a api de {functionality_name} passando valor de ABC no campo {self.variable.key} faltando'
            self.steps = [
                'Dado que o usuário está autenticado na API de Login,',
                f'Quando enviar a requisição passando valor de "ABC" no campo “{self.variable.key}”,',
                'Então a API deve rejeitar a requisição e retornar o status HTTP 500.\n'
            ]
        elif http_status == 500 and case_description == "Numbers with spaces":
            number_with_spaces = ' '.join(str(self.variable.value))
            self.title = f'[HTTP 500] Consultar a api de {functionality_name} passando o valor com espaços {number_with_spaces} no campo {self.variable.key}'
            self.steps = [
                'Dado que o usuário está autenticado na API de Login,',
                f'Quando enviar a requisição passando o valor "{number_with_spaces}" no campo “{self.variable.key}”,',
                'Então a API deve rejeitar a requisição e retornar o status HTTP 500.\n'
            ]
        elif http_status == 500 and case_description == "Decimal on integer field":
            self.title = f'[HTTP 500] Consultar a api de {functionality_name} passando o valor {self.variable.value}.1 no campo {self.variable.key}'
            self.steps = [
                'Dado que o usuário está autenticado na API de Login,',
                f'Quando enviar a requisição passando o valor "{self.variable.value}.1" no campo “{self.variable.key}”,',
                'Então a API deve rejeitar a requisição e retornar o status HTTP 500.\n'
            ]
        elif http_status == 500 and case_description == "Empty":
            self.title = f'[HTTP 500] Consultar a api de {functionality_name} passando aspas no campo {self.variable.key}'
            self.steps = [
                'Dado que o usuário está autenticado na API de Login,',
                f'Quando enviar a requisição passando o valor "" no campo “{self.variable.key}”,',
                'Então a API deve rejeitar a requisição e retornar o status HTTP 500.\n'
            ]
        elif http_status == 422 and case_description == "Null field":
            self.title = f'[HTTP 422] Consultar a api de {functionality_name} passando NULL no campo {self.variable.key}'
            self.steps = [
                'Dado que o usuário está autenticado na API de Login,',
                f'Quando enviar a requisição passando o valor NULL no campo “{self.variable.key}”,',
                'Então a API deve rejeitar a requisição e retornar o status HTTP 422.\n'
            ]

    def __str__(self):
        return f'title: {self.title}, variable: {self.variable}, steps: {self.steps}'