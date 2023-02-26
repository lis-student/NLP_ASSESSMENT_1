import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


forums = [r"العربية-arabic.41",
          r"%E4%B8%AD%E6%96%87-%E6%96%B9%E8%A8%80-chinese.72",
          r"spanish-english-grammar-gramática-español-inglés.22",
          r"spanish-english-vocabulary-vocabulario-español-inglés.83"]


list_of_threads = []



for forum in forums:
    page = 1
    page_num = ''

    while True:
        URL = "https://forum.wordreference.com/forums/{0}/{1}?order=reply_count&direction=desc".format(forum, page_num)
        webpage = requests.get(URL)
        page_num = 'page-{}'.format(str(page))
        if webpage.status_code == 404 or page == 4:
            break
        soup = BeautifulSoup(webpage.content, 'html.parser')
        for i in soup.find_all('a'):
            text = str(i)
            x = re.findall("/threads.+preview\"", text)
            if x:
                for y in x:
                    list_of_threads.append(str(x)[2:-10])
                    print('New Thread Collected')
        page += 1

Author = []
Native_Language = []
Comment = []
Is_Question = []
thread_url=''


for thread in list_of_threads:
    page = 1
    page_num = ''

    while True:
        page += 1
        thread_url = "https://forum.wordreference.com{}{}".format(thread, page_num)
        page_num = 'page-{}'.format(str(page))
        thread_webpage = requests.get(thread_url)
        last_page = ''
        if thread_webpage.status_code == 404 or page == 10:
            break
        else:
            soup = BeautifulSoup(thread_webpage.content, 'html.parser')
            if soup == last_page:
                break
            last_page = soup
            title = True

            for box in soup.find_all(class_ = "message message--post js-post js-inlineModContainer"):
                for match in (re.findall('ified" title="Native language">[^<>]+<', str(box))):
                    Native_Language.append(re.sub('\s', ' ', match)[46:-11])

            misc = [Comment.append(' '.join(re.split('<[^>]+>',
                                            re.findall('<div.+</div>',
                                            re.sub('\n+', '',
                                            re.sub('\t+', '',
                                            str(i))))[0]))) for i in soup.find_all(class_="bbWrapper")]

            for box in soup.find_all(class_ = "message message--post js-post js-inlineModContainer"):
                for match in (re.findall('itemprop="name"><[^<>]+>?[^<>]+<|itemprop="name">[^<>]+<', str(box))):
                    if title:
                        Is_Question.append(title)
                        title = not(title)
                    else:
                        Is_Question.append(title)
                    Author.append(re.findall('>[^<>]+<', str(match))[0][1:-1])
            ID = [i for i in range(len(Author))]
            Data = pd.DataFrame(data={'ID': ID, 'Author': Author, 'Native_Language': Native_Language, 'Is_Question': Is_Question, 'Comment': Comment})
            Data.to_csv('Harry Potter VAD.csv')
