from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = " http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    st = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    submit = browser.find_element(By.XPATH, '//button[@id="solve"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    x_element = browser.find_element(By.XPATH, '//span[@id="input_value"]')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys(y)
    submit.click()

finally:
    time.sleep(10)
    browser.quit()