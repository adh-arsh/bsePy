from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

# Setup chrome driver
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.set_window_size(500, 500)

# Navigate to the url
driver.get('https://www.bseindia.com/markets/equity/EQReports/StockPrcHistori.html?fl')

driver.maximize_window()

# Find input text field
input_text_fname = driver.find_element(By.ID, 'scripsearchtxtbx')

# Take a screenshot before entering a value
driver.save_screenshot("screenshot-1.png")

# Enter a value in the input text field
input_text_fname.send_keys("DALMIA BHARAT SUGAR AND INDUSTRIES LTD")

#to select radiobutton
driver.find_element_by_xpath("//input[@value='D']").click()

# Take a screenshot after entering a value
driver.save_screenshot("screenshot-2.png")

# Close the driver
driver.quit()