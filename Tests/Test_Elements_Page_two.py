import inspect
import time
from config import PROJECT_PATH
import os

from PageObjects.Elements_page_two import elements_page_two
from PageObjects.Homepage import HomePageCls
from Utilities.BaseClass import Baseclass


class Testelementstwo(Baseclass):

    def test_elements_buttons(self):
        Hp = HomePageCls(self.driver)
        Hp.Elements_homepage().click()
        Ep2 = elements_page_two(self.driver)
        Ep2.click_elements_option()
        Ep2.buttons_double_click_me()
        Ep2.buttons_right_click_me()
        Ep2.buttons_dynamic_click_me()
        self.driver.get_screenshot_as_file(f".\\Screenshots\\ele_buttons_{inspect.stack()[0][3]}.png")
        assert "You have done a double click" == Ep2.double_click_message()
        assert "You have done a right click" == Ep2.right_click_message()
        assert "You have done a dynamic click" == Ep2.dynamic_click_message()
        Ep2.click_links_option()
        Ep2.home_link_click()
        Ep2.dynamic_link_click()
        self.window_change(2)
        self.driver.get_screenshot_as_file(".\\Screenshots\\ele_buttons_windows.png")
        self.driver.close()
        self.window_change(1)
        self.driver.close()
        self.window_change(0)
        Ep2.broken_links_click()
        Ep2.click_valid_link()
        self.driver.get_screenshot_as_file(".\\Screenshots\\ele_valid_links.png")
        self.driver.back()
        Ep2.click_upl_download()
        Ep2.upload_file().send_keys(os.path.join(PROJECT_PATH,"Datas\\pexels-pixabay-65894.jpg"))
        self.driver.get_screenshot_as_file(".\\Screenshots\\ele_file_upload.png")
        Ep2.click_download()
        self.scroll_vertical(400)
        Ep2.click_dynamic_properties()
        self.Explicit_wait_by_clickable(Ep2.enable5_seconds_button)
        Ep2.click_enable5_seconds()
        Ep2.click_color_change()
        self.Explicit_wait_by_visiblity(Ep2.visible5_seconds)
        Ep2.click_visible5_seconds()
















