from bs4 import BeautifulSoup
import requests
from time import sleep
from random import randint
from sql_methods import insert_number

def scrape_phone_numbers():
    resp = requests.get('https://www.randomphonenumbers.com/random_us_phone_numbers')
    full_page_html = BeautifulSoup(resp.content, 'html5lib')
    base_html = full_page_html.find_all('div', class_ = 'row no-margin name-list')[0]
    list_of_num_info = base_html.find_all('ul', class_= 'list-unstyled')[0].find_all('li', class_= 'col-md-6 col-sm-6 col-xs-12')
    for num_info in list_of_num_info:
        is_cell = num_info.find_all('p', class_ = 'des')[0].text
        if 'Cell Number' in is_cell:
            number = num_info.find_all('a')[0].text.replace('-', '')
            insert_number('phone_numbers', number)

if __name__ == '__main__':
    while True:
        scrape_phone_numbers()
        sleep(randint(1, 5))
