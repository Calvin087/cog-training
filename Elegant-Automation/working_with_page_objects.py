# Page objects are just Classes?

class TrainingGroundPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://techstepacademy.com/training-ground'

    def go(self):
        self.driver.get(self.url)

    def type_into_input(self, text):
        inputs = self.driver.find_element_by_id('ipt1')
        inputs.clear()
        inputs.send_keys(text)
        return None

    def get_input_text(self):
        inputs = self.driver.find_element_by_id('ipt1')
        elem_text = inputs.get_attribute('value')
        return elem_text
        
    
    def click_button_1(self):
        button1 = self.driver.find_element_by_id('b1')
        button1.click()
        return None

# Tests
from selenium import webdriver

browser = webdriver.Chrome()

# Variables to reuse
test_value = 'Test worked bro!' 

# using the class to build a new object, passing the driver, named argument
training_page = TrainingGroundPage(driver=browser)

# Now we should have a new page that I can call methods on --------

# Actions to take
training_page.go()
training_page.type_into_input(test_value)
# training_page.click_button_1() <-- the alert breaks this but course doesn't address the fix

# Checks to make
text_from_input = training_page.get_input_text()
assert text_from_input == test_value, f"Test failed message ({test_value})"
print('test passed')