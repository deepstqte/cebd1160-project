import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, f1_score

songs_df = pd.read_csv("clean_songs.csv", low_memory=False)

# Changing another file
supported_genres = ['rock', 'pop', 'electro', 'folk', 'hiphop', 'metal', 'rap']
for genre in supported_genres:
	songs_df.loc[songs_df['Genre'].str.contains(genre), 'Genre'] = genre
songs_df = songs_df[songs_df['Genre'].isin(supported_genres)]

songs_df['rock'] = np.where(songs_df['Genre'] == 'rock', '1', '0')
# songs_df.sort_values('rock', ascending=False, inplace=True)

X = songs_df.drop('rock', axis=1)
X = X.drop('Genre', axis=1)

y = songs_df['rock']

# Scaling data (KNeighbors methods do not scale automatically!)
scaler = StandardScaler()
scaler.fit(X)
scaled_features = scaler.transform(X)

X_train, X_test, y_train, y_test = train_test_split(scaled_features, y, test_size=0.35)

knn = KNeighborsClassifier(n_neighbors=4)
knn.fit(X_train, y_train)
y_predicted = knn.predict(X_test)
f1_score = f1_score(y_test, y_predicted, average="macro")
error_rate = np.mean(y_predicted != y_test)

print(f'F1 Score: {f1_score}')
print(f'Error Rate: {error_rate}')

print('Confusion Matrix')
print(confusion_matrix(y_test, y_predicted))
