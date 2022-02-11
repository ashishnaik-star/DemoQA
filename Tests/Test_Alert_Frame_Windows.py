from PageObjects.Alerts_frame_windows_page import afw_po
from PageObjects.Homepage import HomePageCls
from Utilities.BaseClass import Baseclass


class Test_afw(Baseclass):

    def test_afw(self):
        Ep = HomePageCls(self.driver)
        Ep.AFW_homepage().click()
        Afw1 = afw_po(self.driver)
        Afw1.browser_windows_click()




