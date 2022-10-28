from logging.handlers import WatchedFileHandler
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
import re

class BasePage():


    def __init__(self, browser, link):
        self.browser = browser
        self.link = link
    

    # Открывает страницу
    def open_page(self):
        self.browser.get(self.link)


    # Возвращается объект WebElement на основе заданного критерия поиска
    def element_is_present(self, method, locator):
        try:
            self.browser.find_element(method, locator)
        except NoSuchElementException:
            return False
        return True
    

    # Возвращается список WebElements, соответствующий критериям поиска
    def elements_are_present(self, method, locator):
        try:
            return self.browser.find_elements(method, locator)
        except NoSuchElementException:
            return NoSuchElementException


    # Проверяет, что пользователь авторизован
    def should_be_autorized_user(self):
        assert self.element_is_present(*BasePageLocators.USER_ICON)


    # Возвращается элемент или запускается ожидание timeout секунд появления элемента
    # до того, как вернется исключение TimeoutException, если не появится элемент за timeout 
    def element_is_visible(self, locator, timeout = 5):
        return Wait(self.browser, timeout).until(EC.visibility_of_element_located(locator))


    # Возвращаются элементы или запускается ожидание timeout секунд до того, 
    # как вернется исключение TimeoutException, если не найдет элемент за timeout 
    def elements_are_located(self, locator, timeout = 5):
        return Wait(self.browser, timeout).until(EC.presence_of_all_elements_located((locator)))


    # Возвращает цену элемента числом с плавающей точкой
    def get_price(self, price):
        return float(re.sub("[(,|.?)]", '.', price.text[:-2]))