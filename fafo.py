from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup chrome driver
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.set_window_size(500, 500)

# Navigate to the url
driver.get('https://www.bseindia.com/markets/equity/EQReports/StockPrcHistori.html?fl')

driver.maximize_window()

# Find input text field

#to populate security name textfield
input_text_fname = driver.find_element(By.ID, 'scripsearchtxtbx')
# Enter a value in the input text field
input_text_fname.send_keys("DALMIA BHARAT SUGAR AND INDUSTRIES LTD")

#to select daily radiobutton
radio_button = driver.find_element(By.XPATH, "//input[@name='amit' and @value='D']")
radio_button.click()

#to populate from date textfield
from_text_fname = driver.find_element(By.ID, 'txtFromDate')
# Enter a value in the input text field
#from_text_fname.send_keys("01/07/2023")


driver.find_element(By.XPATH, "//input[@class='form-control hasDatepicker' and @id='txtFromDate']").send_keys("10-04-2018")

time.sleep(5)
#to populate to date textfield
to_text_fname = driver.find_element(By.ID, 'txtToDate')
# Enter a value in the input text field

driver.find_element(By.XPATH, "//input[@class='form-control hasDatepicker' and @id='txtToDate']").send_keys("20-04-2018")
time.sleep(5)
#to_text_fname.send_keys("31/07/2023")

#to select daily radiobutton
bt = driver.find_element(By.ID, "btnSubmit")
bt.click()

time.sleep(10)

# Take a screenshot after entering a value
driver.save_screenshot("screenshot-2.png")

# Close the driver
driver.quit()