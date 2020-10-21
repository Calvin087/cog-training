# Using Chrome console panel. We can search by ID and selectors.

# --------------- CSS SELECTORS

# $$("input[id='ipt1']")

# >> ("input[id='ipt1']")
        # [input#ipt1]
        # 0: input#ipt1
        # length: 1
        # __proto__: Array(0)

# ---------------
# ---------------

input2_locator = "input[id='ipt2']"

# --------------- X-PATH Selectors

# >> $x("//button[@id='b4']")

        # 0: button#b4
        # length: 1
        # __proto__: Array(0)

# ---------------
# ---------------

button4_locator = "//button[@id='b4']"

# --------------- Ambiguous Selectors - Extremely Fragile method

# 1. This tag is searching for the text inside a bold tag.
# 2. /.. goes up one level ../ = Two levels which is the DIV
# 3. From the main Div, go back down and find the p tag.
# 4. this gives you an array of p's len(1)
# 5. Then we can index and grab the innerHTML


# >> $x("//b[text()='Product 1']/../../p")[0].innerHTML

#   "
#     Price: $200
#   "

# ---------------
# ---------------

from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://www.techstepacademy.com/training-ground')

# Assign Elements
input2_elem = browser.find_element_by_css_selector(input2_locator)
button4_elem = browser.find_element_by_xpath(button4_locator)

# Manipulate Elements

input2_elem.send_keys("Test Text")
button4_elem.click()

browser.quit()