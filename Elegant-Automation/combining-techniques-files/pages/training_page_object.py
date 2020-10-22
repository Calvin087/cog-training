# Page objects are just Classes?
# This whole class is used for 1 page!
# I guess each page would need it's own personal class for each element

from .base_elements import BaseElement
from .base_pages import BasePage
from selenium.webdriver.common.by import By

class TrainingGroundPage(BasePage):
    

    # IMPROVED METHOD --------------

    @property
    #Allows me to go from calling button1() to just button
    def button1(self):
        locator = (By.ID, 'b1')

        return BaseElement(
            driver=self.driver,
            by=locator[0],
            value=locator[1]
        )

# -----------------------------------------

    # ORIGINAL METHOD --------------
        # def type_into_input(self, text):
        #     inputs = self.driver.find_element_by_id('ipt1')
        #     inputs.clear()
        #     inputs.send_keys(text)
        #     return None
    # ORIGINAL METHOD --------------


    # ORIGINAL METHOD --------------
        # def get_input_text(self):
        #     inputs = self.driver.find_element_by_id('ipt1')
        #     elem_text = inputs.get_attribute('value')
        #     return elem_text
    # ORIGINAL METHOD --------------
        

    # ORIGINAL METHOD --------------
        # def click_button_1(self):
        #     button1 = self.driver.find_element_by_id('b1')
        #     button1.click()
        #     return None
    # ORIGINAL METHOD --------------