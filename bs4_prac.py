import requests
from bs4 import BeautifulSoup

#making request to the website
result = requests.get("https://www.google.com/")

# checking the website status code
print(result.status_code)

# checkimg the http header value
print(result.headers)

# storing the source code into a vairiable
src = result.content

# passing the src variable into the BeautifulSoup obj
soup = BeautifulSoup(src,"lxml")

# finding all the a tags
links = soup.find_all("a")

print(links)
print("\n")

for link in links:
    if "About" in link.text:
        print(link)
        print(link.attrs['href'])

