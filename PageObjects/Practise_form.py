from selenium.webdriver.common.by import By


class Practise_form_po:

    Forms_click_expand = (By.XPATH,"//div[@class='accordion']/div[2]/span/div/div[2]")
    practise_form_click = (By.XPATH,"//span[text()='Practice Form']")

    def __init__(self,driver):
        self.driver = driver

    def click_practise_form(self):
        self.driver.find_element(*Practise_form_po.practise_form_click).click()


