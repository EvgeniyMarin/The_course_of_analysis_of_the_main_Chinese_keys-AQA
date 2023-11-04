from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".navbar__auth_login")  # Кнопка "войти"


class LoginFormLocators:
    FORM_LOGIN = (By.CSS_SELECTOR, "#login_form")  # форма логина
    LOGIN_INPUT = (By.CSS_SELECTOR, '[name="login"]')  # поле ввода логина
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[name="password"]')   # поле ввода пароля
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')      # кнопка "войти"
    LOGIN_AVATAR = (By.CSS_SELECTOR, 'button.navbar__profile-toggler')    # аватар для перехода в профиль (появляется при успешной регистрации)


class SearchPageLocators:
    SEARCH_INPUT_FIEND = (By.CSS_SELECTOR, ".search-form__input")    # поле ввода для поиска
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".search-form__submit")      # кнопка поиска
