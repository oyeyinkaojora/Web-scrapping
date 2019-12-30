import requests
import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns
from bs4 import BeautifulSoup

res = requests.get("http://www.nationmaster.com/country-info/stats/Media/Internet-users")
soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('table')[0] 
data = pd.read_html(str(table))
df = pd.DataFrame(data)
convert = pd.DataFrame.to_csv(df,"data")

print(convert)






# result = requests.get("https://nigerianscholars.com/")
# src = result.content
# soup = BeautifulSoup(src, features="html.parser")

# a_tags = soup.find_all("a")

# print(result.headers)

# print(a_tags)