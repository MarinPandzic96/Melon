import pytest
import json

@pytest.fixture
def browser_instance(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()

@pytest.fixture(scope="session")
def test_data():
    with open("playwright/data/testData.json", "r") as f:
        return json.load(f)