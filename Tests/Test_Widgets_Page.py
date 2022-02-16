import time
import pdb

from PageObjects.Homepage import HomePageCls
from PageObjects.Practise_form import Practise_form_po
from PageObjects.Widgets_page import widgets_form_po
from Utilities.BaseClass import Baseclass


class Test_widgets(Baseclass):

    def test_afw_browser_windows(self):
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



















