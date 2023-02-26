import pandas as pd

data = pd.DataFrame({'Text': [0], 'String': [0], 'Word': ['Test'], 'Valence': [0], 'Arousal': [0], 'Dominance': None})
data.to_csv('Harry Potter VAD.csv', index=False)
