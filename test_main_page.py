import pytest
import time
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage



link = 'http://selenium1py.pythonanywhere.com/ru/'
# Количество книг
count = 3


# Тест проверяет, что пользователь может перейти с главной страницы сайта на страницу с товарами
@pytest.mark.smoke
def test_guest_can_go_to_catalogue(browser):
    # Создает экземпляр главной страницы - Main Page
    page = MainPage(browser, link)
    # Открывает страницу
    page.open_page()
    # Проверяет, что на главной странице присутствует ссылка на страницу товаров
    page.should_be_link_to_product_page()
    # Переходит на страницу с товарами
    page.go_to_product_page()


# Тест проверяет, что пользователь может перейти с главной страницы сайта на страницу авторизации
@pytest.mark.regression
def test_guest_can_go_to_login_page(browser):
    # Создает экземпляр главной страницы - Main Page
    page = MainPage(browser, link)
    # Открывает страницу
    page.open_page()
    # Переходит на страницу авторизации
    page.go_to_login_page()
    # Создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # Проверяет, что текущая страница является страницей авторизации
    page.should_be_login_page()


# Тест проверяет, что пользователь может зарегистрироваться
def test_user_сan_autorize(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    # Создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # Открывает страницу авторизации
    page.open_page()
    # Регистрирует нового пользователя
    page.register_user(email=str(time.time()) + '@mail.org', password='QAZ123edc!')
    # Проверяет, что пользователь авторизован
    page.should_be_autorized_user()


# Тест проверяет, что пользователь может перейти с главной страницы сайта на страницу корзины
def test_guest_can_go_to_basket(browser):
    link = 'https://selenium1py.pythonanywhere.com/ru/catalogue/category/books_2/?page=3'
    # Создает экземпляр главной страницы - Main Page
    page = MainPage(browser, link)
    # Открывает страницу
    page.open_page()
    # Проверяет, что на главной странице присутствует ссылка на страницу корзины
    page.should_be_link_to_basket_page()
    # Переходит на страницу корзины
    page.go_to_basket_page()


# Тест проверяет, что пользователь добавил в корзину только 3 книги 
# каждой по 1 шт. и стоимостью каждой менее 10 £
def test_cheap_books_in_basket(browser):
    link = 'https://selenium1py.pythonanywhere.com/ru/catalogue/category/books_2/?page=3'
    # Создает экземпляр главной страницы - Main Page
    page = MainPage(browser, link)
    # Открывает страницу
    page.open_page()
    # Добавляет в корзину количество книг
    page.add_books_to_basket(count)
    link = 'https://selenium1py.pythonanywhere.com/ru/basket/'
    # Создает экземпляр страницы авторизации
    page = BasketPage(browser, link)
    # Открывает страницу
    page.open_page()
    # Проверяет, что текущая страница является страницей корзины
    page.should_be_basket_page()
    # Сравнивает количество книг в корзине стоимостью менее 10 £
    page.get_count_book()
    # Проверяет наличие скидки
    page.discount_exists()
    # Сравнивает сумму всех книг и общую стоимость книг без скидки
    page.eq_total_price_wout_disc()
    # Сравнивает сумму всех книг и общую стоимость с учетом скидки
    page.eq_total_price_with_disc() 


# Тест проверяет, что пользователь может добавить товар в корзину
def test_user_can_add_book_to_basket(browser):
    link = 'https://selenium1py.pythonanywhere.com/ru/catalogue/category/books_2/?page=3'
    # Создает экземпляр главной страницы - Main Page
    page = MainPage(browser, link)
    # Открывает страницу
    page.open_page()
    # Добавляет в корзину указанное количество книг
    page.add_books_to_basket(count)