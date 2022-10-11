from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


def test_registr1():
    try:
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
    # для ожидания прогрузки сервера:
        browser.implicitly_wait(5)
    # для загрузки страницы:
        browser.get(link)
    # для заполнения страницы:
        input1 = browser.find_element(By.XPATH, '//input[@placeholder="Input your first name"]')
        input1.send_keys("Evgeny")
        input2 = browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
        input2.send_keys("Karamyshev")
        input3 = browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
        input3.send_keys("karamnot@icloud.com")
    # для нажатия кнопки:
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
    # для поиска текста:
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text
    finally:
        browser.quit()


def test_registr2():
    try:
        link = " http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
    # для ожидания прогрузки сервера:
        browser.implicitly_wait(5)
    # для загрузки страницы:
        browser.get(link)
    # для заполнения страницы:
        input1 = browser.find_element(By.XPATH, '//input[@placeholder="Input your first name"]')
        input1.send_keys("Evgeny")
        input2 = browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
        input2.send_keys("Karamyshev")
        input3 = browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
        input3.send_keys("karamnot@icloud.com")
    # для нажатия кнопки:
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
    # для поиска текста:
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text
    finally:
        browser.quit()


if __name__ == "__main__":
    pytest.main()
