import inspect
import time

from PageObjects.Elements_page import elements_page
from PageObjects.Homepage import HomePageCls
from Utilities.BaseClass import Baseclass


class Testelements(Baseclass):

    def test_elements_page_expand(self):
        Hp = HomePageCls(self.driver)
        Hp.Elements_homepage().click()
        Ep = elements_page(self.driver)
        Ep.click_elements_expand()
        Ep.click_elements_expand()
        self.Explicit_wait_by_clickable(Ep.Ele_Dynamic_props)
        self.driver.get_screenshot_as_file(f".\\Screenshots\\elements_{inspect.stack()[0][3]}.png")

    def test_elements_textBox(self):
        Ep = elements_page(self.driver)
        Ep.click_elements_textbox()
        self.driver.get_screenshot_as_file(f".\\Screenshots\\ele_txtbx_{inspect.stack()[0][3]}.png")
        Ep.fill_textbox_details(self.Excel_data_drive("name"), self.Excel_data_drive("Email"),
                                self.Excel_data_drive("Current address"), self.Excel_data_drive("Permanent address"))
        self.driver.get_screenshot_as_file(".\\Screenshots\\ele_filled_details.png")
        Ep.click_textbox_submit()
        OpList = Ep.get_output_textbox()
        assert self.Excel_data_drive("name") in OpList[0]
        assert self.Excel_data_drive("Email") in OpList[1]
        assert self.Excel_data_drive("Current address") in OpList[2]
        assert self.Excel_data_drive("Permanent address") in OpList[3]

    def test_elements_CheckBox(self):
        Ep = elements_page(self.driver)
        Ep.click_elements_checkbox()
        Ep.select_checkbox()
        self.driver.get_screenshot_as_file(f".\\Screenshots\\ele_chkbx_{inspect.stack()[0][3]}.png")
        rootpath = Ep.grab_root_path()
        assert "home" in rootpath
        Ep.expand_root_path()
        self.driver.get_screenshot_as_file(f".\\Screenshots\\ele_checkbox_expand.png")
        Ep.expand_root_desktop()
        Ep.collapse_root_notes()
        Ep.collapse_root_commands()
        assert "Desktop" not in rootpath
        assert "Notes" not in rootpath
        assert "Commands" not in rootpath
        self.driver.get_screenshot_as_file(f".\\Screenshots\\ele_checkbox_collapseDesktop.png")

    def test_elements_radiobutton(self):
        Ep = elements_page(self.driver)
        Ep.click_elements_radiobox()
        Ep.Select_radio_button_yes()
        Radio_res = Ep.get_radio_button_result()
        assert Radio_res == "Yes"
        Ep.Select_radio_button_impressive()
        Radio_res = Ep.get_radio_button_result_impressive()
        assert Radio_res == "Impressive"
        assert not Ep.Select_radio_button_no() == True

    def test_elements_webtables(self):
        Ep = elements_page(self.driver)
        Ep.click_web_tables()
        Ep.select_web_tables_add()
        Ep.enter_web_tables_fname().send_keys("Ashish")
        Ep.enter_web_tables_lname().send_keys("Naik")
        Ep.enter_web_tables_email().send_keys("ashishnaik444@gmail.com")
        Ep.enter_web_tables_age().send_keys("26")
        Ep.enter_web_tables_salary().send_keys("12000")
        Ep.enter_web_tables_department().send_keys("engineering")
        self.driver.get_screenshot_as_file(f".\\Screenshots\\ele_wt_name.png")
        Ep.submit_registration_form()
        self.driver.get_screenshot_as_file(f".\\Screenshots\\ele_wt_newreg_entry.png")
        Ep.delete_web_table_row(2)
        time.sleep(2)
        self.driver.get_screenshot_as_file(f".\\Screenshots\\ele_wt_del_entry.png")
        Ep.edit_web_table_row(1)
        Ep.enter_web_tables_fname().send_keys("Ashok")
        Ep.enter_web_tables_lname().send_keys("kumar")
        Ep.enter_web_tables_email().send_keys("Test44@gmail.com")
        Ep.enter_web_tables_age().send_keys("21")
        Ep.enter_web_tables_salary().send_keys("22000")
        Ep.enter_web_tables_department().send_keys("Accounting")
        self.driver.get_screenshot_as_file(f".\\Screenshots\\ele_wt_edit_entry.png")
        Ep.submit_registration_form()
        Ep.web_table_searchbox().send_keys("Ash")
        time.sleep(3)
        self.driver.get_screenshot_as_file(f".\\Screenshots\\ele_wt_searchbox.png")









        





