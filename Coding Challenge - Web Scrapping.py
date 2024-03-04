import csv

import requests
from bs4 import BeautifulSoup


def scrape_data():
  url = "https://idbop.mylicense.com/verification/Search.aspx"
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')

  data = []
  for row in soup.find_all('tr'):
    cols = row.find_all('td')
    if len(cols) > 0:
      first_name = cols[0].text
      middle_name = cols[1].text
      last_name = cols[2].text
      if last_name.startswith('L'):
        license_number = cols[3].text
        license_type = cols[4].text
        status = cols[5].text
        original_issued_date = cols[6].text
        expiry = cols[7].text
        renewed = cols[8].text
        data.append([first_name, middle_name, last_name, license_number])
        data.append([license_type, status, original_issued_date, expiry])
        data.append([renewed])

  with open('pharmacists.csv', 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(
        ["First Name", "Middle Name", "Last Name", "License Number"])
    writer.writerow(
        ["License Type", "Status", "Original Issued Date", "Expiry"])
    writer.writerow(["Renewed"])
    writer.writerows(data)


scrape_data()
