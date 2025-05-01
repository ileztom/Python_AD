import pytest
import allure
from pages.admin.admin_login_page import AdminLoginPage
from pages.main_page import MainPage


@allure.feature("Админ-панель OpenCart")
class TestAdminPanel:
    ADMIN_URL = "https://demo.opencart.com/admin"
    ADMIN_USER = "admin"
    ADMIN_PASS = "admin"

    @allure.story("Создание категории и товаров")
    def test_create_category_and_products(self, driver):
        with allure.step("Логин в админ-панель"):
            admin_page = AdminLoginPage(driver)
            admin_page.driver.get(self.ADMIN_URL)
            dashboard = admin_page.login(self.ADMIN_USER, self.ADMIN_PASS)

        with allure.step("Создание категории Devices"):
            categories_page = dashboard.open_categories()
            categories_page.create_category("Devices")

        with allure.step("Добавление 2 мышей"):
            products_page = dashboard.open_products()
            products_page.create_product("Mouse 1", "M001", "50", "Devices")
            products_page.create_product("Mouse 2", "M002", "60", "Devices")

        with allure.step("Добавление 2 клавиатур"):
            products_page.create_product("Keyboard 1", "K001", "70", "Devices")
            products_page.create_product("Keyboard 2", "K002", "80", "Devices")

        with allure.step("Проверка на главной странице"):
            main_page = MainPage(driver)
            main_page.driver.get("https://demo.opencart.com/")

            for product in ["Mouse 1", "Mouse 2", "Keyboard 1", "Keyboard 2"]:
                search_page = main_page.search_product(product)
                assert product in driver.page_source, f"Товар {product} не найден"

    @allure.story("Удаление товаров")
    def test_delete_products(self, driver):
        with allure.step("Логин в админ-панель"):
            admin_page = AdminLoginPage(driver)
            admin_page.driver.get(self.ADMIN_URL)
            dashboard = admin_page.login(self.ADMIN_USER, self.ADMIN_PASS)

        with allure.step("Удаление 1 мыши и 1 клавиатуры"):
            products_page = dashboard.open_products()
            products_page.delete_products_by_name("Mouse 1")
            products_page.delete_products_by_name("Keyboard 1")

        with allure.step("Проверка на главной странице"):
            main_page = MainPage(driver)
            main_page.driver.get("https://demo.opencart.com/")

            # Проверяем что удаленные товары отсутствуют
            for product in ["Mouse 1", "Keyboard 1"]:
                search_page = main_page.search_product(product)
                assert "No results" in driver.page_source, f"Товар {product} не был удален"

            # Проверяем что оставшиеся товары присутствуют
            for product in ["Mouse 2", "Keyboard 2"]:
                search_page = main_page.search_product(product)
                assert product in driver.page_source, f"Товар {product} не найден"