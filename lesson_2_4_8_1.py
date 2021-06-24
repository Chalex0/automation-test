import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(browser, 30).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )
    browser.find_element_by_id('book').click()
    y = calc(browser.find_element_by_id('input_value').text)
    browser.find_element_by_id('answer').send_keys(y)
    button = browser.find_element_by_id("solve")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
