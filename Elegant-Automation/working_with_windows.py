from selenium import webdriver

browser1 = webdriver.Chrome()
browser2 = webdriver.Chrome()

browser1.get('http://techstepacademy.com/training-ground')
# browser2.get('http://google.com')

browser1.execute_script('window.open("http://techstepacademy.com", "_blank");')
browser1.execute_script('window.open("http://techstepacademy.com", "_blank");')
browser1.execute_script('window.open("http://techstepacademy.com", "_blank");')
browser1.execute_script('window.open("http://techstepacademy.com", "_blank");')

# ----------
# IMPORTANT # browser1.window_handles
# ----------

handles = browser1.window_handles
# returns a [ LIST ]
# handles[0] is the first tab - [-1]
# The handles are NOT in order