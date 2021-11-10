from bs4 import BeautifulSoup
import requests


url = "http://boards.4chan.org/v/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html5lib")

font = soup.find("b", text="is game still worth playi").find_next_sibling("font")
for event in font.find_all("b", recursive=False):
   event_date = event.previous_sibling.strip()
   event_text = event.get_text(strip=True)
   print(event_date, event_text)
