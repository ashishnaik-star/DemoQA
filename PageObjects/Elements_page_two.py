from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class elements_page_two:
    Ele_buttons = (By.XPATH, "// span[contains(text(), 'Buttons')]")
    Ele_Links = (By.XPATH, "// span[contains(text(), 'Links')]")
    Ele_broken_links = (By.XPATH, "// span[contains(text(), 'Broken Links - Images')]")
    Ele_Upload_download = (By.XPATH, "// span[contains(text(), 'Upload and Download')]")
    Ele_Dynamic_props = (By.XPATH, "// span[contains(text(), 'Dynamic Properties')]")
    double_click_me = (By.CSS_SELECTOR, "#doubleClickBtn")
    right_click_me = (By.CSS_SELECTOR, "#rightClickBtn")
    click_me = (By.XPATH, "// button[text() = 'Click Me']")
    double_click_message_fetch = (By.CSS_SELECTOR, "#doubleClickMessage")
    right_click_message_fetch = (By.CSS_SELECTOR, "#rightClickMessage")
    dynamic_click_message_fetch = (By.CSS_SELECTOR, "#dynamicClickMessage")
    links_home = (By.LINK_TEXT, "Home")
    dynamic_link = (By.XPATH, "//a[text()='Home'  and @id='dynamicLink']")
    valid_link = (By.XPATH, "// a[text() = 'Click Here for Valid Link']")
    broken_link = (By.XPATH, "// a[text() = 'Click Here for Broken Link']")
    choose_file_upload = (By.CSS_SELECTOR, "#uploadFile")
    click_download_button = (By.XPATH, "//a[text()='Download']")
    enable5_seconds_button = (By.CSS_SELECTOR, "#enableAfter")
    color_change = (By.CSS_SELECTOR, "#colorChange")
    visible5_seconds = (By.CSS_SELECTOR, "#visibleAfter")

    def __init__(self, driver):
        self.driver = driver

    def click_elements_option(self):
        self.driver.find_element(*elements_page_two.Ele_buttons).click()

    def buttons_double_click_me(self):
        Act = ActionChains(self.driver)
        Act.double_click(self.driver.find_element(*elements_page_two.double_click_me)).perform()

    def buttons_right_click_me(self):
        Act = ActionChains(driver=self.driver)
        Act.context_click(self.driver.find_element(*elements_page_two.right_click_me)).perform()

    def buttons_dynamic_click_me(self):
        Act = ActionChains(driver=self.driver)
        Act.click(self.driver.find_element(*elements_page_two.click_me)).perform()

    def double_click_message(self):
        return self.driver.find_element(*elements_page_two.double_click_message_fetch).text

    def right_click_message(self):
        return self.driver.find_element(*elements_page_two.right_click_message_fetch).text

    def dynamic_click_message(self):
        return self.driver.find_element(*elements_page_two.dynamic_click_message_fetch).text

    def click_links_option(self):
        return self.driver.find_element(*elements_page_two.Ele_Links).click()

    def click_links_option(self):
        return self.driver.find_element(*elements_page_two.Ele_Links).click()

    def home_link_click(self):
        return self.driver.find_element(*elements_page_two.links_home).click()

    def dynamic_link_click(self):
        return self.driver.find_element(*elements_page_two.dynamic_link).click()

    def broken_links_click(self):
        return self.driver.find_element(*elements_page_two.Ele_broken_links).click()

    def click_valid_link(self):
        return self.driver.find_element(*elements_page_two.valid_link).click()

    def click_broken_link(self):
        return self.driver.find_element(*elements_page_two.broken_link).click()

    def click_upl_download(self):
        return self.driver.find_element(*elements_page_two.Ele_Upload_download).click()

    def upload_file(self):
        return self.driver.find_element(*elements_page_two.choose_file_upload)

    def click_download(self):
        return self.driver.find_element(*elements_page_two.click_download_button).click()

    def click_dynamic_properties(self):
        return self.driver.find_element(*elements_page_two.Ele_Dynamic_props).click()

    def click_enable5_seconds(self):
        return self.driver.find_element(*elements_page_two.enable5_seconds_button).click()

    def click_color_change(self):
        return self.driver.find_element(*elements_page_two.color_change).click()

    def click_visible5_seconds(self):
        return self.driver.find_element(*elements_page_two.visible5_seconds).click()










































