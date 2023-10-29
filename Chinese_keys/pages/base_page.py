class Base_Page:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)         # неявное ожидание в 10 секунд

    def open_page(self):
        self.browser.get(self.url)

