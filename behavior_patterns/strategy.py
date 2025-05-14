class PaymentStrategy:
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Оплата {amount} через кредитную карту")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Оплата {amount} через PayPal")

class ShoppingCart:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def checkout(self, amount):
        self._strategy.pay(amount)

cart = ShoppingCart(CreditCardPayment())
cart.checkout(100)

cart = ShoppingCart(PayPalPayment())
cart.checkout(200)