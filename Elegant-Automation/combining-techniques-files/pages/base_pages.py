# why do we have object as parameter
# any class that you define has object as its
# parent class even if you don’t explicitly say so
# so your class will have a lot of default attributes
# and methods that any Python object has.

class BasePage(object):

    url = None

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)