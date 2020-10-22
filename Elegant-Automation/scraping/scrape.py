from selenium import webdriver
from lxml import etree

browser = webdriver.Chrome()
browser.get("https://techstepacademy.com/trial-of-the-stones")
tree = etree.HTML(browser.page_source)

divs = browser.find_elements_by_xpath(".//div/span/..")
x = tree.findall(".//div/span/..")

print(x)