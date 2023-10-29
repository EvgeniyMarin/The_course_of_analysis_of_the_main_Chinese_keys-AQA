from pages.base_page import Base_Page
from pages.locators import MainPageLocators
from pages.locators import LoginFormLocators


class MainPage(Base_Page):
    def the_presence_of_a_button(self):  # метод для проверки наличия кнопки "войти"
        assert self.browser.find_element(*MainPageLocators.LOGIN_BUTTON), "Кнопка ВОЙТИ не найдена"
        print("Кнопка Войти присутствует на странице")

    def go_to_the_login_form(self):  # метод для перехода к форме логина
        button = self.browser.find_element(*MainPageLocators.LOGIN_BUTTON)
        button.click()
        print("Передох на форму логина")

    def availability_of_a_login_form(self):  # метод для проверки наличия формы логина
        assert self.browser.find_element(*LoginFormLocators.FORM_LOGIN), "Форма логина ОТСУТСТВУЕТ"
        print("Форма логина присутствует")

    def the_presence_of_an_email_field(self):  # метод для проверки наличия поля ввода логина (почты)
        assert self.browser.find_element(*LoginFormLocators.LOGIN_INPUT), "Поле ввода логина отсутствует"
        print("Поле ввода логина присутствует")

    def the_presence_of_an_password_field(self):  # метод для проверки наличия поля ввода пароля
        assert self.browser.find_element(*LoginFormLocators.PASSWORD_INPUT), "Поле ввода пароля отсутствует"
        print("Поле ввода пароля присутствует")

    def button_log_in(self):  # метод проверки наличия кнопки для входа в систему
        assert self.browser.find_element(*LoginFormLocators.SUBMIT_BUTTON), "Кнопка входа в систему ОТСУТСТВУЕТ"
        print("Кнопка входа в систему ПРИСУТСТВУЕТ")

    def login_input(self, login):  # метод ввода логина
        input_email = self.browser.find_element(*LoginFormLocators.LOGIN_INPUT)
        input_email.send_keys(login)

    def password_input(self, password):  # метод ввода пароля
        input_password = self.browser.find_element(*LoginFormLocators.PASSWORD_INPUT)
        input_password.send_keys(password)

    def log_in(self):  # метод входа в систему
        button_log_in = self.browser.find_element(*LoginFormLocators.SUBMIT_BUTTON)
        button_log_in.click()

