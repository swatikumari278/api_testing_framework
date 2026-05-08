Use this for your API automation framework README:

````md id="m0ndt5"
# Pytest REST API Automation Framework

A scalable REST API automation framework built using Python, pytest, and requests library.

This framework is designed for validating REST APIs with reusable utilities, request handling, response validation, reporting, and CI/CD integration.

---

# Tech Stack

- Python
- pytest
- requests
- Allure Reports
- GitHub Actions
- Jenkins

---

# Framework Features

- REST API automation using pytest
- Reusable request handling utilities
- Response validation and assertions
- JSON schema validation
- Configurable environments
- Logging and reporting support
- API test data management
- CI/CD integration support
- Scalable framework structure

---

# Framework Structure

```bash
api_testing_framework/
│
├── tests/
├── utilities/
├── config/
├── testdata/
├── reports/
├── conftest.py
├── requirements.txt
└── pytest.ini
````

---

# Supported Validations

* Status code validation
* Response body validation
* Schema validation
* Header validation
* Authentication validation
* Negative API testing
* Data-driven API testing

---

# Installation

```bash
git clone https://github.com/swatikumari278/api_testing_framework.git
cd api_testing_framework
pip install -r requirements.txt
```

---

# Run Tests

Run all tests:

```bash
pytest
```

Run with verbose logs:

```bash
pytest -v
```

Generate Allure Report:

```bash
pytest --alluredir=reports
allure serve reports
```

---

# CI/CD Integration

The framework supports:

* GitHub Actions
* Jenkins pipeline execution
* Continuous regression execution

---

# Future Enhancements

* Docker integration
* Parallel API execution
* Contract testing
* API mocking
* Performance testing integration

---

# Author

Swati Kumari
QA Automation Lead | Senior SDET

