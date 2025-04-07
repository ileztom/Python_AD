import allure
import pytest
import logging
from selenium import webdriver


@pytest.fixture(scope="function")
def driver(request):
    # Настройка логгера для теста
    logger = logging.getLogger(request.node.name)
    logger.setLevel(logging.INFO)

    # Создаем драйвер
    driver = webdriver.Chrome()
    driver.maximize_window()

    logger.info("Браузер запущен")
    yield driver

    # Если тест упал, делаем скриншот
    if request.node.rep_call.failed:
        screenshot = driver.get_screenshot_as_png()
        allure.attach(
            screenshot,
            name=f"{request.node.name}_failure",
            attachment_type=allure.attachment_type.PNG
        )
        logger.error(f"Тест упал: {request.node.name}")

    driver.quit()
    logger.info("Браузер закрыт")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)