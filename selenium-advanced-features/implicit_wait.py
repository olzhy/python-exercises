from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# 设置隐式等待时间
driver.implicitly_wait(10)

driver.get('https://www.baidu.com/')
text_input = driver.find_element(By.ID, 'kw')
text_input.send_keys('Selenium' + Keys.RETURN)

# 不会抛出异常
first_result_title = driver.find_element(By.XPATH, '//div[@id="content_left"]/div[1]/h3').text
print(first_result_title)

driver.quit()
