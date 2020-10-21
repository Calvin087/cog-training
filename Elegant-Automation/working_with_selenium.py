from selenium import webdriver

browswer = webdriver.Chrome()

browswer.get('https://techstepacademy.com/training-ground')

input_element = browswer.find_element_by_css_selector('input[id="ipt1"]')

input_element.send_keys('My first automation')

button_element = browswer.find_element_by_css_selector('button[name="butn1"]')

button_element.click()
# brings up modal