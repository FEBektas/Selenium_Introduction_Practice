import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

# drag and drop site URL
URL = "http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html"

# webdriver for Chrome
driver = webdriver.Chrome()
driver.get(URL)
# sets the browser to fullscreen
driver.fullscreen_window()


action_chains = ActionChains(driver)

# source finds. - items that will be dragged into the corrcet target element.

first_source = driver.find_element(By.ID, "box1")
second_source = driver.find_element(By.ID, "box2")
third_source = driver.find_element(By.ID, "box3")
fourth_source = driver.find_element(By.ID, "box4")
fifth_source = driver.find_element(By.ID, "box5")
sixth_source = driver.find_element(By.ID, "box6")
seventh_source = driver.find_element(By.ID, "box7")


# target element. - where the dragged items will be correctly placed into the intended items

first_target = driver.find_element(By.ID, "box101")
second_target = driver.find_element(By.ID, "box102")
third_target = driver.find_element(By.ID, "box103")
fourth_target = driver.find_element(By.ID, "box104")
fifth_target = driver.find_element(By.ID, "box105")
sixth_target = driver.find_element(By.ID, "box106")
seventh_target = driver.find_element(By.ID, "box107")


# interactions. - the action where the source is dragged into the correct target.

action_chains.drag_and_drop(first_source, first_target).perform()
action_chains.drag_and_drop(second_source, second_target).perform()
action_chains.drag_and_drop(third_source, third_target).perform()
action_chains.drag_and_drop(fourth_source, fourth_target).perform()
action_chains.drag_and_drop(fifth_source, fifth_target).perform()
action_chains.drag_and_drop(sixth_source, sixth_target).perform()
action_chains.drag_and_drop(seventh_source, seventh_target).perform()

time.sleep(3)
driver.quit()
