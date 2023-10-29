from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".navbar__auth_login")  # Кнопка "войти"


class LoginFormLocators:
    FORM_LOGIN = (By.CSS_SELECTOR, "#login_form")  # форма логина
    LOGIN_INPUT = (By.CSS_SELECTOR, '[name="login"]')  # поле ввода логина
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[name="password"]')   # поле ввода пароля
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')      # кнопка "войти"


