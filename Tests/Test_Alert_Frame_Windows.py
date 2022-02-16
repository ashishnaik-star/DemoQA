import inspect
import time
from PageObjects.Alerts_frame_windows_page import afw_po
from PageObjects.Homepage import HomePageCls
from Utilities.BaseClass import Baseclass


class Test_afw(Baseclass):

    def test_afw_browser_windows(self):
        Ep = HomePageCls(self.driver)
        Ep.AFW_homepage().click()
        Afw1 = afw_po(self.driver)
        parent_handle = self.driver.current_window_handle
        Afw1.browser_windows_click()
        Afw1.click_new_tab()
        self.window_change(1)
        self.driver.get_screenshot_as_file(f".\\Screenshots\\new_tab_{inspect.stack()[0][3]}1.png")
        New_tab_text = Afw1.fetch_new_tab_sample_message()
        assert New_tab_text == "This is a sample page"
        self.driver.close()
        self.driver.switch_to.window(parent_handle)
        Afw1.click_new_window()
        self.window_change(1)
        self.driver.get_screenshot_as_file(f".\\Screenshots\\new_window2_{inspect.stack()[0][3]}.png")
        New_tab_text = Afw1.fetch_new_tab_sample_message()
        assert New_tab_text == "This is a sample page"
        self.driver.close()
        self.driver.switch_to.window(parent_handle)
        Afw1.click_new_window_message()
        self.window_change(1)
        New_tab_text = Afw1.fetch_new_tab_text_message()
        assert New_tab_text == "Knowledge increases by sharing but not by saving. Please share this website with your friends and in your organization."
        self.driver.get_screenshot_as_file(f".\\Screenshots\\new_window3_{inspect.stack()[0][3]}.png")
        self.driver.close()
        self.driver.switch_to.window(parent_handle)

    def test_afw_alerts(self):
        Afw2 = afw_po(self.driver)
        Afw2.click_alerts_option()
        Afw2.click_alerts_generate()
        self.driver.switch_to.alert.accept()
        Afw2.click_timer_alert()
        self.wait_for_alert(10)
        self.driver.switch_to.alert.accept()
        Afw2.click_double_op_alert()
        self.driver.switch_to.alert.accept()
        result_text = Afw2.fetch_confirm_result_text()
        assert result_text == "You selected Ok"
        Afw2.click_double_op_alert()
        self.driver.switch_to.alert.dismiss()
        result_text = Afw2.fetch_confirm_result_text()
        assert result_text == "You selected Cancel"
        Afw2.click_prompt_alert()
        self.driver.switch_to.alert.send_keys("Test message")
        self.driver.switch_to.alert.accept()
        Afw2.click_prompt_alert()
        self.driver.switch_to.alert.dismiss()

    def test_afw_frames(self):
        Afw3 = afw_po(self.driver)
        Afw3.click_frame_window()
        self.frame_wait_switch(10, Afw3.frame_one_locator_css)
        time.sleep(1)
        self.Explicit_wait_by_presence(Afw3.frame_one_contents)
        Current_Frame_text = Afw3.fetch_frame_one_contents()
        assert Current_Frame_text == "This is a sample page"
        self.driver.switch_to.parent_frame()
        self.frame_wait_switch(10, Afw3.frame_two_locator_css)
        self.Explicit_wait_by_presence(Afw3.frame_one_contents)
        Current_Frame_text = Afw3.fetch_frame_one_contents()
        assert Current_Frame_text == "This is a sample page"
        self.driver.switch_to.parent_frame()
        Afw3.click_nested_frame_window()
        time.sleep(1)
        self.frame_wait_switch(3, Afw3.frame_one_locator_css)
        Current_Frame_text_two = Afw3.fetch_new_tab_text_message()
        assert Current_Frame_text_two == "Parent frame"
        self.driver.switch_to.frame(0)
        Current_Frame_text_two = Afw3.fetch_new_tab_text_message()
        assert Current_Frame_text_two == "Child Iframe"
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.parent_frame()

    def test_afw_modal_dialogs(self):
        logs = self.Loggingfunc()
        Afw4 = afw_po(self.driver)
        self.scroll_vertical(400)
        Afw4.click_modal_dialog_window()
        Afw4.click_small_modal()
        self.Explicit_wait_by_clickable(Afw4.close_small_modal)
        Modal_small_body_text = Afw4.fetch_modal_body()
        assert Modal_small_body_text == "This is a small modal. It has very less content", logs.info("Record this small modal issue")
        Afw4.click_close_small_modal()
        Afw4.click_large_modal()
        self.Explicit_wait_by_clickable(Afw4.close_large_modal)
        Modal_body_text = Afw4.fetch_modal_body()
        assert "Lorem Ipsum is simply dummy" in Modal_body_text, logs.info("Record this- Large modal issue ")
        Afw4.click_close_large_modal()































































