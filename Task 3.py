import requests
import time
from threading import Thread


def get_html(link):
    response = requests.get(link)



links = ['https://www.ozon.ru', 'https://ru.wikipedia.org', 'https://www.google.com/',
             'https://mail.ru/', 'https://www.amazon.co.jp/']
threads = [Thread(target=get_html, args=[links[i]]) for i in range(5)]

time1 = time.time()
for i in range(5):
    print(get_html(links[i]))
print(f'Время последовательного выполнения: {time.time() - time1}')

time2 = time.time()
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f'Время параллельного выполнения: {time.time() - time2}')
