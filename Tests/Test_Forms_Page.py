from PageObjects.Homepage import HomePageCls
from PageObjects.Practise_form import Practise_form_po
from Utilities.BaseClass import Baseclass


class Test_forms(Baseclass):

    def test_practise_form(self):
        Fp = HomePageCls(self.driver)
        Fp.Forms_homepage()
        # Fp1 = Practise_form_po(self.driver)
        # Fp1.click_practise_form()








