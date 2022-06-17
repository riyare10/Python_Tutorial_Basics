import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='class')
def init_chorme_browser(request):
    s=Service(ChromeDriverManager().install())
    chrome_driver=webdriver.Chrome(service=s)
    request.cls.driver=chrome_driver
    yield
    chrome_driver.close()

@pytest.mark.usefixtures("init_chorme_browser")
class Test_Base_Chrome:
    pass
class Test_chrome_browser(Test_Base_Chrome):
    def test_verifyTitle(self):
        self.driver.get("http://www.fb.com")
        actual_title = self.driver.title
        assert actual_title == "Facebook – log in or sign up"

    def test_verifyUrl(self):
        self.driver.get("http://www.fb.com")
        actual_url = self.driver.current_url
        assert actual_url == "https://www.facebook.com/"
