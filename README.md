# Playwright BDD Framework

## Setup Instructions
1. Install requirements: `pip install -r requirements.txt`
2. Install Playwright browsers: `playwright install`

## Execution
Run all tests and generate Allure results:
`behave -f allure_behave.formatter:AllureFormatter -o allure-results features/`

`Remove-Item -Recurse -Force allure-results -ErrorAction SilentlyContinue; behave -f allure_behave.formatter:AllureFormatter -o allure-results features/HRpage.feature`

View Allure Report:
`allure serve allure-results`
