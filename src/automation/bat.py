import subprocess
import json
import os

class RequestClone:

    def __init__(self, token, suite_id, scenario_id):
        self.bat_path = os.path.join(os.path.dirname(__file__), "clone_request.bat")
        self.token = token
        self.suite_id = suite_id
        self.scenario_id = scenario_id

    def send_request_to_clone(self):
        cmd = [self.bat_path, self.token, self.suite_id, self.scenario_id]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True, shell=True)
            output = result.stdout.strip()
            json_response = json.loads(output)
            print(f"Clone ID: {json_response['id']}")
            return json_response['id']
        except subprocess.CalledProcessError as e:
            print(f"Erro ao executar o .bat")
            print(f"Comando: {e.cmd}")
            print(f"Comando: {e.returncode}")
            print(f"Comando: {e.stderr}")

class UpdateClone:
    def __init__(self, token, suite_id, scenario_id):
        self.bat_path = os.path.join(os.path.dirname(__file__), "update_clone_request.bat")
        self.token = token
        self.suite_id = suite_id
        self.scenario_id = scenario_id

    def send_request_to_update_test(self, test_id, title, genti_history_id):
        cmd_update = [self.bat_path, self.token, self.suite_id, self.scenario_id, str(test_id), title, str(genti_history_id)]
        try:
            result = subprocess.run(cmd_update, capture_output=True, text=True, check=True, shell=True)
            output = result.stdout.strip()
            print(output)
        except subprocess.CalledProcessError as e:
            print(f"Erro ao executar o .bat")
            print(f"Comando: {e.cmd}")
            print(f"Comando: {e.returncode}")
            print(f"Comando: {e.stderr}")