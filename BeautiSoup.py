import requests
from bs4 import BeautifulSoup

# URL of the web page containing the form
url = 'https://www.bseindia.com/markets/equity/EQReports/StockPrcHistori.html?flag=0'

# Send a GET request to the web page
response = requests.get(url)

# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the dropdown list for the Segment field using appropriate HTML attributes
segment_dropdown = soup.find('select', {'name': 'anntype'})

# Check if the dropdown list is found before selecting an option
if segment_dropdown:
    # Select the desired option (e.g., Equity, Debt/Others, MF/ETFs)
    segment_dropdown.find('option', text='Equity').selected = True
    # If Debt/Others is selected:
    # segment_dropdown.find('option', text='Debt/Others').selected = True
    # If MF/ETFs is selected:
    # segment_dropdown.find('option', text='MF/ETFs').selected = True
else:
    print("Segment dropdown not found in the form.")

# Find the text field for the Security Name using appropriate HTML attributes
security_name_field = soup.find('input', {'name': 'strSecurityName'})

# Check if the field is found before populating a value
if security_name_field:
    security_name_field['value'] = 'AAPL'  # Replace with the desired security name or code
else:
    print("Security Name field not found in the form.")

# Find the radio buttons for the Period field using appropriate HTML attributes
period_radios = soup.find_all('input', {'name': 'period'})

# Check if the radio buttons are found before selecting an option
if period_radios:
    # Select the desired option based on the chosen period (Daily, Monthly, Yearly)
    for radio in period_radios:
        if radio['value'] == 'Daily':
            radio['checked'] = True
        # If Monthly is selected:
        # elif radio['value'] == 'Monthly':
        #     radio['checked'] = True
        # If Yearly is selected:
        # elif radio['value'] == 'Yearly':
        #     radio['checked'] = True
else:
    print("Period radio buttons not found in the form.")

# Find the input fields for the "from" and "to" dates using appropriate HTML attributes
from_date_field = soup.find('input', {'name': 'strDayFromDate'})
to_date_field = soup.find('input', {'name': 'strDayToDate'})

# Check if the fields are found before populating values
if from_date_field and to_date_field:
    # Populate the "from" and "to" dates with the sample data
    from_date_field['value'] = '01/07/2023'
    to_date_field['value'] = '10/07/2023'
else:
    print("Date fields not found in the form.")

# Find the submit button in the form using appropriate HTML attributes
submit_button = soup.find('input', {'type': 'submit'})

# Check if the submit button is found before submitting the form
if submit_button:
    # Extract the form action URL
    form_action_url = submit_button.parent['action']
    # Submit the form by sending a POST request with the updated form data
    form_data = {
        'strType': segment_dropdown['value'],
        'strSecurityName': security_name_field['value'],
        'period': next(radio for radio in period_radios if 'checked' in radio.attrs)['value'],
        'strDayFromDate': from_date_field['value'],
        'strDayToDate': to_date_field['value']
    }
    response = requests.post(form_action_url, data=form_data)

    # Print the response or perform further actions
    print(response.text)
else:
    print("Submit button not found in the form.")
