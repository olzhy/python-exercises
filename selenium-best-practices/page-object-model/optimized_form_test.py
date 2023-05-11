from unittest import TestCase
from selenium import webdriver
from pages.form import Form


class TestForm(TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.addCleanup(self.driver.quit)

    def test_web_form(self) -> None:
        # 打开表单页面
        form_page = Form(self.driver)
        form_page.open()
        self.assertEqual(form_page.get_title(), 'Web form')

        # Text 输入
        form_page.input_text('Selenium')

        # Password 输入
        form_page.input_password('Selenium')

        # Dropdown 选择
        form_page.select_from_dropdown('2')

        # 日期输入
        form_page.input_date('05/10/2023')

        # 点击 Submit 按钮
        form_target_page = form_page.submit()

        # 断言
        message = form_target_page.get_message_text()
        self.assertEqual(message, 'Received!')
