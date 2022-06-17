import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(params=["chrome","firefox","ie"],scope='class')
def init_driver1(request):
    if request.param=="chrome":
        s=Service(executable_path="D:\\SeleniumDrivers\\chromedriver_win32\\chromedriver.exe")
        web_driver=webdriver.Chrome(service=s)
    if request.param=="firefox":
        s=Service(executable_path="D:\\SeleniumDrivers\\gecko31\\geckodriver.exe")
        web_driver=webdriver.Firefox(service=s)
    request.cls.driver=web_driver
    yield
    web_driver.close()