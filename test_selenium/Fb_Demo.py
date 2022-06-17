from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=None
def setup(module):
    global driver
    s=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=s)
    driver.get("http://www.fb.com")
    driver.maximize_window()
    driver.implicitly_wait(30)



def test_verifyTitle():
    actual_title=driver.title
    assert actual_title=="Facebook – log in or sign up"

def test_verifyUrl():
    actual_url=driver.current_url
    assert actual_url=="https://www.facebook.com/"

def test_verifyforgotPasswrod():
    actual_forgotpass=driver.find_element(By.LINK_TEXT,"Forgotten password?").text
    assert actual_forgotpass=="Forgotten password?"

def test_verifyLoginbtn():
    actaul_login_text=driver.find_element(By.NAME,"login").text
    assert actaul_login_text=="Log In"

def test_verifyCreateNewAccount():
  actual_createnewacc= driver.find_element(By.XPATH,"//a[@data-testid='open-registration-form-button']").text
  assert actual_createnewacc=="Create New Account"

def tearDown(module):
    driver.close()