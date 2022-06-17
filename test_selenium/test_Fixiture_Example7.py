import pytest


@pytest.mark.usefixtures("init_driver1")
class BaseTest1:
    pass
class Test_Fb1(BaseTest1):

    def test_verifyTitle_01(self):
        self.driver.get("http://www.fb.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        actual_title=self.driver.title
        assert actual_title=="Facebook – log in or sign up"

    def test_verifyUrl_02(self):
        actual_url=self.driver.current_url
        assert actual_url=="https://www.facebook.com/"