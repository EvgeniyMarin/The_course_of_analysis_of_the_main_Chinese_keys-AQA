from pages.main_page import MainPage
import time


def test_the_presence_of_a_login_button(browser):
    """Тест наличия входа в систему"""
    url = "https://stepik.org/catalog"
    page = MainPage(browser, url)  # инициализация объекта Page Object
    page.open_page()  # открытие страницы по заданному url
    page.the_presence_of_a_button()


def test_availability_of_a_login_form(browser):
    """Тест наличия формы логина"""
    url = "https://stepik.org/catalog"
    page = MainPage(browser, url)  # инициализация объекта Page Object
    page.open_page()  # открытие страницы по заданному url
    page.go_to_the_login_form()
    time.sleep(10)
    page.availability_of_a_login_form()

def test_the_presence_of_a_field_for_entering_a_login(browser):
    """Тест наличия поля ввода логина"""
    url = "https://stepik.org/catalog"
    page = MainPage(browser, url)
    page.open_page()
    page.go_to_the_login_form()
    page.the_presence_of_an_email_field()

def test_the_presence_of_a_field_for_entering_a_password(browser):
    """Тест наличия поля ввода пароля"""
    url = "https://stepik.org/catalog"
    page = MainPage(browser, url)
    page.open_page()
    page.go_to_the_login_form()
    page.the_presence_of_an_password_field()

def test_the_presence_of_a_button_log_in(browser):
    """Тест наличия кнопки входа в систему"""
    url = "https://stepik.org/catalog"
    page = MainPage(browser, url)
    page.open_page()
    page.go_to_the_login_form()
    page.button_log_in()

def test_authorization_on_the_site(browser):
    """Тест авторизации на сайте"""
    url = "https://stepik.org/catalog?auth=login"
    login = "evgeniymarin7@mail.ru"
    password = "D19675d77777d"
    page = MainPage(browser, url)
    page.open_page()
    page.login_input(login)
    page.password_input(password)
    page.log_in()
    page.successful_authorization()
    time.sleep(5)


"""Написать этот тест без использования PAGE OBJECT""" # написан
