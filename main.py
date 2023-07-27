#pip install beautifulsoup4
#pip install selenium

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# For Chrome
driver = webdriver.Chrome()

url = "https://example.com"  # Replace with the URL of the web page you want to scrape
driver.get(url)

# Wait for the element to be loaded (optional)
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "target_element_id")))

# Get the page source
page_source = driver.page_source

# Parse the page source with Beautiful Soup
soup = BeautifulSoup(page_source, "html.parser")

# Find the element you want to extract (replace "target_element_id" with the actual ID of the element)
target_element = soup.find("input", {"id": "target_element_id"})

# Extract the content you want to populate the text field with
content_to_populate = target_element.get("value")

# Close the WebDriver
driver.quit()