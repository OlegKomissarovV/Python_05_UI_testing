from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_link()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_link(self):
        assert 'login' in self.browser.current_url, 'wrong url'


    def should_be_login_form(self):
        assert self.element_is_present(*LoginPageLocators.LOGIN_FORM)


    def should_be_register_form(self):
        assert self.element_is_present(*LoginPageLocators.REGISTER_FORM)


    def register_user(self, email='email', password='password'):
        # Адрес электронной почты передается текстовому элементу на странице регистрации
        self.element_is_visible(LoginPageLocators.REG_EMAIL).send_keys(email)
        # Пароль передается текстовому элементу на странице регистрации
        self.element_is_visible(LoginPageLocators.REG_PASSWORD).send_keys(password)
        # Подтверждение пароля передается текстовому элементу на странице регистрации
        self.element_is_visible(LoginPageLocators.CONFIRM_PASSWORD).send_keys(password)
        # Нажимается кнопка "Зарегистрироваться"
        self.element_is_visible(LoginPageLocators.REG_BTN).click()

