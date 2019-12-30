import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from bs4 import BeautifulSoup
import requests

# creating request to the site
result = requests.get("http://www.hubertiming.com/results/2017GPTR10K")
src = result.content
soup = BeautifulSoup(src,'lxml')

title = soup.title
# print(title)
# print(soup.get_text)

all_links = soup.find_all('a')

for link in all_links:
    print(link.get('href'))


rows = soup.find_all('tr')
# print(rows[:10])  

list_rows = []
for row in rows:
    row_td = row.find_all("td")
    str_cells = str(row_td)
    cleantext = BeautifulSoup(str_cells, "lxml").get_text()
    list_rows.append(cleantext)
print(cleantext)

# remove the html tags using Beautiful Soup
# str_cells = str(row_td)
# cleantext = BeautifulSoup(str_cells, "lxml").get_text()
# print(cleantext)

df = pd.DataFrame(list_rows)
df.head(10)