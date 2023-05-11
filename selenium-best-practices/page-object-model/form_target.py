from selenium.webdriver.common.by import By


class FormTarget:
    def __init__(self, driver) -> None:
        self.driver = driver

    def get_message_text(self) -> str:
        return self.driver.find_element(By.ID, 'message').text
