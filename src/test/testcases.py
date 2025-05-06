from src.document.json import Json
from src.test.testcase import TestCase
class TestCases:
    def __init__(self):
        self.test_cases_list = []

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

    def create_loja_vision_test_cases(self, functionality_name):
        path = "data/visao_loja.json"
        test_cases_data = Json(path).read_file()
        for test_case_data in test_cases_data:
            if test_case_data["http"] == 200:
                self.create_test_case(200, functionality_name, "Loja vision", test_case_data)
            elif test_case_data["http"] == 422:
                self.create_test_case(422, functionality_name, "Loja vision", test_case_data)

    def create_json_test_cases(self, functionality_name, path, validation):
        test_cases_data = Json(path).read_file()
        for test_case_data in test_cases_data:
            if test_case_data["httpStatus"] == 200:
                self.create_test_case(200, functionality_name, validation, test_case_data)
            elif test_case_data["httpStatus"] == 422:
                self.create_test_case(422, functionality_name, validation, test_case_data)

    def create_test_cases(self, functionality_name, variables, http_method, validation):
        self.create_test_case(200, functionality_name, "Valid values")
        if http_method == "GET":
            pass
        elif http_method == "POST":
            for variable in variables:
                self.create_test_case(422, functionality_name, "Null field", variable)

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

            self.create_test_case(422, functionality_name, "Field missing", variable)

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

            elif variable.var_type == "object":
                self.create_test_case(500, functionality_name, "Empty", variable)

        if validation == "visao gestor simples":
            self.create_json_test_cases(functionality_name, "data/validation/visao_gestor_simples.json", validation)
        elif validation == "visao gestor":
            self.create_json_test_cases(functionality_name, "data/validation/visao_gestor_simples.json", validation)
        elif validation == "visao substabelecido simples":
            self.create_json_test_cases(functionality_name, "data/validation/visao_substabelecido_simples.json", validation)
        elif validation == "visao substabelecido":
            self.create_json_test_cases(functionality_name, "data/validation/visao_substabelecido.json", validation)
        elif validation == "visao loja simples":
            self.create_json_test_cases(functionality_name, "data/validation/visao_loja_simples.json", validation)
        elif validation == "visao loja":
            self.create_json_test_cases(functionality_name, "data/validation/visao_loja.json", validation)

