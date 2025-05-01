from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    CART_ITEMS = (By.CSS_SELECTOR, ".table-responsive tr")
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "#content p")
    REMOVE_BUTTON = (By.CSS_SELECTOR, ".btn-danger")
    CONTINUE_BUTTON = (By.LINK_TEXT, "Continue Shopping")
    CHECKOUT_BUTTON = (By.LINK_TEXT, "Checkout")
    ITEM_NAME = (By.CSS_SELECTOR, ".text-left > a")
    ITEM_PRICE = (By.CSS_SELECTOR, ".text-right:nth-child(5)")
    ITEM_QUANTITY = (By.CSS_SELECTOR, ".text-center input")

    def is_empty(self):
        """Проверяет, пуста ли корзина"""
        return self.is_visible(self.EMPTY_CART_MESSAGE)

    def get_items_count(self):
        """Возвращает количество товаров в корзине"""
        items = self.driver.find_elements(*self.CART_ITEMS)
        return len(items) - 1  # минус заголовок таблицы

    def remove_all_items(self):
        """Удаляет все товары из корзины"""
        while not self.is_empty():
            self.click(self.REMOVE_BUTTON)
            self.wait_for_invisibility(self.REMOVE_BUTTON)

    def get_product_names(self):
        """Возвращает список названий товаров в корзине"""
        return [el.text for el in self.driver.find_elements(*self.ITEM_NAME)]

    def continue_shopping(self):
        """Продолжить покупки"""
        self.click(self.CONTINUE_BUTTON)
        from .main_page import MainPage
        return MainPage(self.driver)