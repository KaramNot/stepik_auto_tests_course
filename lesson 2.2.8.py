from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Evgeny")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Karamyshev")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("Karamnot@icloud.com")
    
    # загрузка файла:
    element = browser.find_element(By.XPATH, '//input[@accept=".txt"]')
    current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
finally:
    time.sleep(10)
    browser.quit()