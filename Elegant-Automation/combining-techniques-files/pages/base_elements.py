# Wrapping a selenium driver in a class.
# We're going to reuse this base element all the time.

# WAIT IS THE BREAD AND BUTTER OF AUTOMATED TESTING!??

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseElement(object):
    def __init__(self, driver, value, by):
        self.driver = driver
        self.value = value
        self.by = by
        self.locator = (self.by, self.value)

        self.web_element = None
        # this is none until the method sets it, so that we can use the (wait)

        self.find()
        # Calls the method below to find and set
        # the element before anything else happens.

    def find(self):
        
        # Using wait here means we get a wait by default on every action we take for free.
        element = WebDriverWait(
            self.driver, 10).until(EC.visibility_of_element_located(self.locator))
        # Locator is some kind of (tuple)
        # This means that for every find that we implement, we wait, until the element has been found.
        # Making sure that the elemenet is on the page / DOM before moving ahead.
        # Stops us from having sleep times of undefined spaces.

        self.web_element = element

        return None

    def input_text(self, text):
        self.web_element.send_keys(text)
        return None

    def click(self):
        element = WebDriverWait(
            self.driver, 10).until(EC.element_to_be_clickable(self.locator))
        
        element.click()
        return None

    def attribute(self, attr_name):
        attribute = self.web_element.get_attribute(attr_name)
        return attribute

    @property
    def text(self):
        #We've already found the element after a wait, so not needed here
        text = self.web_element.text
        return text