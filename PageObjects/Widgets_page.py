import pdb
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class widgets_form_po:
    expand_widgets = (By.XPATH, "(//div[@class='header-right'])[4]")
    accordian_select = (By.XPATH, "//span[text()='Accordian']")
    auto_complete_select = (By.XPATH, "//span[text()='Auto Complete']")
    date_picker_select = (By.XPATH, "//span[text()='Date Picker']")
    slider_menu_click = (By.XPATH, "// span[text() = 'Slider']")
    progress_bar_menu = (By.XPATH, "//span[text()='Progress Bar']")
    widgets_menu_tabs = (By.XPATH, "//span[text()='Tabs']")
    widgets_tools_tips = (By.XPATH, "//span[text()='Tool Tips']")
    widgets_menu = (By.XPATH, "//span[text()='Menu']")
    select_menu_click = (By.XPATH, "//span[text()='Select Menu']")
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
    slider_pointer = (By.CSS_SELECTOR, ".range-slider.range-slider--primary")
    start_stop_button = (By.CSS_SELECTOR, "#startStopButton")
    progress_bar_complete = (By.CSS_SELECTOR, ".progress-bar.bg-success")
    tabs_what_text = (By.CSS_SELECTOR, "#demo-tabpane-what")
    tabs_origin_switch = (By.CSS_SELECTOR, "#demo-tab-origin")
    tabs_origin_text = (By.CSS_SELECTOR, "#demo-tabpane-origin")
    tabs_use_switch = (By.CSS_SELECTOR, "#demo-tab-use")
    tabs_use_text = (By.CSS_SELECTOR, "#demo-tabpane-use")
    hover_me_button = (By.CSS_SELECTOR, "#toolTipButton")
    hover_me_text_box = (By.CSS_SELECTOR, "#toolTipTextField")
    hover_main_item = (By.XPATH, "//a[text()='Main Item 1']")
    hover_main_item2 = (By.XPATH, "//a[text()='Main Item 2']")
    hover_main_item2_sub_list = (By.XPATH, "//a[text()='SUB SUB LIST »']")
    hover_main_item3 = (By.XPATH, "//a[text()='Main Item 3']")
    click_select_value = (By.CSS_SELECTOR, "#withOptGroup")
    click_select_one_value = (By.CSS_SELECTOR, "#selectOne")
    click_select_old_menu = (By.CSS_SELECTOR, "#oldSelectMenu")
    click_multi_select_dropdown = (By.XPATH, "//p/b[text()='Multiselect drop down']//parent::p/following-sibling::div")
    select_cars_dropdown = (By.CSS_SELECTOR, "#cars")

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

    def click_slider_from_right_menu(self):
        self.driver.find_element(*widgets_form_po.slider_menu_click).click()

    def slider_move(self, xpos):
        element = self.driver.find_element(*widgets_form_po.slider_pointer)
        ActionChains(self.driver).drag_and_drop_by_offset(element, xpos, 0).perform()

    def progress_bar_menu_click(self):
        self.driver.find_element(*widgets_form_po.progress_bar_menu).click()

    def start_stop_button_click(self):
        self.driver.find_element(*widgets_form_po.start_stop_button).click()

    def click_menu_tab(self):
        self.driver.find_element(*widgets_form_po.widgets_menu_tabs).click()

    def fetch_tabs_what_text(self):
        return self.driver.find_element(*widgets_form_po.tabs_what_text).text

    def switch_tabs_origin(self):
        self.driver.find_element(*widgets_form_po.tabs_origin_switch).click()

    def fetch_tabs_origin_text(self):
        return self.driver.find_element(*widgets_form_po.tabs_origin_text).text

    def switch_tabs_use(self):
        self.driver.find_element(*widgets_form_po.tabs_use_switch).click()

    def fetch_tabs_use_text(self):
        return self.driver.find_element(*widgets_form_po.tabs_use_text).text

    def click_widgets_tool_tips(self):
        self.driver.find_element(*widgets_form_po.widgets_tools_tips).click()

    def hover_over_button(self):
        Ele = self.driver.find_element(*widgets_form_po.hover_me_button)
        ActionChains(self.driver).move_to_element(Ele).perform()

    def hover_over_text_box(self):
        Ele = self.driver.find_element(*widgets_form_po.hover_me_text_box)
        ActionChains(self.driver).move_to_element(Ele).perform()

    def click_widgets_menu(self):
        self.driver.find_element(*widgets_form_po.widgets_menu).click()

    def hover_main_item_tab(self):
        Ele1 = self.driver.find_element(*widgets_form_po.hover_main_item)
        ActionChains(self.driver).move_to_element(Ele1).perform()

    def hover_main_item2_tab(self):
        Ele2 = self.driver.find_element(*widgets_form_po.hover_main_item2)
        ActionChains(self.driver).move_to_element(Ele2).perform()

    def hover_main_item2_sub_tab(self):
        Ele3 = self.driver.find_element(*widgets_form_po.hover_main_item2_sub_list)
        ActionChains(self.driver).move_to_element(Ele3).perform()

    def hover_main_item3_tab(self):
        Ele4 = self.driver.find_element(*widgets_form_po.hover_main_item3)
        ActionChains(self.driver).move_to_element(Ele4).perform()

    def click_select_menu(self):
        self.driver.find_element(*widgets_form_po.select_menu_click).click()

    def select_value_dropdown_input(self, text):
        self.driver.find_element(*widgets_form_po.click_select_value).click()
        ActionChains(self.driver).send_keys(text).send_keys(Keys.ENTER).perform()

    def select_one_dropdown_input(self, text):
        self.driver.find_element(*widgets_form_po.click_select_one_value).click()
        ActionChains(self.driver).send_keys(text).send_keys(Keys.ENTER).perform()

    def select_multi_input_dropdown(self, *param1):
        Act = ActionChains(self.driver)
        for parm in param1:
            self.driver.find_element(*widgets_form_po.click_multi_select_dropdown).click()
            Act.send_keys(parm).perform()
            time.sleep(1)
            Act.send_keys(Keys.ENTER).perform()






























    
