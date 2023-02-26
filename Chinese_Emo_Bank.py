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