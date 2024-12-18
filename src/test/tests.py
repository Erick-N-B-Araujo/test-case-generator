class TestPlan:
    def __init__(self, team_name, project_name, functionality_name, genti_history):
        self.team_name = team_name
        self.project_name = project_name
        self.functionality_name = functionality_name
        self.genti_history = genti_history

class TestCases:
    def __init__(self):
        self.test_cases_list = []

    def create_test_cases(self, team_id, functionality_name, variables):
        for variable in variables:
            null_test_case = TestCase(variable)
            null_test_case.create_title(500, functionality_name, "Field missing")
            null_test_case.create_steps(500, "Field missing")
            self.test_cases_list.append(null_test_case)

        if team_id == 1:
            for variable in variables:
                test_case_http_200 = TestCase(variable)
                test_case_http_200.create_title(200, functionality_name, "Decimal on integer field")
                test_case_http_200.create_steps(200, "Decimal on integer field")
                self.test_cases_list.append(test_case_http_200)
                test_case_http_400 = TestCase(variable)
                test_case_http_400.create_title(400, functionality_name, "Random text on string field")
                test_case_http_400.create_steps(400, "Random text on string field")
                self.test_cases_list.append(test_case_http_400)
                test_case_http_500 = TestCase(variable)
                test_case_http_500.create_title(500, functionality_name, "Nonexistent in database")
                test_case_http_500.create_steps(500, "Nonexistent in database")
                self.test_cases_list.append(test_case_http_500)

class TestCase:
    def __init__(self, variable):
        self.title = ""
        self.variable = variable
        self.steps = []

    def create_title(self, http_status, functionality_name, case_description):
        if http_status == 200 and case_description == "Decimal on integer field":
            self.title = f'[HTTP 200] Consultar a api de "{functionality_name}" passando o valor "{self.variable.value}.1" no campo "{self.variable.key}"'
        elif http_status == 400 and case_description == "Random text on string field":
            self.title = f'[HTTP 400] Consultar a api de "{functionality_name}" passando o valor "ABC" no campo "{self.variable.key}"'
        elif http_status == 500 and case_description == "Nonexistent in database":
            self.title = f'[HTTP 500] Consultar a api de "{functionality_name}" passando o valor "999" no campo "{self.variable.key}"'
        elif http_status == 500 and case_description == "Field missing":
            self.title = f'[HTTP 500] Consultar a api de "{functionality_name}" com o campo "{self.variable.key}" faltando'
        return self.title

    def create_steps(self, http_status, case_description):
        if http_status == 200 and case_description == "Decimal on integer field":
            self.steps = [
                'Dado que o usuário está autenticado na API de Login,',
                f'Quando Enviar a requisição com o valor “{self.variable.value}.1” no campo “{self.variable.key}”,',
                'Então a API deve aceitar a requisição e retornar o status HTTP 200.\n'
            ]
        elif http_status == 400 and case_description == "Random text on string field":
            self.steps = [
                'Dado que o usuário está autenticado na API de Login,',
                f'Quando Enviar a requisição com o valor “ABC” no campo “{self.variable.key}”,',
                'Então a API deve rejeitar a requisição e retornar o status HTTP 400.\n'
            ]
        elif http_status == 500 and case_description == "Nonexistent in database":
            self.steps = [
                'Dado que o usuário está autenticado na API de Login,',
                f'Quando Enviar a requisição com o valor “999” no campo “{self.variable.key}”,',
                'Então a API deve rejeitar a requisição e retornar o status HTTP 500.\n'
            ]
        elif http_status == 500 and case_description == "Field missing":
            self.steps = [
                'Dado que o usuário está autenticado na API de Login,',
                f'Quando Enviar a requisição com o campo “{self.variable.key}” faltando,',
                'Então a API deve rejeitar a requisição e retornar o status HTTP 500.\n'
            ]

    def __str__(self):
        return f'title: {self.title}, variable: {self.variable}, steps: {self.steps}'