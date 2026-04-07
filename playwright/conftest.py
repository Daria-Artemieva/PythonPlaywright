import pytest


def launch_browser(playwright, browser_name):
    #headless = not headed
    if browser_name == "chrome":
        return playwright.chromium.launch(headless=False)
    if browser_name == "firefox":
        return playwright.firefox.launch(headless=False)
    raise ValueError(f"Unsupported browser name: {browser_name}")


@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Browser selection"
    )


@pytest.fixture
def browser_instance(playwright, request):
    browser_name = request.config.getoption("browser_name")
    headed = request.config.getoption("headed")
    browser = launch_browser(playwright, browser_name)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()
