import pandas as pd

file_read = pd.read_csv(r'C:\Users\belmi\Downloads\Ratings_Warriner_et_al.csv')

file_read = file_read.iloc[:, [1, 2, 5, 8]]
file_read.columns = ['Word', 'Valence Mean', 'Arousal Mean', 'Dominance Mean']
print(file_read)

file_read.to_csv('english_emo_bank.csv', index=False)

