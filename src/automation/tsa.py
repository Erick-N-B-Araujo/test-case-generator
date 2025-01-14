from src.automation.bat import RequestClone
from src.automation.bat import UpdateClone

class TSA:
    def __init__(self, token, suite_id):
        self.token = token
        self.suite_id = suite_id
        self.payload = {}

    def clone_testcase_request(self, scenario_id):
        cloned_test_id = RequestClone(self.token, self.suite_id, scenario_id).send_request_to_clone()
        return cloned_test_id

    def update_testcase_request(self, cloned_testcase_id, test_id, title, genti_history_id):
        updated_test = UpdateClone(self.token, self.suite_id, cloned_testcase_id)
        updated_test.send_request_to_update_test(test_id, title, genti_history_id)
        return updated_test

    def create_test(self, scenario_id, test_id,title, genti_history_id):
        cloned_testcase_id = self.clone_testcase_request(scenario_id)
        self.update_testcase_request(cloned_testcase_id, test_id, title, genti_history_id)

    def create_tests_in_tsa(self, genti_history_id, tsa_starting_scenario_id, test_cases, scenario_200_ref_id, scenario_400_ref_id, scenario_500_ref_id):
        id_count = tsa_starting_scenario_id
        print("Starting tests creation in TSA...")
        for test_case in test_cases:
            if "HTTP 200" in test_case.title:
                self.create_test(scenario_200_ref_id, id_count, test_case.title, genti_history_id)
                id_count += 1
            elif "HTTP 400" in test_case.title or "HTTP 401" in test_case.title or "HTTP 403" in test_case.title or "HTTP 422" in test_case.title:
                self.create_test(scenario_400_ref_id, id_count, test_case.title, genti_history_id)
                id_count += 1
            elif "HTTP 500" in test_case.title:
                self.create_test(scenario_500_ref_id, id_count, test_case.title, genti_history_id)
                id_count += 1

        print("Finished tests creation in TSA!")