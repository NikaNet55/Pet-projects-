from Pages.form_page import FormPage
from faker import Faker
from selenium.webdriver.common.keys import Keys

fake = Faker(['ru_RU'])


class FormFlow:
    def __init__(self, driver, url):
        self.form_page = FormPage(driver, url)

    def test_form_page(self):
        """
        Тест получает случайное значение фейковыйх данных и передаёт их странице для заполнения
        :return: проверка полученных случайных фейковыйх данных и тех что возвращает страница
        """
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        subject = fake.text(max_nb_chars=25)
        address = fake.address()
        mobile = fake.msisdn()[:10]

        self.form_page.fill_fields_and_submit2(email=email,
                                               first_name=first_name,
                                               last_name=last_name,
                                               mobile=mobile,
                                               subjects=subject,
                                               hobby='Sports',
                                               gender='Male',
                                               file=r'C:\Users\User\PycharmProjects\PyTest Selenium\Pages',
                                               address=address)

        self.form_page.driver.find_element(*self.form_page.submit_button).send_keys(Keys.ENTER)
        table = self.form_page.get_form_results()
        assert table[0] == f"{first_name} {last_name}", f"Несовпадение Имени и Фамилии:{table[0]} и {first_name} {last_name}"
        assert table[1] == email, f"Не совпадает email:{table[1]} и {email}"
        assert table[2] == 'Male', f"Не совпадает пол: {table[2]} и Male"
        assert table[3] == mobile, f"Не совпадает мобильный телефон: {table[3]} и {mobile}"
        assert table[4] == 'Sports', f"Не совпадает мобильный хобби:{table[4]} и Sports"
        assert table[5] == address, f"Не совпадает адрес:{table[5]} и {address}"
