from typing import Tuple, Any, List
from Pages.Page_Objects import MainPage
from Pages.PageLocators import FormLocators
from selenium.webdriver.common.by import By


class FormPage(MainPage, FormLocators):

    def fill_fields_and_submit2(self, **kwargs):
        """
        функцмя вводит в форму данные для заполнения
        :return: Имя, Фамилия и почта для проверки ввода
        """

        genders = {'Male': self.gender_male, 'Female': self.gender_female, 'Other': self.gender_other}
        hobbies = {'Sports': self.hobby_sport_checkbox, 'Reading': self.hobby_reading_checkbox,
                   'Misic': self.hobby_misic_checkbox}
        self.wait_page_loaded(timeout=60)
        self.driver.find_element(*self.first_name).send_keys(kwargs.get('first_name'))
        self.driver.find_element(*self.last_name).send_keys(kwargs.get('last_name'))
        self.driver.find_element(*self.EMAIL).send_keys(kwargs.get('email'))
        self.element_is_visible(genders[kwargs.get('gender')], timeout=10).click()
        self.driver.find_element(*self.MOBILE).send_keys(kwargs.get('mobile'))
        self.driver.find_element(*hobbies[kwargs.get('hobby')]).click()
        self.driver.find_element(*self.file_input).send_keys(kwargs.get('file'))
        self.driver.find_element(*self.CURRENT_ADRESS).send_keys(kwargs.get('address'))

    def get_form_results(self) -> list[Any]:
        """
        Получение результатов формы
        :return: list результатов
        """
        first_last_name = self.driver.find_element(By.XPATH,
                                                             '/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[1]/td[2]').text
        email = self.driver.find_element(By.XPATH,
                                                   '/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[2]/td[2]').text
        gender = self.driver.find_element(By.XPATH,
                                                    '/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[3]/td[2]').text
        mobile = self.driver.find_element(By.XPATH,
                                                    '/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[4]/td[2]').text
        hobbies = self.driver.find_element(By.XPATH,
                                                     '/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[7]/td[2]').text
        address = self.driver.find_element(By.XPATH,
                                                     '/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[9]/td[2]').text

        results_table = [first_last_name, email, gender, mobile, hobbies, address]

        return results_table
