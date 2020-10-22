from selenium import webdriver
from pages.training_page_object import TrainingGroundPage

# Test Set up
browser = webdriver.Chrome()

test_value = 'Test worked bro!' 

# TEST
# using the class to build a new object, passing the driver, named argument
training_page = TrainingGroundPage(driver=browser)

# Now we should have a new page that I can call methods on --------

# Actions to take
training_page.go()
assert training_page.button1.text == 'Button1'
training_page.button1.click()

browser.quit()

# training_page.type_into_input(test_value)
# training_page.click_button_1() <-- the alert breaks this but course doesn't address the fix


# Checks to make no longer needed
    # ORIGINAL METHOD --------------
        # text_from_input = training_page.get_input_text()
        # assert text_from_input == test_value, f"Test failed message ({test_value})"
        # print('test passed')
    # ORIGINAL METHOD --------------