from docx import Document
from abc import ABC
from datetime import datetime

date = datetime.now()
date_formated = date.strftime("%d/%m/%Y")
arquivo_referencia = "references/testplan.docx"
doc = Document(arquivo_referencia)

class DocWord:
    def __init__(self, test_plan):
        self.test_plan = test_plan
        self.test_cases = 1

    def set_placeholders(self):
        test_plan_data = {
            "[TEAM_NAME]": f'{self.test_plan.team_name}',
            "[PROJECT_NAME]": f'{self.test_plan.project_name}',
            "[FUNCTIONALITY_NAME]": f'{self.test_plan.functionality_name}',
            "[GENTI_HISTORY]": f'{self.test_plan.genti_history}',
            "[DATE]": f'{date_formated}'
        }
        return test_plan_data

    def write_placeholders(self, test_plan_data):
        for paragraph in doc.paragraphs:
            for placeholder, valor in test_plan_data.items():
                if placeholder in paragraph.text:
                    paragraph.text = paragraph.text.replace(placeholder, valor)

    def assembly_testcase(self, team_choosed, http_status, functionality_name, test_steps):
        doc.add_paragraph(
            f"{self.test_cases}- {test_steps.create_title(team_choosed, http_status, functionality_name)}",
            style='List Paragraph')
        if team_choosed == 1 and http_status == 200:
            self.write_test_steps(test_steps.create_http_200_steps_decimal())
        elif team_choosed == 1 and http_status == 400:
            self.write_test_steps(test_steps.create_http_400_steps_string())
        elif team_choosed == 1 and http_status == 500:
            self.write_test_steps(test_steps.create_http_500_steps_not_found_in_database())
        elif team_choosed == 1 and http_status == 501:
            self.write_test_steps(test_steps.create_http_501_steps_null_field())

    def write_test_steps(self, steps):
        for step in steps:
            doc.add_paragraph(step, style='List Paragraph')
        self.test_cases += 1

    def create_testcases(self, team_choosed, functionality_name, test_steps, variable_type):
        if team_choosed == 1 and variable_type == 'integer':
            self.assembly_testcase(team_choosed, 501, functionality_name, test_steps)
            self.assembly_testcase(team_choosed, 200, functionality_name, test_steps)
            self.assembly_testcase(team_choosed, 400, functionality_name, test_steps)
            self.assembly_testcase(team_choosed, 500, functionality_name, test_steps)
        elif team_choosed == 1 and variable_type == 'string':
            self.assembly_testcase(team_choosed, 501, functionality_name, test_steps)
            self.assembly_testcase(team_choosed, 400, functionality_name, test_steps)
