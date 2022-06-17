import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=None
@pytest.fixture(scope='module')
def setup():
    global driver
    s=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=s)
    driver.get("http://www.fb.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield
    driver.close()

@pytest.mark.smoke
def test_verifyTitle(setup):
    actual_title = driver.title
    assert actual_title == "Facebook – log in or sign up"

@pytest.mark.smoke
def test_verifyUrl(setup):
    actual_url = driver.current_url
    assert actual_url == "https://www.facebook.com/"

@pytest.mark.sanity
def test_verifyforgotPasswrod(setup):
    actual_forgotpass = driver.find_element(By.LINK_TEXT, "Forgotten password?").text
    assert actual_forgotpass == "Forgotten password?"

@pytest.mark.regression
def test_verifyLoginbtn(setup):
    actaul_login_text = driver.find_element(By.NAME, "login").text
    assert actaul_login_text == "Log In"

@pytest.mark.smoke
def test_verifyCreateNewAccount(setup):
    actual_createnewacc = driver.find_element(By.XPATH, "//a[@data-testid='open-registration-form-button']").text
    assert actual_createnewacc == "Create New Account"
