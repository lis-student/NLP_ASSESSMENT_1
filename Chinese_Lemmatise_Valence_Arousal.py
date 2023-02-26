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

#{'Text': [], 'String': [], 'Word': [], 'Valence': [], 'Arousal': []}
Data = pd.read_csv('Data.csv')


with open(r"C:\\Users\belmi\OneDrive\Desktop\Python Projects\Chinese.txt", 'r', encoding = 'utf-8') as text_body:
    text = ''.join(text_body.readlines())
    text_broken = text.split('\n')
    file_num = (Data.max(axis= 0, numeric_only=True)['Text']) + 1
    match = 0
    Data = pd.read_csv('Data.csv')
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
    #Data.to_csv('Data.csv')