from selenium.webdriver.common.by import By
from .base_page import BasePage

class SearchPage(BasePage):
    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".btn-default")
    PRODUCT_ITEMS = (By.CSS_SELECTOR, ".product-layout")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".caption h4 a")
    NO_RESULTS_MESSAGE = (By.XPATH, "//p[contains(text(),'There is no product')]")

    def search(self, query):
        """Выполняет поиск товара"""
        self.send_keys(self.SEARCH_INPUT, query)
        self.click(self.SEARCH_BUTTON)
        return self

    def get_found_products(self):
        """Возвращает список найденных товаров"""
        return [el.text for el in self.driver.find_elements(*self.PRODUCT_NAME)]

    def is_no_results(self):
        """Проверяет сообщение 'нет результатов'"""
        return self.is_visible(self.NO_RESULTS_MESSAGE)

    def open_product(self, product_name):
        """Открывает страницу товара по названию"""
        products = self.driver.find_elements(*self.PRODUCT_ITEMS)
        for product in products:
            name = product.find_element(*self.PRODUCT_NAME).text
            if name == product_name:
                product.find_element(*self.PRODUCT_NAME).click()
                from .product_page import ProductPage
                return ProductPage(self.driver)
        raise ValueError(f"Товар '{product_name}' не найден")