import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Datas.User_common_datas import Dataset


@pytest.fixture(scope='class')
def init_browser(request):
    browsr_name = request.config.getoption("browser_name")
    if browsr_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("ignore-certificate-errors")
        s = Service(".\\DriverLocation\\chromedriver.exe")
        driver = webdriver.Chrome(service=s, options=chrome_options)
    elif browsr_name == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.accept_untrusted_certs = True
        fal = Service(".\\DriverLocation\\geckodriver.exe")
        driver = webdriver.Firefox(service=fal, options=firefox_options)
        driver.maximize_window()
        print("Please enter among the list of browser \n1.firefox\n2.chrome \noptions for browse")
    driver.implicitly_wait(10)
    request.cls.driver = driver
    driver.get(Dataset.URL)
    driver.set_page_load_timeout(20)
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")