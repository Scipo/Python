from threading import Thread 
from bs4 import BeautifulSoup
import requests as req
import queue as q
import json

starting_url = '' # starting url
visited = set()
max_visited = 100
num_worker = 5
data = []

def get_html(url):
    try:
        response = req.get(url)
        return response.content
    except Exception as e:
        print(e)
        return ''


def extract_links(ex_link):
    return [a.get('href') for a in ex_link.select('a.page-numbers') if a.get('href') not in visited]

def exract_content(content):
    # content extraction
    for product in content.select('.product'): 
        data.append({
            'id': product.find('a', attrs={'data-product_id': True})['data-product_id'], 
            'name': product.find('h2').text,
            'price': product.find(class_='amount').text,
        })

def crawl(url):
    visited.add(url)
    print("Crawl: ", url)
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    exract_content(soup)
    links=extract_links(soup)
    for link in links:
        if link not in visited:
            q.put(link)

def queue_work(i, q):
    while True:
        url = q.get()
        if (len(visited) < max_visited and url not in visited):
            crawl(url)
        q.task_done()

q = q.Queue()
for i in range(num_worker):
    Thread(target=queue_work, args=(i, q), daemon=True).start()

q.put(starting_url)
q.join()

print('Done')
print('Visited: ', visited)
#print('Data: ', data)
print('Data: ', json.dumps(data))