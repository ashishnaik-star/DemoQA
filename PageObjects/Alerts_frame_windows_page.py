from selenium.webdriver.common.by import By


class afw_po:
    expand_afw = (By.XPATH, "(//div[@class='header-right'])[3]")
    browser_windows = (By.XPATH, "//span[text()='Browser Windows']")

    def __init__(self,driver):
        self.driver=driver

    def click_expand_afw(self):
        self.driver.find_element(*afw_po.expand_afw).click()

    def browser_windows_click(self):
        self.driver.find_element(*afw_po.browser_windows).click()







