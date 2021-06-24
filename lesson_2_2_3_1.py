from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


#link = "http://suninjuly.github.io/selects1.html"
link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # Ваш код, который заполняет обязательные поля
    y = int(browser.find_element_by_id('num1').text) + int(browser.find_element_by_id('num2').text)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(y))

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
