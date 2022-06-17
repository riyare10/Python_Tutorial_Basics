import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager


@pytest.fixture(scope='class')
def init_chrome_browser(request):
    s=Service(ChromeDriverManager().install())
    chrome_driver=webdriver.Chrome(service=s)
    request.cls.driver=chrome_driver
    yield
    chrome_driver.close()

@pytest.fixture(scope='class')
def init_ff_driver(request):
    s=Service(executable_path="D:\\SeleniumDrivers\\gecko31\\geckodriver.exe")
    ff_driver=webdriver.Firefox(service=s)
    request.cls.driver=ff_driver
    yield
    ff_driver.close()



@pytest.mark.usefixtures("init_chrome_browser")
class Test_Base_Chrome():
    pass
class Test_Chrome(Test_Base_Chrome):

    def test_verifyTitle(self):
        self.driver.get("http://www.rediff.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        assert self.driver.title=="Rediff.com: News | Rediffmail | Stock Quotes | Shopping"

@pytest.mark.usefixtures("init_ff_driver")
class Test_Base_Firefox():
    pass

class Test_Firefox(Test_Base_Firefox):

    def test_verifyTitle(self):
        self.driver.get("http://www.rediff.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        assert self.driver.title == "Rediff.com: News | Rediffmail | Stock Quotes | Shopping"