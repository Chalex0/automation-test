import unittest
from selenium import webdriver
import time

links = ["http://suninjuly.github.io/registration1.html", "http://suninjuly.github.io/registration2.html"]


class TestForms(unittest.TestCase):
    browser = webdriver.Chrome()

    def test_fill_form(self):
        for link in links:
            self.browser.get(link)
            input1 = self.browser.find_element_by_css_selector('div.first_block input.form-control.first')
            input1.send_keys("Ivan")
            input2 = self.browser.find_element_by_css_selector('div.first_block input.form-control.second')
            input2.send_keys("Petrov")
            input3 = self.browser.find_element_by_css_selector('div.first_block input.form-control.third')
            input3.send_keys("addr@mail.ru")
            self.browser.find_element_by_css_selector("button.btn").click()
            time.sleep(1)
            welcome_text = self.browser.find_element_by_tag_name("h1").text
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                             "{link} {welcome_text} should be equal 'Congratulations! You have successfully"
                             " registered!' ")
            time.sleep(3)

        self.browser.quit()


if __name__ == "__main__":
    unittest.main()

