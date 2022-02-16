from selenium.webdriver.common.by import By


class afw_po:
    expand_afw = (By.XPATH, "(//div[@class='header-right'])[3]")
    browser_windows = (By.XPATH, "//span[text()='Browser Windows']")
    alert_windows = (By.XPATH, "//span[text()='Alerts']")
    nested_frames_windows = (By.XPATH, "//span[text()='Nested Frames']")
    modal_dialogs_window = (By.XPATH, "//span[text()='Modal Dialogs']")
    new_tab_click = (By.CSS_SELECTOR, "#tabButton")
    new_tab_sample_msg = (By.CSS_SELECTOR, "#sampleHeading")
    new_window_click = (By.CSS_SELECTOR, "#windowButton")
    new_window_message_click = (By.CSS_SELECTOR, "#messageWindowButton")
    new_window_text_msg = (By.XPATH, "/html/body")
    alert_generate = (By.CSS_SELECTOR, "#alertButton")
    alert_timer_generate = (By.CSS_SELECTOR, "#timerAlertButton")
    double_option_alert = (By.CSS_SELECTOR, "#confirmButton")
    confirm_result_text = (By.CSS_SELECTOR, "#confirmResult")
    prompt_alert = (By.CSS_SELECTOR, "#promtButton")
    frame_window = (By.XPATH, "//span[text()='Frames']")
    frame_one_locator_css = (By.CSS_SELECTOR, "#frame1")
    frame_one_contents = (By.CSS_SELECTOR, "#sampleHeading")
    frame_two_locator_css = (By.CSS_SELECTOR, "#frame2")
    small_modal = (By.CSS_SELECTOR, "#showSmallModal")
    large_modal = (By.CSS_SELECTOR, "#showLargeModal")
    modal_body_text = (By.CSS_SELECTOR, ".modal-body")
    close_small_modal = (By.CSS_SELECTOR, "#closeSmallModal")
    close_large_modal = (By.CSS_SELECTOR, "#closeLargeModal")

    def __init__(self, driver):
        self.driver = driver

    def click_expand_afw(self):
        self.driver.find_element(*afw_po.expand_afw).click()

    def browser_windows_click(self):
        self.driver.find_element(*afw_po.browser_windows).click()

    def click_new_tab(self):
        self.driver.find_element(*afw_po.new_tab_click).click()

    def fetch_new_tab_sample_message(self):
        return self.driver.find_element(*afw_po.new_tab_sample_msg).text

    def click_new_window(self):
        self.driver.find_element(*afw_po.new_window_click).click()

    def click_new_window_message(self):
        self.driver.find_element(*afw_po.new_window_message_click).click()

    def fetch_new_tab_text_message(self):
        return self.driver.find_element(*afw_po.new_window_text_msg).text

    def click_alerts_option(self):
        return self.driver.find_element(*afw_po.alert_windows).click()

    def click_alerts_generate(self):
        return self.driver.find_element(*afw_po.alert_generate).click()

    def click_timer_alert(self):
        return self.driver.find_element(*afw_po.alert_timer_generate).click()

    def click_double_op_alert(self):
        return self.driver.find_element(*afw_po.double_option_alert).click()

    def fetch_confirm_result_text(self):
        return self.driver.find_element(*afw_po.confirm_result_text).text

    def click_prompt_alert(self):
        return self.driver.find_element(*afw_po.prompt_alert).click()

    def click_frame_window(self):
        return self.driver.find_element(*afw_po.frame_window).click()

    def fetch_frame_one_contents(self):
        return self.driver.find_element(*afw_po.frame_one_contents).text

    def frame_one_locator(self):
        return self.driver.find_element(*afw_po.frame_one_locator_css)

    def click_nested_frame_window(self):
        return self.driver.find_element(*afw_po.nested_frames_windows).click()

    def click_modal_dialog_window(self):
        self.driver.find_element(*afw_po.modal_dialogs_window).click()

    def click_small_modal(self):
        self.driver.find_element(*afw_po.small_modal).click()

    def click_large_modal(self):
        self.driver.find_element(*afw_po.large_modal).click()

    def fetch_modal_body(self):
        return self.driver.find_element(*afw_po.modal_body_text).text

    def click_close_small_modal(self):
        self.driver.find_element(*afw_po.close_small_modal).click()

    def click_close_large_modal(self):
        self.driver.find_element(*afw_po.close_large_modal).click()


































