import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

URL = "https://wiki.python.org/moin/FrontPage"

driver = webdriver.Chrome()
driver.get(URL)
actions = ActionChains(driver)

# find the element
drop_down = driver.find_element(By.XPATH, "//*[@id='sidebar']/div[3]/ul/li[5]/form/div/select")

drop_down.click()

drop_down.send_keys(Keys.ARROW_DOWN)
drop_down.send_keys(Keys.RETURN)

time.sleep(2)
driver.quit()