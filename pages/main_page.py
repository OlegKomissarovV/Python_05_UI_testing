from time import time
from .base_page import BasePage
from .locators import MainPageLocators
import re


class MainPage(BasePage):

    def should_be_link_to_product_page(self):
        assert self.element_is_visible(MainPageLocators.LINK_TO_PRODUCT_PAGE)
  

    def should_be_link_to_basket_page(self):
        assert self.element_is_visible(MainPageLocators.BASKET_BTN)
        

    def go_to_product_page(self):
        self.element_is_visible(MainPageLocators.LINK_TO_PRODUCT_PAGE).click()


    def go_to_basket_page(self):
        self.element_is_visible(MainPageLocators.BASKET_BTN).click()


    def go_to_login_page(self):
        self.element_is_visible(MainPageLocators.LOGIN_BTN).click()


    def add_elements_page(self):
        return self.elements_are_present(*MainPageLocators.BOOK_PRICE)
        

    # Определяется соответствие книги на странице требованиям 
    def get_book(self, prod_price):
        price = prod_price.get_property('children')
        # Проверяется доступность книги для заказа и стоимости книги 
        if price[1].text == 'Недоступно' or self.get_price(price[0]) > 10: return
        # Добавляется в корзину книга и обновляется страница
        self.add_book(price[2].get_property('children')[2])
        return price


    # Добавляется в корзину книга и обновляется страница
    def add_book(self, button):
        button.click()
        self.browser.refresh()


    #Добавляются в корзину требуемые книги
    def add_books_to_basket(self, book_count):
        list_el_prodprice = self.elements_are_located(MainPageLocators.PROD_PRICE)
        count = 0
        for i in range(len(list_el_prodprice)):
            if count == book_count: break
            prod_price = self.elements_are_located(MainPageLocators.PROD_PRICE)
            if self.get_book(prod_price[i]): count += 1
        assert count == book_count, 'wrong count books'