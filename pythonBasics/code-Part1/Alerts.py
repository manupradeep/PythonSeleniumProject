from selenium import webdriver
from selenium.webdriver.support.select import Select
user = "Manoj"
driver = webdriver.Chrome(executable_path="chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element_by_css_selector("#name").send_keys(user)
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
alert.accept()
assert user in alertText
driver.quit()

