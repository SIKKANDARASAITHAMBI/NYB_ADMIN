from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
# parent_window = driver.current_window_handle
# driver.find_element(By.LINK_TEXT, "Open a popup window").click()
# windows = driver.window_handles
# for window in windows:
#     if window.title().__eq__("New Window"):
#         new_window_text = driver.find_element(By.XPATH, "/html/body/div/h3").text
#         print(new_window_text)
#         driver.close()
#         break
# driver.switch_to.window(parent_window)

# all = driver.find_elements(By.XPATH, "//table[@id='table1']//tbody//td")
# count =len(all)
# b = []
#
# for index in range (count):
#     get_text= all[index].text
#     b.append(get_text)
#
# print(b)

dd = driver.find_element(By.XPATH, "//*[@class='dropbtn']")
dd.click()
wait = WebDriverWait(driver,30)
flipkart_option = wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT,"Flipkart")))
flipkart_option.click()




