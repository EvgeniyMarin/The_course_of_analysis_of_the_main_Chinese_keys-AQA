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

    def availability_of_a_login_form(self):         # метод для проверки наличия формы логина
        assert self.browser.find_element(*LoginFormLocators.FORM_LOGIN), "Форма логина ОТСУТСТВУЕТ"
        print("Форма логина присутствует")