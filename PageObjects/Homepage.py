from selenium.webdriver.common.by import By

class HomePageCls:

    ToolsQA_heading = (By.XPATH, "//header/a[1]")
    Elements = (By.XPATH, "// h5[contains(text(), 'Elements')]")
    Alert_frame_window = (By.XPATH, "//h5[contains(text(), 'Alerts, Frame & Windows')]")
    Widgets = (By.XPATH, "// h5[contains(text(), 'Widgets')]")
    Forms = (By.XPATH, "// h5[contains(text(), 'Forms')]")
    BookstoreApp = (By.XPATH, "// h5[contains(text(),'Book Store Application')]")
    Interactions = (By.XPATH, "// h5[contains(text(), 'Interactions')]")

    def __init__(self, driver):
        self.driver = driver

    def Heading_refresh(self):
        return self.driver.find_element(*HomePageCls.ToolsQA_heading)

    def Elements_homepage(self):
        return self.driver.find_element(*HomePageCls.Elements)

    def Forms_homepage(self):
        return self.driver.find_element(*HomePageCls.Forms)

    def Widgets_homepage(self):
        return self.driver.find_element(*HomePageCls.Widgets)

    def AFW_homepage(self):
        return self.driver.find_element(*HomePageCls.Alert_frame_window)

    def BookstoreApp_homepage(self):
        return self.driver.find_element(*HomePageCls.BookstoreApp)

    def Interactions_homepage(self):
        return self.driver.find_element(*HomePageCls.Interactions)

    