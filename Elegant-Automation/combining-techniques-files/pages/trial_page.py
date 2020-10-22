from .base_elements import BaseElement
from .base_pages import BasePage
from .locator_class import Locator
from selenium.webdriver.common.by import By

class TrialPage(BasePage):
    
    url = "https://techstepacademy.com/trial-of-the-stones"

    @property
    def stone_input(self):
        locator = Locator(by=By.CSS_SELECTOR, value='input#r1Input')

        return BaseElement(
            driver=self.driver,
            locator=locator,
                # by=locator[0],
                # value=locator[1]
        )
    
    @property
    def stone_button(self):
        locator = Locator(by=By.CSS_SELECTOR, value='button#r1Btn')

        return BaseElement(
            driver=self.driver,
            locator=locator,
                # by=locator[0],
                # value=locator[1]
        )

    @property
    def secrets_input(self):
        locator = Locator(by=By.CSS_SELECTOR, value='input#r2Input')

        return BaseElement(
            driver=self.driver,
            locator=locator,
                # by=locator[0],
                # value=locator[1]
        )

    @property
    def secrets_button(self):
        locator = Locator(by=By.CSS_SELECTOR, value='button#r2Butn')

        return BaseElement(
            driver=self.driver,
            locator=locator,
                # by=locator[0],
                # value=locator[1]
        )