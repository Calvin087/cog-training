from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://www.techstepacademy.com/trial-of-the-stones")


# Assigning Variables.
answer_one = browser.find_element_by_css_selector('input[id="r1Input"]')
answer_one_btn = browser.find_element_by_css_selector('button[id="r1Btn"]')
stone_answer = browser.find_element_by_css_selector('div#passwordBanner > h4')
trial_done_banner = browser.find_element_by_css_selector('div#trialCompleteBanner > h4')

# Answer two
answer_two = browser.find_element_by_css_selector('input[id="r2Input"]')
answer_two_btn = browser.find_element_by_css_selector('button[id="r2Butn"]')


# Answer three
answer_three = browser.find_element_by_css_selector('input[id="r3Input"]')
richest_merchant_locator = browser.find_element_by_xpath("//p[text()='3000']/../span/b")
answer_three_btn = browser.find_element_by_css_selector('button[id="r3Butn"]')

# Check Answers
check_answers = browser.find_element_by_css_selector('button[id="checkButn"]')

# Selenium Runs
answer_one.send_keys("Rock")
answer_one_btn.click()

answer_two.send_keys(stone_answer.text)
answer_two_btn.click()

answer_three.send_keys(richest_merchant_locator.text)
answer_three_btn.click()

check_answers.click()

assert trial_done_banner.text == "Trial Complete"
# No errors show if this is correct.

# $x("//p[text()='3000']/../p")[0].innerHTML
# >> $x("//b[text()='Product 1']/../../p")[0].innerHTML
