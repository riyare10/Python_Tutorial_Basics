from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_Fb():
    s=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=s)
    driver.get("http://www.fb.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    actual_title=driver.title
    assert actual_title=="Facebook – log in or sign up"
    driver.close()

def test_Google():
    s=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=s)
    driver.get("http://www.google.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    actual_title=driver.title
    assert actual_title=="Google"
    driver.close()

def test_redbus():
    s=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=s)
    driver.get("http://www.redbus.in")
    driver.maximize_window()
    driver.implicitly_wait(30)
    actual_title=driver.title
    assert actual_title=="Book Bus Travels, AC Volvo Bus, rPool & Bus Hire - redBus India"
    driver.close()

def test_rediff():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get("http://www.rediff.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    actual_title=driver.title
    assert actual_title=="Rediff.com: News | Rediffmail | Stock Quotes | Shopping"
    driver.close()

def test_flipkart():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get("http://www.flipkart.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    actual_title = driver.title
    assert actual_title == "Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!"
    driver.close()