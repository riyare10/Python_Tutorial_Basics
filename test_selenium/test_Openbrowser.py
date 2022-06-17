from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_chrome_Openbrowser():
    s=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=s)
    driver.get('http://www.fb.com')
    driver.maximize_window()
    actual_title=driver.title
    expected_title="Facebook – log in or sign up"
    assert actual_title==expected_title
    driver.close()
