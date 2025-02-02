from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver=webdriver.Firefox()
driver.get("https://www.facebook.com/signup")
# select = Select(driver.find_element(By.XPATH,"//select[@id='birthday_wrapper']"))
# all_selected_option = select.all_selected_options
# options= select.options

day_select= Select(driver.find_element(By.ID,"day"))
month_select= Select(driver.find_element(By.ID,"month"))
year_select =Select(driver.find_element(By.NAME, "birthday_year"))


default_day = day_select.first_selected_option.text
default_month = month_select.first_selected_option.text
default_year= year_select.first_selected_option.text
DOB= f"{default_day}  {default_month} {default_year}"

print(DOB)


all_select = day_select.all_selected_options
print(all_select[0].text)

