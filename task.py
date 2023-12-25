from urllib import request
from bs4 import BeautifulSoup
# подключаем urlopen из модуля urllib
from urllib.request import urlopen
import time


# получаем исходный код страницы
html_code = str(urlopen('https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D0%BB%D0%BE%D0%B0%D0%B7%D0%B8%D0%B0%D1%82%D1%81%D0%BA%D0%B8%D0%B9_%D1%82%D1%80%D0%B8%D1%82%D0%BE%D0%BD').read(),'utf-8')
# отправляем исходный код страницы на обработку в библиотеку
inner_soup = BeautifulSoup(html_code, "html.parser")
# оставляем только блок с содержимым статьи
inner_soup = inner_soup.find('title')
print(inner_soup.get_text())


start_time = time.time()

