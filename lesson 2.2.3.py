from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    link2 = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link2)
    x = browser.find_element(By.XPATH, '//span[@id="num1"]')
    x = x.text
    y = browser.find_element(By.XPATH, '//span[@id="num2"]')
    y = y.text
    z = int(x)+int(y)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(z))
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
