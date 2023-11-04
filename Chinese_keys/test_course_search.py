from pages.search_page import Search_page
import time


def test_presence_of_an_input_field(browser):
    """Тест наличия поля ввода поиска"""
    url = "https://stepik.org/catalog/search"
    page = Search_page(browser, url)
    page.open_page()
    page.presence_of_an_input_field()


def test_presence_of_a_search_button(browser):
    url = "https://stepik.org/catalog/search"
    page = Search_page(browser, url)
    page.open_page()
    page.presence_of_a_search_button()
