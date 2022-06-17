import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service



@pytest.fixture(params=["chrome","firefox"],scope='class')
def init_driver(request):
    if request.param=="chrome":
        s=Service(executable_path="D:\\SeleniumDrivers\\chromedriver_win32\\chromedriver.exe")
        web_driver=webdriver.Chrome(service=s)
    if request.param=="firefox":
        s=Service(executable_path="D:\\SeleniumDrivers\\gecko31\\geckodriver.exe")
        web_driver=webdriver.Firefox(service=s)
    request.cls.driver=web_driver
    yield
    web_driver.close()

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass
class Test_Fb(BaseTest):

    def test_verifyTitle(self):
        self.driver.get("http://www.fb.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        actual_title=self.driver.title
        assert actual_title=="Facebook – log in or sign up"

    def test_verifyUrl(self):
        actual_url=self.driver.current_url
        assert actual_url=="https://www.facebook.com/"