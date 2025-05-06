# Test Case Generator

This project, [test-case-generator](https://github.com/Erick-N-B-Araujo/test-case-generator), is a Python-based tool designed to automate test case generation, simplifying the creation of test plans and integration with automation tools.

## Features

- **Test Case Generation**: Automatically creates test cases based on user-defined variables.
- **Integration with TSA**: Supports direct test creation in Test Suite Automation (TSA) using an access token.
- **Documentation Generation**: Creates Word documents containing test cases for easy sharing and documentation.

## Project Structure

- **`testcase_generator.py`**: Main script that orchestrates test case generation, TSA integration, and Word document creation.
- **`src/test/variables.py`**: Manages variables used in test cases.
- **`src/test/tests.py`**: Includes the `TestPlan` and `TestCases` classes for creating test plans and test cases.
- **`src/document/json.py`**: Handles reading JSON files containing data required for test generation.
- **`src/automation/tsa.py`**: Manages integration with TSA, allowing automated test creation in the platform.
- **`src/document/word.py`**: Generates Word documents to document the created test cases.

## How to Use

1. **Configuration**: Edit the `data/test_data.json` file with your project details, including `team_id`, `genti_history_id`, `project_name`, `functionality_name`, and more.

2. **Execution**: Run the `testcase_generator.py` script to generate test cases, integrate them into TSA (if configured), and create a Word document.

   ```python
   python testcase_generator.py
   ```

3. **Output**: Test cases will be generated based on your configuration, integrated into TSA (if enabled), and a Word document will be created in the specified folder.

## Requirements

- Python 3.x
- Additional libraries listed in the `requirements.txt` file (if available).

------

## Contribution

Contributions are welcome! Feel free to open issues and pull requests to improve this project.

------

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.