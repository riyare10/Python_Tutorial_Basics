import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager



@pytest.fixture(scope='class')
def init_chrome_browser(request):
    s = Service(ChromeDriverManager().install())
    chrome_driver = webdriver.Chrome(service=s)
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()


@pytest.fixture(scope='class')
def init_firefox_browser(request):
    s = Service(executable_path=GeckoDriverManager().install())
    firefox_driver = webdriver.Firefox(service=s)
    request.cls.driver = firefox_driver
    yield
    firefox_driver.close()


@pytest.fixture(scope='class')
def init_Opera_browser(request):
    s = Service(executable_path=GeckoDriverManager().install())
    opera_driver = webdriver.Opera(service=s)
    request.cls.driver = opera_driver
    yield
    opera_driver.close()


@pytest.mark.usefixtures('init_chrome_browser')
class Base_Chrome_Test:
    pass


class Test_Fb(Base_Chrome_Test):
    def test_verifytitle(self):
        self.driver.get("http://www.fb.com")
        actual_title = self.driver.title
        assert actual_title == "Facebook – log in or sign up"
