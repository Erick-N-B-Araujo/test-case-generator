from src.test.variables import Variables
from src.test.tests import TestPlan
from src.test.tests import TestCases
from src.document.json import Json
from src.automation.tsa import TSA
from src.document.word import DocWord

path = "data/test_data.json"
test_data = Json(path).read_file()

team_id = test_data["team_id"]
team_name = ""
if team_id == 1:
    team_name = "Plataforma Parceiros"
elif team_id == 2:
    team_name = "Correspondente Bancário Transacional"

genti_history_id = test_data["genti_history_id"]
project_name = test_data["project_name"]
functionality_name = test_data["functionality_name"]
create_tests_in_tsa = test_data["create_tests_in_tsa"]
create_document_word = test_data["create_document_word"]
tsa_token = test_data["tsa_token"]
tsa_suite_id = test_data["tsa_suite_id"]
tsa_starting_scenario_id = test_data["tsa_starting_scenario_id"]
tsa_scenario_200_ref_id = test_data["tsa_scenario_200_ref_id"]
tsa_scenario_400_ref_id = test_data["tsa_scenario_400_ref_id"]
tsa_scenario_500_ref_id = test_data["tsa_scenario_500_ref_id"]
list_variables = test_data["variables"]
test_variables = Variables()

for variable in list_variables:
    test_variables.add_variable(variable["key"], variable["value"], variable["var_type"])

test_plan = TestPlan(team_name, project_name, functionality_name, genti_history_id)
test_cases = TestCases()

test_cases.create_test_cases(team_id, functionality_name, test_variables.variables)

if create_document_word == "True":
    word_document = DocWord(test_plan)
    word_document.set_placeholders()
    word_document.write_placeholders()
    word_document.create_testcases(test_cases)
    word_document.create_document()

if create_tests_in_tsa == "True":
    tsa = TSA(tsa_token, tsa_suite_id)
    tsa.create_tests_in_tsa(genti_history_id, tsa_starting_scenario_id, test_cases.test_cases_list, tsa_scenario_200_ref_id, tsa_scenario_400_ref_id, tsa_scenario_500_ref_id)
