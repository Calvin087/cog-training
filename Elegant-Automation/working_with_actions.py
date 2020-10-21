from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present

browser = webdriver.Chrome()

browser.get('https://techstepacademy.com/training-ground')

# ----------------
    # alert = Alert(browser)
    # alert.text
    # >> 'You clickedButton1'
    # alert.accept() / dismiss()
# ----------------

# ----------------
    # print("I've arrived at the site location: ")

    # WebDriverWait(browser, 10).until(alert_is_present())
    # print('Alert has appeared')
# ----------------

sel = browser.find_element_by_id('sel1')
my_selection = Select(sel)

# my_selection.options >> list of elements
# [el.text for el in my_selection.options] >> list comp
# >>my ['Bears', 'Beets', 'Battlestar Galactica']
# my_selection.select_by_visible_text('Battlestar Galactica') >> changes drop down text
# my_selection.select_by_index(0) >> changes drop down text
# my_selection.select_by_value('second') >> changes drop down text
# my_selection.first_selected_option.text >> displays first or current item