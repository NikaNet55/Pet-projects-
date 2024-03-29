from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(object):

    def __init__(self, driver, url):  # принимает значение драйвера браузера и ссылку
        self.driver = driver
        self.url = url
        self.get()

    def wait_page_loaded(self, timeout=5):
        return Wait(self.driver, timeout)

    def element_is_visible(self, locator: tuple[str, str], timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def get(self):  # Загрузка страницы по ссылке
        self.driver.get(self.url)

    def go_back(self):
        self.driver.back()
        self.wait_page_loaded()

    def refresh(self):
        self.driver.refresh()
        self.wait_page_loaded()

    def scroll_down(self, offset=0):  # прокрутка страницы вниз до конца или на указанное значение пикселей

        if offset:
            self.driver.execute_script('window.scrollTo(0, {0});'.format(offset))
        else:
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    def scroll_up(self, offset=0):  # прокрутка страницы вверх до конца или на указанное значение пикселей

        if offset:
            self.driver.execute_script('window.scrollTo(0, -{0});'.format(offset))
        else:
            self.driver.execute_script('window.scrollTo(0, -document.body.scrollHeight);')
