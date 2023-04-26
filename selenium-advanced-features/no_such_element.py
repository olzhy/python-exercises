from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
text_input = driver.find_element(By.ID, 'kw')
text_input.send_keys('Selenium' + Keys.RETURN)

# 会抛出 NoSuchElementException 异常
first_result_title = driver.find_element(By.XPATH, '//div[@id="content_left"]/div[1]/h3').text
print(first_result_title)

driver.quit()
