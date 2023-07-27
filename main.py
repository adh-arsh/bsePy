#pip install beautifulsoup4
#pip install selenium

#https://stackoverflow.com/questions/13166395/fill-input-of-type-text-and-press-submit-using-python




#https://www.bseindia.com/markets/equity/EQReports/StockPrcHistori.html?flag=0

#use beautifulsoup library to populate text fields and click submit button


#search_in_page(link = "https://www.bseindia.com/markets/equity/EQReports/StockPrcHistori.html?flag=0", companyCode = "BSECODE", radio="daily", from="01/07/2023" , to="10/07/2023")





from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#how to populate textfields beautifulsoup
#how to populate radiobutton beautiful soup
#how to press button beautiful soup



# For Chrome
driver = webdriver.Chrome()

url = "https://www.bseindia.com/markets/equity/EQReports/StockPrcHistori.html?fl"  # Replace with the URL of the web page you want to scrape
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