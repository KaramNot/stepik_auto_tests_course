from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    new_window = browser.window_handles[1]  # ищем новое отрывшееся окно их два
    browser.switch_to.window(new_window)   # переключаемся для работы во втором окне браузера
    x_element = browser.find_element(By.XPATH, '//span[@id="input_value"]')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys(y)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

