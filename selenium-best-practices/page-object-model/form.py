from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.form_target import FormTarget


class Form:
    def __init__(self, driver) -> None:
        self.driver = driver

    def open(self) -> None:
        self.driver.get('https://www.selenium.dev/selenium/web/web-form.html')

    def get_title(self) -> str:
        return self.driver.title

    def input_text(self, text: str) -> None:
        elem = self.driver.find_element(By.ID, 'my-text-id')
        elem.send_keys(text)

    def input_password(self, password: str) -> None:
        elem = self.driver.find_element(By.NAME, 'my-password')
        elem.send_keys(password)

    def select_from_dropdown(self, value: str) -> None:
        elem = Select(self.driver.find_element(By.NAME, 'my-select'))
        elem.select_by_value(value)

    def input_date(self, date: str) -> None:
        elem = self.driver.find_element(By.XPATH, '//input[@name="my-date"]')
        elem.send_keys(date)

    def submit(self) -> FormTarget:
        elem = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
        elem.click()

        # 等待进入已提交页面
        WebDriverWait(self.driver, 10).until(EC.title_is('Web form - target page'))

        # 返回 FormTarget 对象
        return FormTarget(self.driver)
