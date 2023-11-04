from pages.main_page import MainPage
from pages.locators import SearchPageLocators


class Search_page(MainPage):
    def presence_of_an_input_field(self):
        assert self.browser.find_element(*SearchPageLocators.SEARCH_INPUT_FIEND), "поле ввода для поиска отсутствует"
        print("Поле ввода для поиска ПРИСУТСТВУЕТ")

    def presence_of_a_search_button(self):  # метод для проверки наличия кнопки "поиск"
        assert self.browser.find_element(*SearchPageLocators.SEARCH_BUTTON), "кнопка поиска не найдена"
        print("Кнопка 'поиск' ПРИСУТСТВУЕТ")
