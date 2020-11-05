import os
import requests
from bs4 import BeautifulSoup
import datetime
import csv

today = datetime.datetime.now()
today = (today.strftime("%Y-%b-%d"))
output_folder = 'results'

try:
    os.mkdir(output_folder)
except:
    print('cant create folder')
    pass

for root, _, files in os.walk("./search_lists", topdown=False):
    for search_file in files:
        full_search_file = os.path.join(root, search_file)

        with open(full_search_file, 'r') as listfile:
            lines = listfile.readlines()

            for query in lines:

                count = 0
                no_of_pages = 2 # no of pages to search

                querys = query.replace(' ', '+')
                url = f'https://www.google.com/search?q={querys}'

                query_title = query.replace(' ', '-') # used for filename

                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}

                with open(f'{output_folder}/sem_{query_title}.csv', 'a', newline='') as csvfile:
                    linewriter = csv.writer(csvfile, delimiter='^', quotechar='"', quoting=csv.QUOTE_MINIMAL) # using ^ (caret) as delimiter
                    linewriter.writerow(['Date', 'Rank', 'Title', 'Url', 'Description']) # write csv header line

                    for i in range(no_of_pages): # get results from x no. of pages
                        full_url = f'{url}&start={count}' # add results count to url (0=1st page, 10=2nd page etc)
                        result = requests.get(full_url, headers=headers)

                        if result.status_code == 200:
                            soup = BeautifulSoup(result.content, 'lxml')

                            search_results = soup.find_all('div', class_='rc') # the search results excluding paid ads
                            for index, result in enumerate(search_results, start = 1):
                                index = index + count
                                linewriter.writerow([f'{today}^ {index}^ {result.h3.string}^ {result.a.get("href")}^ {result.h3.parent.parent.next_sibling.text}']) # write results in csv file

                                # Print results out
                                print(f'Date: {today}')
                                print(f'Rank: {index}')
                                print(f'Title: {result.h3.string}')
                                print(f'Url: {result.a.get("href")}')
                                print(f'Description: {result.h3.parent.parent.next_sibling.text}')
                                print('############\n')

                        count = count + 10 # add 10 to get next 10 search results