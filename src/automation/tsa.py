import requests

class TSA:
    def __init__(self, token, suite_id):
        self.token = token
        self.url = "https://testesuaapi.ftabb.intranet.bb.com.br/api"
        self.suite_id = suite_id
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        self.cookies = {}
        self.payload = {}

    def clone_testcase_request(self, scenario_id):
        url_to_clone = f'{self.url}/cenarios/{scenario_id}/clonar/{self.suite_id}'
        response_cloned_testcase = requests.post(url_to_clone, headers=self.headers, cookies=self.cookies, json=self.payload)
        json_body = response_cloned_testcase.json()
        return json_body['id']

    def update_testcase_request(self, cloned_testcase_id, test_id,title, genti_history_id):
        url_to_update = f'{self.url}/cenarios/{cloned_testcase_id}'
        payload = {
            "suiteId": f"{self.suite_id}",
            "nome": f"CT{test_id} - {title}",
            "historiaALM": f"{genti_history_id}",
            "tipoArtefato": "GENTI"
        }
        response_updated_testcase = requests.patch(url_to_update, headers=self.headers, cookies=self.cookies, json=payload)
        return response_updated_testcase

    def create_test(self, scenario_id, test_id,title, genti_history_id):
        cloned_testcase_id = self.clone_testcase_request(scenario_id)
        self.update_testcase_request(cloned_testcase_id, test_id, title, genti_history_id)

    def create_tests_in_tsa(self, genti_history_id, tsa_starting_scenario_id, test_cases, scenario_200_ref_id, scenario_400_ref_id, scenario_500_ref_id):
        try:
            id_count = tsa_starting_scenario_id
            print("Starting tests creation in TSA...")
            for test_case in test_cases:
                if "HTTP 200" in test_case.title:
                    self.create_test(scenario_200_ref_id, id_count, test_case.title, genti_history_id)
                    id_count+=1
                elif "HTTP 400" in test_case.title:
                    self.create_test(scenario_400_ref_id, id_count, test_case.title, genti_history_id)
                    id_count += 1
                elif "HTTP 500" in test_case.title:
                    self.create_test(scenario_500_ref_id, id_count, test_case.title, genti_history_id)
                    id_count += 1

        except requests.RequestException as e:
            print("Error sending the request:", e)

        print("Finished tests creation in TSA!")