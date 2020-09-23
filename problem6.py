from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome(
    executable_path="C:\drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://bdnews24.com/")


def page_title():
    return driver.title

def click_element():
    return  driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[7]/div[1]/div[1]/div[1]/a[1]').click()
test=page_title();
print(test);

click_element();
test=page_title();
print(test);

driver.quit();