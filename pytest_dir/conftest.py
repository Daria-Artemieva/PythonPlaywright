import pytest


@pytest.fixture(scope="module")
def pre_work():
    print("I setup module instance")
    return "fail"


@pytest.fixture(scope="module")
def pre_setup_work():
    print("I setup browser instance")