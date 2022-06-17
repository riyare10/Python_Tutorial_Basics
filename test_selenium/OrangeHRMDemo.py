from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=None
def setup_module(module):
    global driver
    s=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=s)
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    driver.implicitly_wait(30)

def teardown_module(module):
    driver.close()

def test_verifyTitle():
    actual_title= driver.title
    assert actual_title=="OrangeHRM"

def test_verifyUrl():
    actual_url=driver.current_url
    assert actual_url=="https://opensource-demo.orangehrmlive.com/"

def test_verifyusernameandPassword():
    actual_up=driver.find_element(By.XPATH,"//span[text()='( Username : Admin | Password : admin123 )']").text
    assert actual_up=="( Username : Admin | Password : admin123 )"

def test_verifyloginPanelHeading():
   actual_loginheading= driver.find_element(By.ID,"logInPanelHeading").text
   assert actual_loginheading=="LOGIN Panel"

def test_verifyLogin():
    driver.find_element(By.ID,"txtUsername").send_keys("Admin")
    driver.find_element(By.ID,"txtPassword").send_keys("admin123")
    driver.find_element(By.ID,"btnLogin").click()
    actual_logintext=driver.find_element(By.ID,"welcome").text
    expected_logintext="Welcome"
    assert actual_logintext==expected_logintext

