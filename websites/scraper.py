import csv
import requests
from bs4 import BeautifulSoup

# Specify the CSV file name
csv_filename = "books_data.csv"

# Send request and parse HTML
html_text = requests.get('https://books.toscrape.com/').text
soup = BeautifulSoup(html_text, 'lxml')

# Find categories container
container = soup.find('div', class_='side_categories')
sub_container = container.find('ul', class_='nav nav-list')
actual_container = sub_container.find('ul')
item_list = actual_container.find_all('li')

# Open CSV file for writing in append mode
with open(csv_filename, 'a', newline='') as csvfile:
    # Create CSV writer object
    csv_writer = csv.writer(csvfile)

    # Write header row if the file is empty
    if csvfile.tell() == 0:
        csv_writer.writerow(['Category Name', 'Category Link'])

    # Extract and write data to CSV
    for item in item_list:
        link = item.a.get('href')
        name = item.a.text
        csv_writer.writerow([name, link])

print(f"Data saved to CSV file: {csv_filename}")
