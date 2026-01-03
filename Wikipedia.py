
import requests as rq
from bs4 import BeautifulSoup as bs
pages = int(input('how many wikipedia pages do you want to search'))
contact = input("what is your email (This is used only for wikipedias robot policy)")
headers = {
'User-Agent': f'TestBot/1.0 (contact: {contact})'
}
for page in range(pages):
    page = input("Web Page: ")
    item = int(input('which paragraph of the article do you want (if you want them all answer -1)'))
    response = rq.get(page, headers=headers)
    soup = bs(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    if item != -1:
        print(paragraphs[item].get_text())
    else:
        for p in paragraphs:
            words = p.get_text()
            print(words)
