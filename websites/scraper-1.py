import csv
import requests
from bs4 import BeautifulSoup

# Specify the CSV file name
csv_filename = "books_data.csv"

# Send request and parse HTML
html_text = requests.get('https://books.toscrape.com/').text
soup = BeautifulSoup(html_text, 'lxml')

# find section that contains interested books
section = soup.find('section')

#printing out the description which is the first div container
description_container = section.find('div').text
# print(books_container)

interested_container = section.find('ol')
book_lists = interested_container.find_all('li')
# things to get
# name, title, instock or not, price, imageURL






for items in book_lists:
    # image_url = items.a.get('href')
    image_url = items.article.div.a['href'].replace(" ",'')
    Book_title = items.h3.text
    price_container = items.find('div', class_='product_price')
    price = price_container.find('p', class_='price_color').text.replace(" ",'')
    availability = price_container.find('p',class_='instock availability').text.replace(" ",'' )
    
    # print(f'''
    #       product name: {Book_title}
    #       Product image: {image_url}
    #       Product price: {price}
    #       Product avalability: {availability}  
    #       ''')
    
    print(f'product name: {Book_title.strip()}')
    print(f' Product image:{image_url}')
    print(f'Product price: {price.strip()}')
    print(f'Product avalability: {availability.strip()}')









# # Open CSV file for writing in append mode
# with open(csv_filename, 'a', newline='') as csvfile:
#     # Create CSV writer object
#     csv_writer = csv.writer(csvfile)

#     # Write header row if the file is empty
#     if csvfile.tell() == 0:
#         csv_writer.writerow(['Category Name', 'Category Link'])

#     # Extract and write data to CSV
#     for item in item_list:
#         link = item.a.get('href')
#         name = item.a.text
#         csv_writer.writerow([name, link])

# print(f"Data saved to CSV file: {csv_filename}")
