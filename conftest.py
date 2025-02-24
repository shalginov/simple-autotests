import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="browser name",
        choices=("chrome", "firefox", "yandex")
    )

    parser.addoption(
        "--driver_path",
        default="c:\\Users\\User\\Downloads",
        help="path to driver"
    )

    parser.addoption(
        "--url",
        default="http://192.168.27.17:8081/",
        help="base url"
    )


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    driver_path = request.config.getoption("--driver_path")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "yandex":
        options = webdriver.ChromeOptions()
        options.binary_location = "c:\Program files\Yandex"
        service = Service(executable_path=os.path.join(driver_path, "yandexdriver"))
        driver = webdriver.Chrome(options=options, service=service)
    else:
        raise Exception("Driver not supported")

    driver.maximize_window()

    yield driver

    driver.close()


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")
