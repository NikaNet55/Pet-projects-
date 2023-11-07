from flow.form_flow import FormFlow
from selenium import webdriver
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_fill_form(driver):
    """
    Тест формы с проверкой соответствия имени, фамилии, почты
    :param driver: Chrom
    :return: результаты теста
    """
    url = 'https://demoqa.com/automation-practice-form'
    form_flow = FormFlow(driver, url)
    form_flow.test_form_page()
