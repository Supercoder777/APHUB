import pytest
from selenium import webdriver
import time

from selenium.webdriver.common import service
from selenium.webdriver.common.service import Service


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")

@pytest.fixture(scope="class")
def setup(request, service_obj=service):
    global driver
    browser_name=request.config.getoption("browser_name")
    if browser_name == "chrome":
        #driver = driver = webdriver.Chrome(executable_path="/Applications/Utilities/chromedriver")
        service_obj = Service("/Applications/chromedriver")
        driver = webdriver.chrome(service=service_obj)
    elif browser_name == "firefox":
        #driver = webdriver.Chrome(executable_path="/Applications/Utilities/geckodriver")
        service_obj = Service("/Applications/geckodriver")
        driver = webdriver.Firefox(service=service_obj)

    driver.get("https://hub.knime.com/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()

#the next set of code was copied to help document failed tests by taking screenshots and saving it in the project
#Also, an html report will be generated using this code below.

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)