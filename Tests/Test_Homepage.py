import pytest
from PageObjects.Homepage import HomePageCls
from Utilities.BaseClass import Baseclass


class Test_Homepage(Baseclass):

    def test_toolsqa_header(self):
        Homepg = HomePageCls(self.driver)
        Homepg.Heading_refresh().click()
        self.Loggingfunc().info("Page heading Refreshed successfully")
        assert "true"

    def test_elements(self):
        Homepg = HomePageCls(self.driver)
        Homepg.Elements_homepage().click()
        self.driver.get_screenshot_as_file(".\\Screenshots\\elements_Hompage.png")
        self.Loggingfunc().info("Elements clicked and captured screenshots from home page")
        self.driver.back()

    def test_forms(self):
        Homepg = HomePageCls(self.driver)
        Homepg.Forms_homepage().click()
        self.driver.get_screenshot_as_file(".\\Screenshots\\elements_Forms.png")
        self.Loggingfunc().info("Elements clicked and captured screenshots from Forms")
        self.driver.back()

    def test_afw(self):
        Homepg = HomePageCls(self.driver)
        Homepg.AFW_homepage().click()
        self.driver.get_screenshot_as_file(".\\Screenshots\\elements_afw.png")
        self.Loggingfunc().info("Elements clicked and captured screenshots from Alerts frames windows")
        self.driver.back()

    def test_widgets(self):
        Homepg = HomePageCls(self.driver)
        Homepg.Widgets_homepage().click()
        self.driver.get_screenshot_as_file(".\\Screenshots\\elements_widgets.png")
        self.Loggingfunc().info("Elements clicked and captured screenshots from widgets")
        self.driver.back()

    def test_bookstoreapp(self):
        self.Scrolldown(800)
        Homepg = HomePageCls(self.driver)
        Homepg.BookstoreApp_homepage().click()
        self.driver.get_screenshot_as_file(".\\Screenshots\\elements_BookstoreApp.png")
        self.Loggingfunc().info("Elements clicked and captured screenshots from BookstoreApp")
        self.driver.back()

    def test_interactions(self):
        Homepg = HomePageCls(self.driver)
        Homepg.Interactions_homepage().click()
        self.driver.get_screenshot_as_file(".\\Screenshots\\elements_interactions.png")
        self.Loggingfunc().info("Elements clicked and captured screenshots from interactions")
        self.driver.back()




