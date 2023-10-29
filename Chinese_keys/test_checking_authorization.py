from pages.main_page import MainPage


def test_the_presence_of_a_login_button(browser):
    """Тест наличия входа в систему"""
    url = "https://stepik.org/catalog"
    page = MainPage(browser, url)     # инициализация объекта Page Object
    page.open_page()                  # открытие страницы по заданному url
    page.the_presence_of_a_button()
