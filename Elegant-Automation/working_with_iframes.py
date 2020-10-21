from selenium import webdriver

browswer = webdriver.Chrome()

browswer.get('https://techstepacademy.com/iframe-training')

# dave = browswer.find_element_by_css_selector("div#block-ec928cee802cf918d26c div p")
# with Frames it's not able to locate the ID inside the i-frame.

#------------ We have to switch to iframe.

iframe = browswer.find_element_by_css_selector("iframe")

browswer.switch_to_frame(iframe)
dave = browswer.find_element_by_css_selector("div#block-ec928cee802cf918d26c div p")
# NOW I can access the id's within the IFRAME

print(dave)

#------------

#------------ Getting back up to the top level of the site
# Find something outside of the IFrame.

browswer.switch_to.default_content()
title_text = browswer.find_element_by_css_selector("div#page-5d3de848045889000188d388 div p")
print(title_text.text)
#------------