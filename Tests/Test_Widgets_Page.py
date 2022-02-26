import time
import pdb

from PageObjects.Homepage import HomePageCls
from PageObjects.Practise_form import Practise_form_po
from PageObjects.Widgets_page import widgets_form_po
from Utilities.BaseClass import Baseclass


class Test_widgets(Baseclass):

    def test_widgets_accordian(self):
        Ep = HomePageCls(self.driver)
        Ep.Widgets_homepage().click()
        Ep1 = widgets_form_po(self.driver)
        Ep1.click_accordian()
        Content_section_one = Ep1.fetch_section_one_content()
        assert "Lorem Ipsum" in Content_section_one
        Ep1.click_expand_section_two()
        time.sleep(2)
        Content_section_two = Ep1.fetch_section_two_content()
        assert "45 BC" in Content_section_two
        Ep1.click_expand_section_three()
        time.sleep(2)
        Content_section_three = Ep1.fetch_section_three_content()
        assert "injected humour" in Content_section_three

    def test_auto_complete_widgets(self):
        Ep2 = widgets_form_po(self.driver)
        Ep2.click_auto_complete()
        Ep2.fill_container_color_names("Red", "Blue", "Green")
        Ep2.fill_container_single("Blue")

    def test_date_picker(self):
        Ep3 = widgets_form_po(self.driver)
        Ep3.click_date_picker()
        Ep3.click_date_picker_date()
        self.date_picker_by_value(1, 1, 1990, Practise_form_po.date_picker_month, Practise_form_po.date_picker_year)
        self.date_picker_by_datetime(12, 'March', 2001, "20:00", Ep3.date_picker_select_date_time)
        self.driver.get_screenshot_as_file(".\\Screenshots\\widget_date_time.png")

    def test_slider(self):
        Ep4 = widgets_form_po(self.driver)
        self.scroll_vertical(400)
        Ep4.click_slider_from_right_menu()
        Ep4.slider_move(30)
        self.driver.get_screenshot_as_file(".\\Screenshots\\widget_slider_movement.png")

    def test_progress_bar(self):
        Ep5 = widgets_form_po(self.driver)
        self.scroll_vertical(400)
        Ep5.progress_bar_menu_click()
        self.scroll_vertical(100)
        Ep5.start_stop_button_click()
        self.Explicit_wait_by_visiblity(Ep5.progress_bar_complete)
        self.driver.get_screenshot_as_file(".\\Screenshots\\widget_progressbar_complete.png")

    def test_widgets_tabs(self):
        Ep6 = widgets_form_po(self.driver)
        self.scroll_vertical(400)
        Ep6.click_menu_tab()
        self.scroll_vertical(100)
        what_text = Ep6.fetch_tabs_what_text()
        assert "PageMaker" in what_text
        Ep6.switch_tabs_origin()
        self.Explicit_wait_by_visiblity(Ep6.tabs_origin_text)
        origin_text = Ep6.fetch_tabs_origin_text()
        assert "The Extremes of Good and Evil" in origin_text
        Ep6.switch_tabs_use()
        self.Explicit_wait_by_visiblity(Ep6.tabs_use_text)
        use_text = Ep6.fetch_tabs_use_text()
        assert "injected humour and the like" in use_text

    def test_widgets_tool_tips(self):
        Ep7 = widgets_form_po(self.driver)
        self.scroll_vertical(400)
        Ep7.click_widgets_tool_tips()
        self.scroll_vertical(100)
        Ep7.hover_over_button()
        time.sleep(1)
        self.driver.get_screenshot_as_file(".\\Screenshots\\widget_hover_over.png")
        Ep7.hover_over_text_box()
        time.sleep(1)
        self.driver.get_screenshot_as_file(".\\Screenshots\\widget_hover_over_textbox.png")

    def test_widgets_menu(self):
        Ep8 = widgets_form_po(self.driver)
        self.scroll_vertical(400)
        Ep8.click_widgets_menu()
        Ep8.hover_main_item_tab()
        self.driver.get_screenshot_as_file(".\\Screenshots\\widget_hover_main_item.png")
        Ep8.hover_main_item2_tab()
        self.driver.get_screenshot_as_file(".\\Screenshots\\widget_hover_main_item2.png")
        Ep8.hover_main_item2_sub_tab()
        self.driver.get_screenshot_as_file(".\\Screenshots\\widget_hover_main_item2_sub.png")
        Ep8.hover_main_item3_tab()
        self.driver.get_screenshot_as_file(".\\Screenshots\\widget_hover_main_item3_sub.png")

    def test_widget_menu(self):
        Ep9 = widgets_form_po(self.driver)
        self.scroll_vertical(400)
        Ep9.click_select_menu()
        Ep9.select_value_dropdown_input("Group 1, option 2")
        Ep9.select_one_dropdown_input("Prof.")
        self.Select_by_dropdown(Ep9.click_select_old_menu, 2)
        Ep9.select_multi_input_dropdown("Green", "Black")
        self.Select_dropdown_visible_text(Ep9.select_cars_dropdown, "Opel")
        self.driver.get_screenshot_as_file(".\\Screenshots\\widget_select_menu_sub.png")







































