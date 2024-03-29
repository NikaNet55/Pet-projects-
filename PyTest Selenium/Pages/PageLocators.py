from selenium.webdriver.common.by import By


class FormLocators:
    first_name = (By.XPATH, '//input [@id="firstName"]')
    last_name = (By.XPATH, '//input [@id="lastName"]')
    EMAIL = (By.XPATH, '//input [@placeholder="name@example.com"]')
    gender_male = (
    By.XPATH, '//*[@id="gender-radio-1"]/ancestor::div[@class="custom-control custom-radio custom-control-inline"]')
    gender_female = (By.XPATH, '//input [@id="gender-radio-2"]')
    gender_other = (By.XPATH, '//input [@id="gender-radio-3"]')
    MOBILE = (By.XPATH, '//input[@id="userNumber"]')
    subjects = (By.XPATH, '//*[@id="subjectsContainer"]/div')
    hobby_sport_checkbox = (By.XPATH, '//*[@id="hobbiesWrapper"]/div[2]/div[1]')
    hobby_reading_checkbox = (By.XPATH, '//input[@id="hobbies-checkbox-2"]')
    hobby_misic_checkbox = (By.XPATH, '//input[@id="hobbies-checkbox-3"]')
    HOBBIES = (By.XPATH, '//*[@id="hobbiesWrapper"]/div[2]/div[1]/label')
    file_input = (By.XPATH, '//input[@id="uploadPicture"]')
    CURRENT_ADRESS = (By.XPATH, '//textarea[@id="currentAddress"]')
    submit_button = (By.XPATH, '//button[@id="submit"]')
    RESULT_TABLE = (By.XPATH, '//div[@class="table-responsive"]')
