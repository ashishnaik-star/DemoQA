import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class widgets_form_po:
    expand_widgets = (By.XPATH, "(//div[@class='header-right'])[4]")
    accordian_select = (By.XPATH, "//span[text()='Accordian']")
    auto_complete_select = (By.XPATH, "//span[text()='Auto Complete']")
    date_picker_select = (By.XPATH, "//span[text()='Date Picker']")
    expand_section_one = (By.CSS_SELECTOR, "#section1Heading")
    expand_section_two = (By.CSS_SELECTOR, "#section2Heading")
    expand_section_three = (By.CSS_SELECTOR, "#section3Heading")
    content_section_one = (By.CSS_SELECTOR, "#section1Content")
    content_section_two = (By.CSS_SELECTOR, "#section2Content")
    content_section_three = (By.CSS_SELECTOR, "#section3Content")
    auto_complete_color_name = (By.CSS_SELECTOR, "#autoCompleteMultipleContainer>div")
    auto_complete_single = (By.CSS_SELECTOR, "#autoCompleteSingleContainer")
    date_picker_select_date = (By.CSS_SELECTOR, "#datePickerMonthYearInput")
    date_picker_select_date_time = (By.CSS_SELECTOR, "#dateAndTimePickerInput")
    date_picker_dt_month = (By.CSS_SELECTOR, ".react-datepicker__month-read-view")
    date_picker_dt_year = (By.CSS_SELECTOR, ".react-datepicker__year-read-view")

    def __init__(self, driver):
        self.driver = driver

    def click_expand_widgets(self):
        self.driver.find_element(*widgets_form_po.expand_widgets).click()

    def click_accordian(self):
        self.driver.find_element(*widgets_form_po.accordian_select).click()

    def click_auto_complete(self):
        self.driver.find_element(*widgets_form_po.auto_complete_select).click()

    def click_expand_section_one(self):
        self.driver.find_element(*widgets_form_po.expand_section_one).click()

    def click_expand_section_two(self):
        self.driver.find_element(*widgets_form_po.expand_section_two).click()

    def click_expand_section_three(self):
        self.driver.find_element(*widgets_form_po.expand_section_three).click()

    def fetch_section_one_content(self):
        return self.driver.find_element(*widgets_form_po.content_section_one).text

    def fetch_section_two_content(self):
        return self.driver.find_element(*widgets_form_po.content_section_two).text

    def fetch_section_three_content(self):
        return self.driver.find_element(*widgets_form_po.content_section_three).text

    def fill_container_color_names(self, *param1):
        Act = ActionChains(self.driver)
        for parm in param1:
            self.driver.find_element(*widgets_form_po.auto_complete_color_name).click()
            Act.send_keys(parm).perform()
            time.sleep(1)
            Act.send_keys(Keys.ENTER).perform()

    def fill_container_single(self, param1):
        Act = ActionChains(self.driver)
        self.driver.find_element(*widgets_form_po.auto_complete_single).click()
        Act.send_keys(param1).perform()
        time.sleep(1)
        Act.send_keys(Keys.ENTER).perform()

    def click_date_picker(self):
        self.driver.find_element(*widgets_form_po.date_picker_select).click()

    def click_date_picker_date(self):
        self.driver.find_element(*widgets_form_po.date_picker_select_date).click()

    def click_date_picker_date_time(self):
        self.driver.find_element(*widgets_form_po.date_picker_select_date_time).click()

















    
