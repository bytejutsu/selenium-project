from selenium import webdriver

CHROME_DRIVER_PATH = "/home/nablidev/DEV/chromedriver"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get("https://www.python.org/")

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)

bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')

event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")
for name in event_names:
    print(name.text)

dictionary = {time.text: name.text for time in event_times for name in event_names}
print(dictionary)

# driver.close()
driver.quit()
