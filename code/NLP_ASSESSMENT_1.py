###############################################
###############################################
###############################################
#Chinese Emo Bank Excel To Usable CSV

import pandas as pd

file_read = pd.read_csv(r'C:\Users\belmi\Downloads\ChineseEmoBank\ChineseEmoBank\CVAW_SD\CVAW_all_SD.csv')
columns = []
cells = []

for i in file_read:
    columns = ['', 'Word', 'Valence Mean', 'Arousal Mean', 'Dominance Mean']
    for cell in file_read[i]:
        cells.append(cell.split('\t'))

emo_bank_data = {columns[1]: [i[1] for i in cells], columns[2]: [float(i[2]) for i in cells], columns[3]: [float(i[3]) for i in cells], columns[4]: [None for i in cells]}
emo_bank = pd.DataFrame(data = emo_bank_data)
print(emo_bank)

emo_bank.to_csv('chinese_emo_bank.csv', index=False)

###############################################
###############################################
###############################################
#Chinese Emo Bank Excel To Usable CSV

import pandas as pd

file_read = pd.read_csv(r'C:\Users\belmi\Downloads\Ratings_Warriner_et_al.csv')

file_read = file_read.iloc[:, [1, 2, 5, 8]]
file_read.columns = ['Word', 'Valence Mean', 'Arousal Mean', 'Dominance Mean']
print(file_read)

file_read.to_csv('english_emo_bank.csv', index=False)

###############################################
###############################################
###############################################
#Creating a Dataframe To Add to Later

import pandas as pd

data = pd.DataFrame({'Text': [0], 'String': [0], 'Word': ['Test'], 'Valence': [0], 'Arousal': [0], 'Dominance': None})
data.to_csv('Harry Potter VAD.csv', index=False)


###############################################
###############################################
###############################################
#Harry Potter Chinese TEXT TO CSV

from googletrans import Translator
import string
import MicroTokenizer
from TCSP import read_stopwords_list
import pandas as pd
from hanziconv import HanziConv

stop_words_chinese = read_stopwords_list()
punct = list(string.punctuation)
translator = Translator()

for i in ['，', '【', '】', '”', '￣', '》', '“', '。', '·',  '《', '）',  ' ', '；', '！', '（', '、', '：', '？', '‘', '’']:
    punct.append(i)

emo_bank = pd.read_csv('chinese_emo_bank.csv')
emo_bank_dict = {}

for i in range(len(emo_bank)):
    emo_bank_dict[emo_bank.iloc[i]['Word']] = [emo_bank.iloc[i]['Valence Mean'], emo_bank.iloc[i]['Arousal Mean']]


Data = pd.read_csv('Harry Potter VAD.csv')


with open(r"C:\\Users\belmi\OneDrive\Desktop\Python Projects\Harry_Potter_Complete_Chinese.txt", 'r', encoding = 'utf-8') as text_body:
    text = ''.join(text_body.readlines())
    text_broken = text.split('\n')
    file_num = (Data.max(axis= 0, numeric_only=True)['Text']) + 1
    match = 0
    Data = pd.read_csv('Harry Potter VAD.csv')
    for i in text_broken:
        string_num = (Data.max(axis=0, numeric_only=True)['String']) + 1
        if not i.isalnum():
            token = MicroTokenizer.cut(i)
            tokens = []
            for element in token:
                if element not in punct and element not in stop_words_chinese:
                    tokens.append(element)
            if tokens:
                for word in tokens:
                    try:
                        val = emo_bank_dict.get(HanziConv.toTraditional(word))[0]
                        aro = emo_bank_dict.get(HanziConv.toTraditional(word))[1]
                        match += 1
                        new_row = {'Text': int(file_num), 'String': int(string_num), 'Word': word, 'Valence': val, 'Arousal': aro, 'Dominance': None}
                        Data = Data.append(new_row, ignore_index=True)
                    except:
                        try:
                            val = emo_bank_dict.get(HanziConv.toSimplified(word))[0]
                            aro = emo_bank_dict.get(HanziConv.toSimplified(word))[1]
                            match += 1
                            new_row = {'Text': file_num, 'String': int(string_num), 'Word': word, 'Valence': val, 'Arousal': aro, 'Dominance': None}
                            Data = Data.append(new_row, ignore_index=True)
                        except:
                            pass
    print(Data)
    Data.to_csv('Harry Potter VAD.csv')

###############################################
###############################################
###############################################
#Harry Potter English Text TO CSV

import nltk
import pandas as pd
import string
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

lemmatizer = WordNetLemmatizer()
stop_words = stopwords.words("english")
punct = list(string.punctuation)

emo_bank = pd.read_csv('english_emo_bank.csv')
emo_bank_dict = {}

for i in range(len(emo_bank)):
    emo_bank_dict[emo_bank.iloc[i]['Word']] = [emo_bank.iloc[i]['Valence Mean'], emo_bank.iloc[i]['Arousal Mean'], emo_bank.iloc[i]['Dominance Mean']]

with open(r"C:\\Users\belmi\OneDrive\Desktop\Python Projects\Harry_Potter_Complete_English.txt", 'r', encoding = 'utf-8') as text_body:
    text = ''.join(text_body.readlines())
    text_unbroken = ''.join(text.split('\n')).split('.')
    Data = pd.read_csv('Harry Potter VAD.csv')
    file_num = (Data.max(axis= 0, numeric_only=True)['Text']) + 1
    match = 0
    for i in text_unbroken:
        string_num = (Data.max(axis=0, numeric_only=True)['String']) + 1
        if not i.isalnum():
            token = word_tokenize(i)
            tokens = []
            for element in token:
                if element not in punct and element not in stop_words:
                    tokens.append(element.lower())
            if tokens:
                for word in tokens:
                    try:
                        val = emo_bank_dict.get(lemmatizer.lemmatize(word))[0]
                        aro = emo_bank_dict.get(lemmatizer.lemmatize(word))[1]
                        dom = emo_bank_dict.get(lemmatizer.lemmatize(word))[2]
                        new_row = {'Text': int(file_num), 'String': int(string_num), 'Word': word, 'Valence': val, 'Arousal': aro, 'Dominance': dom}
                        Data = Data.append(new_row, ignore_index=True)
                    except:
                        pass
    Data.to_csv('Harry Potter VAD.csv')

import tika
from tika import parser
tika.initVM()

###############################################
###############################################
###############################################
#Harry Potter English PDF to Text

def parse_text(filename):
    parsed = parser.from_file(r"C:\Users\belmi\Downloads\{filename}.pdf".format(filename=filename))
    file = open(r"C:\Users\belmi\OneDrive\Desktop\Python Projects\{filename}.txt".format(filename=filename), 'w', encoding= "utf-8")
    file.write(parsed['content'])
    file.close()

parse_text('Harry_Potter_Complete_English')


###############################################
###############################################
###############################################
#Website Scrape

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



