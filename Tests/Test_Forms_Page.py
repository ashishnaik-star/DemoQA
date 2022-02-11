import os
from PageObjects.Homepage import HomePageCls
from PageObjects.Practise_form import Practise_form_po
from Utilities.BaseClass import Baseclass
from config import PROJECT_PATH


class Test_forms(Baseclass):

    def test_practise_form(self):
        Fp = HomePageCls(self.driver)
        Fp.Forms_homepage().click()
        Fp1 = Practise_form_po(self.driver)
        Fp1.click_practise_form()
        Fp1.click_first_name().send_keys("Ashish")
        Fp1.click_last_name().send_keys("Naik")
        Fp1.click_email_id().send_keys("ashishnaik@zmail.com")
        Fp1.click_gender_radio_female()
        Fp1.click_user_number().send_keys("8127272712")
        Fp1.click_current_address().send_keys("Test Address %$!@@!^%@ Line 1")
        Fp1.click_subject_form_Maths()
        Fp1.click_hobbies_checkbox_reading()
        Fp1.click_upload_image().send_keys(os.path.join(PROJECT_PATH,"Datas\\pexels-pixabay-65894.jpg"))
        self.Explicit_wait_by_clickable(Fp1.select_state)
        self.scroll_vertical(800)
        Fp1.click_state()
        self.dropdown_byvalue("Uttar Pradesh")
        Fp1.click_city()
        self.dropdown_byvalue("Agra")
        self.date_picker_by_value(1, 1, 1995, Fp1.date_picker_month, Fp1.date_picker_year)
        self.driver.get_screenshot_as_file(".\\Screenshots\\Forms_entries.png")
        Fp1.click_on_submit()
        student_name = Fp1.get_student_name()
        assert student_name == "Ashish Naik"
        self.driver.get_screenshot_as_file(".\\Screenshots\\Forms_entries_submit.png")
        Fp1.click_close_submitform()


















