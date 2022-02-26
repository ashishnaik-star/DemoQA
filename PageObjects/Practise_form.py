import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By


class Practise_form_po:

    Forms_click_expand = (By.XPATH, "//div[@class='accordion']/div[2]/span/div/div[2]")
    practise_form_click = (By.XPATH, "//span[text()='Practice Form']")
    resizable_interactions_click = (By.XPATH, "//span[text()='Resizable']")
    enter_first_name = (By.CSS_SELECTOR,"#firstName")
    enter_last_name = (By.CSS_SELECTOR, "#lastName")
    radio_button_gender_female = (By.XPATH, "//label[@for='gender-radio-2']")
    enter_user_number = (By.CSS_SELECTOR, "#userNumber")
    enter_email = (By.CSS_SELECTOR, "#userEmail")
    hobbies_checkbox_reading = (By.XPATH, "//label[@for='hobbies-checkbox-2']")
    subjects_form_Maths = (By.CSS_SELECTOR, "#subjectsContainer")
    upload_picture = (By.CSS_SELECTOR, "#uploadPicture")
    current_address = (By.CSS_SELECTOR, "#currentAddress")
    select_state = (By.CSS_SELECTOR, "#state")
    select_city = (By.CSS_SELECTOR, "#city")
    submit_click = (By.CSS_SELECTOR, "#submit")
    close_submit_form = (By.CSS_SELECTOR, "#closeLargeModal")
    date_picker = (By.CSS_SELECTOR, "#dateOfBirthInput")
    date_picker_month = (By.CSS_SELECTOR, ".react-datepicker__month-select")
    date_picker_year = (By.CSS_SELECTOR, ".react-datepicker__year-select")
    student_name_entered = (By.XPATH, "//td[text() = 'Student Name']/following-sibling::td")

    def __init__(self,driver):
        self.driver = driver

    def click_practise_form(self):
        self.driver.find_element(*Practise_form_po.practise_form_click).click()

    def click_first_name(self):
        return self.driver.find_element(*Practise_form_po.enter_first_name)

    def click_last_name(self):
        return self.driver.find_element(*Practise_form_po.enter_last_name)

    def click_gender_radio_female(self):
        self.driver.find_element(*Practise_form_po.radio_button_gender_female).click()

    def click_user_number(self):
        return self.driver.find_element(*Practise_form_po.enter_user_number)

    def click_email_id(self):
        return self.driver.find_element(*Practise_form_po.enter_email)

    def click_subject_form_Maths(self):
        self.driver.find_element(*Practise_form_po.subjects_form_Maths).click()
        actions = ActionChains(self.driver)
        actions.send_keys("Maths").perform()
        time.sleep(2)
        actions.send_keys(Keys.ENTER).perform()

    def click_current_address(self):
        return self.driver.find_element(*Practise_form_po.current_address)

    def click_hobbies_checkbox_reading(self):
        self.driver.find_element(*Practise_form_po.hobbies_checkbox_reading).click()

    def click_upload_image(self):
        return self.driver.find_element(*Practise_form_po.upload_picture)

    def click_state(self):
        return self.driver.find_element(*Practise_form_po.select_state).click()

    def click_city(self):
        return self.driver.find_element(*Practise_form_po.select_city).click()

    def click_on_submit(self):
        return self.driver.find_element(*Practise_form_po.submit_click).click()

    def click_close_submitform(self):
        return self.driver.find_element(*Practise_form_po.close_submit_form).click()

    def date_picker_click(self):
        return self.driver.find_element(*Practise_form_po.date_picker).click()

    def get_student_name(self):
        return self.driver.find_element(*Practise_form_po.student_name_entered).text



