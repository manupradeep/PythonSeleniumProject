from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

#driver.find_element_by_name("name").send_keys("Rahul")
driver.find_element_by_xpath("(//input[@name='name'])[1]").send_keys("Manoj")
driver.find_element_by_name("email").send_keys("Kumar")

driver.find_element_by_id("exampleCheck1").click()

#select class provide the methods to handle the options in dropdown
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

driver.find_element_by_xpath("//input[@type='submit']").click()

message = driver.find_element_by_class_name("alert-success").text
print(message)
assert "success" in message