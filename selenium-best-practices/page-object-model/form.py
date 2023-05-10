from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Form:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://www.selenium.dev/selenium/web/web-form.html')

    def get_title(self):
        return self.driver.title

    def input_text(self, text: str):
        elem = self.driver.find_element(By.ID, 'my-text-id')
        elem.send_keys(text)

    def input_password(self, password: str):
        elem = self.driver.find_element(By.NAME, 'my-password')
        elem.send_keys(password)

    def select_from_dropdown(self, value: str):
        elem = Select(self.driver.find_element(By.NAME, 'my-select'))
        elem.select_by_value(value)

    def input_date(self, date: str):
        elem = self.driver.find_element(By.XPATH, '//input[@name="my-date"]')
        elem.send_keys(date)

    def submit(self):
        elem = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
        elem.click()

        # 等待进入已提交页面
        WebDriverWait(self.driver, 10).until(EC.title_is('Web form - target page'))
