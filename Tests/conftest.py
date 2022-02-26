import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from selenium.webdriver.chrome.options import Options
from Datas.User_common_datas import Dataset

driver = None


@pytest.fixture(scope='class')
def init_browser(request):
    global driver
    browsr_name = request.config.getoption("browser_name")
    if browsr_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("ignore-certificate-errors")
        prefs = {'download.default_directory': '.\\Datas'}
        chrome_options.add_experimental_option('prefs', prefs)
        chrome_options.add_extension('.\\Datas\\extension_3_12_0_0.crx')
        caps = DesiredCapabilities().CHROME
        caps["pageLoadStrategy"] = "none"
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        s = ChromeService(executable_path=".\\DriverLocation\\chromedriver.exe")
        driver = webdriver.Chrome(service=s, options=chrome_options, desired_capabilities=caps)
        Wh = driver.window_handles
        time.sleep(8)
        driver.switch_to.window(Wh[0])
        driver.close()
        driver.switch_to.window(Wh[1])
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


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        extra.append(pytest_html.extras.url("https://demoqa.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            report_directory = os.path.dirname(item.config.option.htmlpath)
            file_name = str(int(round(time.time() * 1000))) + ".png"
            # file_name = report.nodeid.replace("::", "_") + ".png"
            destination_file = os.path.join(report_directory, file_name)
            driver.save_screenshot(destination_file)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def pytest_html_report_title(report):
    report.title = "DEMO QA REPORT!"
