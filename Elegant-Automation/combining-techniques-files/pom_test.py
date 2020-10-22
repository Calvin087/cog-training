from selenium import webdriver
from pages.training_page_object import TrainingGroundPage
from pages.trial_page import TrialPage

# Test Set up
browser = webdriver.Chrome()

# Trial Page
trial_page = TrialPage(driver=browser)
trial_page.go()
trial_page.stone_input.input_text('rock')
trial_page.stone_button.click()

input('continue?')

# Training Page
training_page = TrainingGroundPage(driver=browser)
training_page.go()
assert training_page.button1.text == 'Button1', 'problems on button1'

input('continue?')

browser.quit()
