# PytestPython

Sample automation project built with `pytest` and `Playwright`, including:

- UI tests
- API tests
- end-to-end API + UI scenarios
- BDD scenarios with `pytest-bdd`

## Project Structure

- `playwright/` - main Playwright tests, page objects, API utilities, and test data
- `playwright/page_objects/` - page object classes
- `playwright/utils/` - helper classes for API interactions
- `playwright/data/credentials.json` - test credentials
- `playwright/Features/` - BDD feature files
- `pytest_dir/` - separate basic pytest examples
- `pytest.ini` - pytest configuration and markers

## Included Tests

- `playwright/test_playwright_basics.py` - basic UI checks and browser usage examples
- `playwright/test_ui_validation_1.py` - UI scenarios with products and popup window handling
- `playwright/test_web_api.py` - e2e flow: create order via API and validate it in UI
- `playwright/test_framework_web_api.py` - e2e flow using page objects and parametrization
- `playwright/test_framework_web_api_bdd.py` - BDD version of the e2e scenario
- `playwright/test_api_create_order.py` - standalone API test for order creation

## Installation

Create and activate a virtual environment, then install dependencies:

```bash
pip install pytest playwright pytest-bdd
playwright install
```

## Running Tests

Run all tests:

```bash
pytest
```

Run only Playwright tests:

```bash
pytest playwright
```

Run the standalone API test:

```bash
pytest playwright/test_api_create_order.py -q
```

Run smoke tests:

```bash
pytest -m smoke
```

Select a browser:

```bash
pytest playwright --browser_name=chrome
pytest playwright --browser_name=firefox
```

## Notes

- The tests use the external site `https://rahulshettyacademy.com`, so internet access is required.
- Test credentials are stored in `playwright/data/credentials.json`.
- In `playwright/conftest.py`, the browser is launched with `headless=False`.
