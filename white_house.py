import requests
from bs4 import BeautifulSoup


#getting info from the link
result = requests.get("https://www.whitehouse.gov/briefings-statements/")
src = result.content
soup = BeautifulSoup(src, features="html.parser")

#print(result.status_code)


urls = []
for h2_tags in soup.find_all("h2"):
    a_tags = h2_tags.find("a")
    urls.append(a_tags.attrs["href"])

print(urls)    

