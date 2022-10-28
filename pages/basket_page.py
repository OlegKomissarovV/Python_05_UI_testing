from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    # Проверяет, что текущая страница является страницей корзины
    def should_be_basket_page(self):
        self.should_be_basket_link()

    
    def should_be_basket_link(self):
        assert 'basket' in self.browser.current_url, 'wrong url'

        
    # Определяется сумма цен каждой книги за 1 шт.
    def get_sum_prices(self):
        # Получает список элементов цен каждой книги за 1 шт.
        list_el_price = self.browser.find_elements(*BasketPageLocators.PRICEBOOK)
        return sum(map(self.get_price, list_el_price))


    # Определяется сумма скидки
    def get_discount(self):
        # Получает элемент скидки
        el_price = self.browser.find_element(*BasketPageLocators.PRICEDISCOUNT)
        return self.get_price(el_price)


    # Определяется скидка согласно требованиям
    def discount_exists(self):
        assert self.get_discount() != 0, 'no discount'


    # Возвращается общая стоимость книг в корзине без учета скидок
    def get_total_price_wout_disc(self):
        # Получает элемент общей стоимости книг в корзине без учета скидок
        el_price = self.browser.find_element(*BasketPageLocators.PRICEOUTDISCOUNT)
        return self.get_price(el_price)


    # Сравнивается сумма всех книг и общая стоимость книг без скидки
    def eq_total_price_wout_disc(self):
        # Сумма цен каждой книги за 1 шт.
        sum_prices_books = self.get_sum_prices()
        # Общая стоимость книг в корзине без учета скидки
        total_price_basket = self.get_total_price_wout_disc()
        assert sum_prices_books == total_price_basket, 'no equals total prices without discount'
    

    # Сравнивается сумма всех книг и общая стоимость с учетом скидки
    def eq_total_price_with_disc(self):
        # Сумма цен каждой книги за 1 шт.
        total_price = self.get_sum_prices()
        # Сумма скидки
        discount_price = self.get_discount()
        # Получает элемент общей стоимости книг в корзине c учетом скидки
        el_price = self.browser.find_element(*BasketPageLocators.TOTALPRICE)
        assert total_price + discount_price == self.get_price(el_price), 'wrong total price with discount'


    # Определяется соответствие требованиям количества каждой книги 
    def get_quantity_book(self, quantity):
        k = int(quantity.get_property('value'))
        assert int(quantity.get_property('value')) == 1, 'wrong quantity book'


    # Определяется количество книг, указанных в поле ввода input
    def get_count_book(self):
        # Получает список элементов количества каждой книги
        list_el_quantity = self.browser.find_elements(*BasketPageLocators.QUANTITY)
        list(map(self.get_quantity_book, list_el_quantity))
    
