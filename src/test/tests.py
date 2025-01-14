from src.document.json import Json


class TestPlan:
    def __init__(self, team_name, project_name, functionality_name, genti_history):
        self.team_name = team_name
        self.project_name = project_name
        self.functionality_name = functionality_name
        self.genti_history = genti_history

class TestCases:
    def __init__(self):
        self.test_cases_list = []
        self.has_codigo_convenio_gestor = False
        self.is_gestor_vision = False
        self.has_codigo_convenio_substabelecido_origem = False
        self.has_codigo_convenio_substabelecido = False
        self.is_substabelecido_vision = False
        self.has_codigo_loja_origem = False
        self.has_codigo_loja = False
        self.is_loja_vision = False
        self.conditions_count = 0

    def create_test_case(self, http_status, functionality_name, case_description, *args):
        if len(args) > 0:
            variable = args[0]
        else:
            variable = None
        test_case = TestCase(variable)
        test_case.create_test(http_status, functionality_name, case_description, variable)
        self.test_cases_list.append(test_case)

    def create_substabelecido_vision_test_cases(self, functionality_name):
        path = "data/visao_substabelecido.json"
        test_cases_data = Json(path).read_file()
        for test_case_data in test_cases_data:
            if test_case_data["http"] == 200:
                self.create_test_case(200, functionality_name, "Substabelecido vision", test_case_data)
            elif test_case_data["http"] == 422:
                self.create_test_case(422, functionality_name, "Substabelecido vision", test_case_data)
        self.is_substabelecido_vision = False

    def create_loja_vision_test_cases(self, functionality_name):
        path = "data/visao_loja.json"
        test_cases_data = Json(path).read_file()
        for test_case_data in test_cases_data:
            if test_case_data["http"] == 200:
                self.create_test_case(200, functionality_name, "Loja vision", test_case_data)
            elif test_case_data["http"] == 422:
                self.create_test_case(422, functionality_name, "Loja vision", test_case_data)
        self.is_loja_vision = False

    def create_test_cases(self, team_id, functionality_name, variables):
        self.create_test_case(200, functionality_name, "Valid values")
        if team_id == 1:
            for variable in variables:
                self.create_test_case(422, functionality_name, "Field missing", variable)
                if variable.var_type == "integer":
                    self.create_test_case(200, functionality_name, "Decimal on integer field", variable)
                    self.create_test_case(400, functionality_name, "Random text on string field", variable)
                    self.create_test_case(500, functionality_name, "Nonexistent in database", variable)
                elif variable.var_type == "string":
                    self.create_test_case(500, functionality_name, "Random text on string field", variable)

        elif team_id == 2:
            self.create_test_case(400, functionality_name, "Missing header authorization")
            self.create_test_case(400, functionality_name, "Missing signed certificate")
            self.create_test_case(401, functionality_name, "Invalid token in header authorization")
            self.create_test_case(401, functionality_name, "Expired token in header authorization")
            self.create_test_case(403, functionality_name, "Missing parameter gw-dev-app-key")
            self.create_test_case(403, functionality_name, "31 characters in parameter gw-dev-app-key")
            self.create_test_case(403, functionality_name, "33 characters in parameter gw-dev-app-key")
            self.create_test_case(403, functionality_name, "32 numbers in parameter gw-dev-app-key")
            self.create_test_case(403, functionality_name, "Empty in parameter gw-dev-app-key")

            for variable in variables:

                if variable.var_type == "integer":
                    self.create_test_case(422, functionality_name, "Size limit minus one", variable)
                    self.create_test_case(422, functionality_name, "Size limit plus one", variable)
                    self.create_test_case(422, functionality_name, "Nonexistent in database", variable)
                    self.create_test_case(422, functionality_name, "Negative value", variable)
                    self.create_test_case(500, functionality_name, "Random text in number field", variable)
                    self.create_test_case(500, functionality_name, "Numbers with spaces", variable)
                    self.create_test_case(500, functionality_name, "Decimal on integer field", variable)
                    self.create_test_case(500, functionality_name, "Empty", variable)

                elif variable.var_type == "string":
                    self.create_test_case(500, functionality_name, "Random text on string field", variable)

                elif variable.var_type == "float":
                    self.create_test_case(200, functionality_name, "One decimal", variable)
                    self.create_test_case(422, functionality_name, "Negative value", variable)
                    self.create_test_case(500, functionality_name, "Three decimal", variable)
                    self.create_test_case(500, functionality_name, "Random text in number field", variable)
                    self.create_test_case(500, functionality_name, "Numbers with spaces", variable)
                    self.create_test_case(500, functionality_name, "Empty", variable)

                if variable.key == "codigoConvenioGestor":
                    self.has_codigo_convenio_gestor = True
                    self.conditions_count += 1
                elif variable.key == "codigoConvenioSubstabelecidoOrigem":
                    self.has_codigo_convenio_substabelecido_origem = True
                    self.conditions_count += 1
                elif variable.key == "codigoConvenioSubstabelecido":
                    self.has_codigo_convenio_substabelecido = True
                    self.conditions_count += 1
                elif variable.key == "codigoLojaOrigem":
                    self.has_codigo_loja_origem = True
                    self.conditions_count += 1
                elif variable.key == "codigoLoja":
                    self.has_codigo_loja = True
                    self.conditions_count += 1

                if self.has_codigo_convenio_gestor and self.has_codigo_convenio_substabelecido_origem and self.has_codigo_convenio_substabelecido and self.conditions_count == 3:
                    self.is_gestor_vision = True
                if self.has_codigo_convenio_substabelecido_origem and self.has_codigo_convenio_substabelecido and self.conditions_count == 2:
                    self.is_substabelecido_vision = True
                if self.has_codigo_loja_origem or self.has_codigo_loja:
                    self.is_loja_vision = True

            if self.is_gestor_vision:
                pass
            elif self.is_substabelecido_vision:
                self.create_substabelecido_vision_test_cases(functionality_name)
            if self.is_loja_vision:
                self.create_loja_vision_test_cases(functionality_name)

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
                    f'   mciAutenticado: {test_data["mci"]}',
                    f'   codigoConvenioSubstabelecidoOrigem: {test_data["substabelecidoOrigem"]}',
                    f'   codigoConvenioSubstabelecido: {test_data["substabelecido"]}',
                    f'   codigoLoja: {test_data["loja"]}',
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
                    f'   mciAutenticado: {test_data["mci"]}',
                    f'   codigoConvenioSubstabelecidoOrigem: {test_data["substabelecidoOrigem"]}',
                    f'   codigoConvenioSubstabelecido: {test_data["substabelecido"]}',
                    f'   codigoLoja: {test_data["loja"]}',
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

    def __str__(self):
        return f'title: {self.title}, variable: {self.variable}, steps: {self.steps}'