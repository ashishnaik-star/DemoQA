import inspect

from selenium.webdriver.common.by import By

from Utilities.BaseClass import Baseclass


class elements_page:
    Expand_elements = (By.XPATH, "(//div[@class='header-right'])[1]")
    Dynamic_properties = (By.XPATH, "// span[contains(text(), 'Dynamic Properties')]")
    Ele_text_box = (By.XPATH, "// span[contains(text(), 'Text Box')]")
    Ele_check_box = (By.XPATH, "// span[contains(text(), 'Check Box')]")
    Ele_radio_button = (By.XPATH, "// span[contains(text(), 'Radio Button')]")
    Ele_web_tables = (By.XPATH, "// span[contains(text(), 'Web Tables')]")
    Ele_buttons = (By.XPATH, "// span[contains(text(), 'Buttons')]")
    Ele_Links = (By.XPATH, "// span[contains(text(), 'Links')]")
    Ele_broken_links = (By.XPATH, "// span[contains(text(), 'Broken Links - Images')]")
    Ele_Upload_download = (By.XPATH, "// span[contains(text(), 'Upload and Download')]")
    Ele_Dynamic_props = (By.XPATH, "// span[contains(text(), 'Dynamic Properties')]")
    Textbox_username = (By.CSS_SELECTOR, "#userName")
    Textbox_email = (By.CSS_SELECTOR, "#userEmail")
    Textbox_current_address = (By.CSS_SELECTOR, "#currentAddress")
    Textbox_permanent_address = (By.CSS_SELECTOR, "#permanentAddress")
    Textbox_submit = (By.CSS_SELECTOR, "#submit")
    Checkbox_tick = (By.XPATH, "//label[@for='tree-node-home']")
    Checkbox_tick_Desktop = (By.XPATH, "//label[@for='tree-node-desktop']")
    Checkbox_tick_Documents = (By.XPATH, "//label[@for='tree-node-notes']")
    Checkbox_tick_Commands = (By.XPATH, "//label[@for='tree-node-commands']")
    Checkbox_grab_path = (By.CSS_SELECTOR, "#result")
    Checkbox_expand_home = (By.XPATH, "//label[@for='tree-node-home']/parent::span/button")
    Checkbox_expand_desktop = (By.XPATH, "//label[@for='tree-node-desktop']/parent::span/button")
    Radio_button_yes = (By.CSS_SELECTOR, "label[for='yesRadio']")
    Radio_button_text_yes = (By.XPATH, "//span[contains(text(),'Yes')]")
    Radio_button_text_impressive = (By.XPATH, "// span[contains(text(), 'Impressive')]")
    Radio_button_impressive = (By.CSS_SELECTOR, "label[for ='impressiveRadio']")
    Radio_button_No = (By.CSS_SELECTOR, ".custom-control-input.disabled")
    Web_tables_add = (By.CSS_SELECTOR, "#addNewRecordButton")
    Web_tables_fname =(By.CSS_SELECTOR, "#firstName")
    Web_tables_lname =(By.CSS_SELECTOR, "#lastName")
    Web_tables_email = (By.CSS_SELECTOR, "#userEmail")
    Web_tables_age = (By.CSS_SELECTOR, "#age")
    Web_tables_salary = (By.CSS_SELECTOR, "#salary")
    Web_tables_department = (By.CSS_SELECTOR, "#department")
    Web_tables_reg_submit = (By.CSS_SELECTOR, "#submit")
    Web_tables_searchbox = (By.CSS_SELECTOR, "input[id = 'searchBox'][type = 'text']")

    def __init__(self, driver):
        self.driver = driver

    def click_elements_expand(self):
        self.driver.find_element(*elements_page.Expand_elements).click()

    def click_elements_textbox(self):
        self.driver.find_element(*elements_page.Ele_text_box).click()

    def fill_textbox_details(self, name, email, curraddr, permaddr):
        self.driver.find_element(*elements_page.Textbox_username).send_keys(name)
        self.driver.find_element(*elements_page.Textbox_email).send_keys(email)
        self.driver.find_element(*elements_page.Textbox_current_address).send_keys(curraddr)
        self.driver.find_element(*elements_page.Textbox_permanent_address).send_keys(permaddr)

    def click_textbox_submit(self):
        self.driver.find_element(*elements_page.Textbox_submit).click()

    def get_output_textbox(self):
        output_List = []
        for i in range(1, 5):
            output_List.append(self.driver.find_element(By.XPATH, f"//div[@class='border col-md-12 col-sm-12']/p[{i}]").text)
            print(output_List)
        return output_List

    def click_elements_checkbox(self):
        self.driver.find_element(*elements_page.Ele_check_box).click()

    def select_checkbox(self):
        self.driver.find_element(*elements_page.Checkbox_tick).click()

    def grab_root_path(self):
        return self.driver.find_element(*elements_page.Checkbox_grab_path).text

    def expand_root_path(self):
        return self.driver.find_element(*elements_page.Checkbox_expand_home).click()

    def expand_root_desktop(self):
        return self.driver.find_element(*elements_page.Checkbox_expand_desktop).click()

    def collapse_root_notes(self):
        return self.driver.find_element(*elements_page.Checkbox_tick_Documents).click()

    def collapse_root_commands(self):
        return self.driver.find_element(*elements_page.Checkbox_tick_Commands).click()

    def click_elements_radiobox(self):
        return self.driver.find_element(*elements_page.Ele_radio_button).click()

    def Select_radio_button_yes(self):
        return self.driver.find_element(*elements_page.Radio_button_yes).click()

    def get_radio_button_result(self):
        return self.driver.find_element(*elements_page.Radio_button_text_yes).text

    def Select_radio_button_impressive(self):
        return self.driver.find_element(*elements_page.Radio_button_impressive).click()

    def get_radio_button_result_impressive(self):
        return self.driver.find_element(*elements_page.Radio_button_text_impressive).text

    def Select_radio_button_no(self):
        return self.driver.find_element(*elements_page.Radio_button_No).is_enabled()

    def click_web_tables(self):
        return self.driver.find_element(*elements_page.Ele_web_tables).click()

    def select_web_tables_add(self):
        return self.driver.find_element(*elements_page.Web_tables_add).click()

    def enter_web_tables_fname(self):
        self.driver.find_element(*elements_page.Web_tables_fname).clear()
        return self.driver.find_element(*elements_page.Web_tables_fname)

    def enter_web_tables_lname(self):
        self.driver.find_element(*elements_page.Web_tables_lname).clear()
        return self.driver.find_element(*elements_page.Web_tables_lname)

    def enter_web_tables_email(self):
        self.driver.find_element(*elements_page.Web_tables_email).clear()
        return self.driver.find_element(*elements_page.Web_tables_email)

    def enter_web_tables_age(self):
        self.driver.find_element(*elements_page.Web_tables_age).clear()
        return self.driver.find_element(*elements_page.Web_tables_age)

    def enter_web_tables_salary(self):
        self.driver.find_element(*elements_page.Web_tables_salary).clear()
        return self.driver.find_element(*elements_page.Web_tables_salary)

    def enter_web_tables_department(self):
        self.driver.find_element(*elements_page.Web_tables_department).clear()
        return self.driver.find_element(*elements_page.Web_tables_department)

    def submit_registration_form(self):
        return self.driver.find_element(*elements_page.Web_tables_reg_submit).click()

    def delete_web_table_row(self, i):
        Web_tables_delete_row = (By.XPATH, f"//div[@class='rt-tbody']/div[{i}]/div/div[7]/div/span[2]")
        return self.driver.find_element(*Web_tables_delete_row).click()

    def edit_web_table_row(self, i):
        Web_tables_edit_row = (By.XPATH, f"//div[@class='rt-tbody']/div[{i}]/div/div[7]/div/span[1]")
        return self.driver.find_element(*Web_tables_edit_row).click()

    def web_table_searchbox(self):
        self.driver.find_element(*elements_page.Web_tables_searchbox).clear()
        return self.driver.find_element(*elements_page.Web_tables_searchbox)










































