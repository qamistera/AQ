import allure
import pytest
from playwright.sync_api import sync_playwright

#1

@pytest.fixture(scope="session")
@allure.title("Создание браузера для сессии")
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()
    playwright.stop()

"""
#2 no start stop

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        with allure.step("Запускаем браузер"):
            browser = playwright.chromium.launch(headless=False)
            yield browser
            browser.close()
            
"""
