from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
text_input = driver.find_element(By.ID, 'kw')
text_input.send_keys('Selenium' + Keys.RETURN)

# 等待搜索结果展示
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'content_left')))

# 不会抛出异常
first_result_title = driver.find_element(By.XPATH, '//div[@id="content_left"]/div[1]/h3').text
print(first_result_title)

driver.quit()
