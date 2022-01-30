import inspect
import logging
import pytest
import openpyxl
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("init_browser")
class Baseclass:

    def Loggingfunc(self):
        logname = inspect.stack()[1][3]
        logger = logging.getLogger(logname)
        filehndler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehndler.setFormatter(formatter)
        logger.addHandler(filehndler)
        logger.setLevel(logging.DEBUG)
        return logger

    def Scrolldown(self, y):
        self.driver.execute_script(f"window.scrollTo(0,{y})")

    def Explicit_wait_by_clickable(self, locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.element_to_be_clickable(locator))

    def Excel_data_drive(self, catogary):
        wb = openpyxl.load_workbook(".\\Datas\\Data_set.xlsx")
        sheet1 = wb.active
        if catogary == "name":
            return str(sheet1.cell(row=1, column=2).value)
        elif catogary == "Email":
            return str(sheet1.cell(row=2, column=2).value)
        elif catogary == "Current address":
            return str(sheet1.cell(row=3, column=2).value)
        elif catogary == "Permanent address":
            return str(sheet1.cell(row=4, column=2).value)

