from selenium import webdriver
import time

try:
    link = 'http://suninjuly.github.io/registration1.html'
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element_by_css_selector('div.first_block div.first_class input.first')
    first_name.send_keys('Anton')
    last_name = browser.find_element_by_css_selector('div.first_block div.second_class input.second')
    last_name.send_keys('Ivanov')
    email = browser.find_element_by_css_selector('div.first_block div.third_class input.third')
    email.send_keys('email@email.ru')
    button_submit = browser.find_element_by_css_selector('button.btn')
    button_submit.click()
    
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name('h1')
    welcome_text = welcome_text_elt.text
    assert 'Congratulations! You have successfully registered!' == welcome_text

finally:
    time.sleep(30)
    browser.quit()

