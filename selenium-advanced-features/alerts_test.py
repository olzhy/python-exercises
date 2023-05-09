from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAlerts(TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.addCleanup(self.driver.quit)

    def test_alert(self) -> None:
        # 打开 Alerts 示例页面
        self.driver.get('file:///Users/larry/Desktop/alerts-test.html')

        # 点击超链接 "Click to see an example alert"
        self.driver.find_element(By.LINK_TEXT, 'Click to see an example alert').click()

        # 等待窗口弹出，获取 Alert 信息，点击 OK
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert_message = alert.text
        alert.accept()

        # 断言
        self.assertEqual(alert_message, 'This is an example alert')

    def test_confirm(self) -> None:
        # 打开 Alerts 示例页面
        self.driver.get('file:///Users/larry/Desktop/alerts-test.html')

        # 点击超链接 "Click to see an example confirm"
        self.driver.find_element(By.LINK_TEXT, 'Click to see an example confirm').click()

        # 等待窗口弹出，点击 OK
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert.accept()

        # 获取 `#confirmed` 文本
        confirmed = self.driver.find_element(By.ID, 'confirmed').text

        # 断言
        self.assertEqual(confirmed, 'true')

    def test_prompt(self) -> None:
        # 打开 Alerts 示例页面
        self.driver.get('file:///Users/larry/Desktop/alerts-test.html')

        # 点击超链接 "Click to see an example prompt"
        self.driver.find_element(By.LINK_TEXT, 'Click to see an example prompt').click()

        # 等待窗口弹出，输入信息，点击 OK
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert.send_keys('Football')
        alert.accept()

        # 获取 `#favorite-sport` 文本
        favorite_sport = self.driver.find_element(By.ID, 'favorite-sport').text

        # 断言
        self.assertEqual(favorite_sport, 'Football')
