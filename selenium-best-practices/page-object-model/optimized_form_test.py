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

        # 输入
        form_target_page = form_page.input_text('Selenium') \
            .input_password('Selenium') \
            .select_from_dropdown('2') \
            .input_date('05/10/2023') \
            .submit()

        # 断言
        message = form_target_page.get_message_text()
        self.assertEqual(message, 'Received!')
