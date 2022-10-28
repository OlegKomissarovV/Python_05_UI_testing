from selenium.webdriver.common.by import By


class MainPageLocators():
    LINK_TO_PRODUCT_PAGE = (By.XPATH, "//ul[@id='browse']//ul//a")
    PROD_PRICE = (By.CSS_SELECTOR, '.product_price')
    LOGIN_BTN = (By.ID, 'login_link')
    BASKET_BTN = (By.CSS_SELECTOR, '[href *= "basket"]')


class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    REG_EMAIL = (By.ID, 'id_registration-email')
    REG_PASSWORD = (By.ID, 'id_registration-password1')
    CONFIRM_PASSWORD = (By.ID, 'id_registration-password2')
    REG_BTN = (By.CSS_SELECTOR, "#register_form button")


class BasketPageLocators():
    PRICEBOOK = (By.CSS_SELECTOR, '.basket-items div:nth-last-child(2) > p')
    TOTALPRICEBOOK = (By.CSS_SELECTOR, '.basket-items div:last-child > p')
    PRICEDISCOUNT = (By.CSS_SELECTOR, 'td[class = "basket-discount"] ~ td')
    PRICEOUTDISCOUNT = (By.CSS_SELECTOR, 'td:not([class]) ~ td')
    QUANTITY = (By.CSS_SELECTOR, '.basket-items .form-control')
    TOTALPRICE = (By.CSS_SELECTOR, '#basket_totals .price_color')
    REFRESH_BTN = (By.CSS_SELECTOR, 'span button[type="submit"]')


class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')