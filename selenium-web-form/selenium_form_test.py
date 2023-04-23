from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class TestSeleniumForm(TestCase):
    def setUp(self) -> None:
        # 无痕模式的 Chrome
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')

        self.browser = webdriver.Chrome(options=options)
        self.addCleanup(self.browser.quit)

    def test_web_form(self) -> None:
        # 打开表单页面
        self.browser.get('https://www.selenium.dev/selenium/web/web-form.html')
        self.assertEqual(self.browser.title, 'Web form')

        # Text 输入
        text_input = self.browser.find_element(By.ID, 'my-text-id')
        text_input.send_keys('Selenium')

        # Password 输入
        password = self.browser.find_element(By.NAME, 'my-password')
        password.send_keys('Selenium')

        # Dropdown 选择 Two
        dropdown = Select(self.browser.find_element(By.NAME, 'my-select'))
        dropdown.select_by_value('2')

        # 选择文件
        file_input = self.browser.find_element(By.CSS_SELECTOR, 'input[name="my-file"]')
        file_input.send_keys('/tmp/file.txt')

        # 日期选择
        date_input = self.browser.find_element(By.XPATH, '//input[@name="my-date"]')
        date_input.send_keys('04/21/2023')

        # 点击 Submit 按钮
        submit_button = self.browser.find_element(By.XPATH, '//button[@type="submit"]')
        submit_button.click()

        # 等待进入已提交页面
        WebDriverWait(self.browser, 10).until(EC.title_is('Web form - target page'))

        # 断言
        message = self.browser.find_element(By.ID, 'message').text
        self.assertEqual(message, 'Received!')
