from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.page_load_strategy = 'eager'  # 'none', 'normal'
driver = webdriver.Chrome(options=options)
driver.get('http://www.baidu.com')
driver.quit()
