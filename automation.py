from selenium import webdriver
import time

def wait(sec):
	chrome_browser.implicitly_wait(sec)

chrome_browser = webdriver.Chrome('./chromedriver')

#chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

wait(5)
close_pop_up = chrome_browser.find_element_by_class_name('at-cm-no-button')

close_pop_up.click()

assert 'Selenium Easy Demo' in chrome_browser.title
show_message_button = chrome_browser.find_element_by_class_name('btn-default')
# print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')
user_button2 = chrome_browser.find_element_by_css_selector('#get-input > .btn')
print(user_button2)
user_message.clear()
user_message.send_keys('I AM EXTRA COOL!')

show_message_button.click()

output_message = chrome_browser.find_element_by_id('display')
assert 'I AM EXTRA COOL!' in output_message.text

time.sleep(5)
chrome_browser.quit()