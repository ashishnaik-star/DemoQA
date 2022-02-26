import pdb
import random
import time

import pytest
from selenium.webdriver.common.by import By

from PageObjects.Book_Store_App import book_store_application
from PageObjects.Homepage import HomePageCls
from Utilities.BaseClass import Baseclass

invoked = False


class Test_interactions(Baseclass):

    @pytest.mark.parametrize(('username', 'password'), (
            ("ashish", "naik"),
            ("Ashishnaik123", "Ashish44!")))
    def test_login(self, username, password):
        global invoked
        if not invoked:
            Ip = HomePageCls(self.driver)
            time.sleep(5)
            self.Scrolldown(1000)
            Ip.BookstoreApp_homepage().click()
            time.sleep(5)
            self.scroll_vertical(700)
            Bsa1 = book_store_application(self.driver)
            Bsa1.click_login()
            Bsa1.click_new_user()
            Bsa1.input_first_name().send_keys("Ashish")
            Bsa1.input_last_name().send_keys("Naik")
            Bsa1.input_user_name().send_keys("Ashishnaik1234")
            Bsa1.input_password().send_keys("Ashish44!")
            # Bsa1.click_captcha()
            Bsa1.click_back_to_login()
            # self.driver.switch_to.alert.accept()
            # Bsa1.click_go_to_login()
            invoked = True
        self.driver.find_element(*book_store_application.bsa_user_name).clear()
        Bsa2 = book_store_application(self.driver)
        Bsa2.login_username().clear()
        Bsa2.login_username().send_keys(username)
        Bsa2.login_password().clear()
        Bsa2.login_password().send_keys(password)
        # Bsa2.click_login_book_store()
        self.driver.get_screenshot_as_file(f".\\Screenshots\\intrct{str(random.randint(1, 100))}.png")

    def test_book_store(self):
        Bsa3 = book_store_application(self.driver)
        self.scroll_vertical(700)
        Bsa3.click_book_store()
        Bsa3.click_search_box().send_keys("Git")
        self.driver.get_screenshot_as_file(f".\\Screenshots\\books_store_searchbar.png")
        Bsa3.click_search_box().clear()
        self.driver.refresh()
        self.Explicit_wait_by_visiblity(Bsa3.book_learning_js)
        Bsa3.click_book_one()
        self.driver.get_screenshot_as_file(f".\\Screenshots\\books_one.png")

