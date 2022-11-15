

import requests
from bs4 import BeautifulSoup
import urllib.request
from email_scraper import scrape_emails
import pandas as pd
from google.colab import files


urlid = input("Enter Website url (i.e.: example.com): ")
url = "https://"+urlid+"/"
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

response = []
urls = [link.get('href') for link in soup.find_all('a')]
for url_ in urls:
    fp = (
        urllib.request.urlopen(url + url_)
        if url_.startswith("https://")
        else urllib.request.urlopen(url + url_)
    )

    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    response.append(scrape_emails(mystr))
email = [item for item in response if item]
df = pd.DataFrame(email, columns=["Email"])
df.to_csv('email.csv', index=False)

files.download("email.csv")

