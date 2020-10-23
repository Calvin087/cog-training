import unittest
from selenium import webdriver
from pages.training_page_object import TrainingGroundPage
from pages.trial_page import TrialPage

class TheTest(unittest.TestCase):
    # Test Set up

    # Trial Page
    def test_something(self):
        browser = webdriver.Chrome()
        trial_page = TrialPage(driver=browser)
        trial_page.go()
        trial_page.stone_input.input_text('rock')
        trial_page.stone_button.click()

        # input('continue?')
    def test_something_else(self):
        # Training Page
        browser = webdriver.Chrome()
        training_page = TrainingGroundPage(driver=browser)
        training_page.go()
        assert training_page.button1.text == 'Button12', 'problems on button1'

        # input('continue?')

        browser.quit()

if __name__ == '__main__':
    unittest.main()