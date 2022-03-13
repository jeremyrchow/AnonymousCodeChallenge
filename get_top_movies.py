#!/usr/bin/env python

import lxml.html as html
import requests
import re

url = 'https://www.imdb.com/chart/moviemeter/'
page = requests.get(url)
content = html.fromstring(page.content)

# Pull correct table by class
tr_elements = content.xpath("//tbody[@class='lister-list']//tr")

def extract_title(title_eles):
    if not title_eles:
        return 'NULL'
    return title_eles[0]
def extract_year(year_eles):
    if not year_eles:
        return 'NULL'
    year_string = year_eles[0]
    if re.fullmatch('\(([0-9])+\)',year_string):
        return year_string[1:-1]
    return 'NULL'

def extract_rating(rating_eles):
    if not rating_eles:
        return 'NULL'
    rating = rating_eles[0]
    return rating

row_dict = {
    'title' : ['title'],
    'year' : ['year'],
    'rating': ['rating'],
}
# Iterate through every row in table, besides header row
for row in range(len(tr_elements)):
    title_eles = tr_elements[row].xpath(".//td[@class='titleColumn']//a/text()")
    row_dict['title'].append(extract_title(title_eles))
    
    year_ele = tr_elements[row].xpath(".//td[@class='titleColumn']//span/text()")
    row_dict['year'].append(extract_year(year_ele))

    rating_ele = tr_elements[row].xpath(".//td[@class='ratingColumn imdbRating']//strong/text()")
    row_dict['rating'].append(extract_rating(rating_ele))

# Write to file
with open('output.txt','w') as f:
    for i in range(len(tr_elements)-1):
        f.write(row_dict['title'][i] + "," +  row_dict['year'][i] + "," + row_dict['rating'][i] + "\n")
