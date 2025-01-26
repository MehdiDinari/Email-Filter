import pandas as pd
import sqlite3
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

MODEL_FILE = "spam_model.pkl"
VECTORIZER_FILE = "vectorizer.pkl"
DB_FILE = "spam.db"
DATA_FILE = "spam.csv"

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message TEXT,
    category TEXT
)
''')

if os.path.exists(DATA_FILE):
    data = pd.read_csv(DATA_FILE)
    data.drop_duplicates(inplace=True)
    data['Category'] = data['Category'].replace(['ham', 'spam'], ['Not Spam', 'Spam'])
    data.to_sql('messages', conn, if_exists='replace', index=False)

    mess = data['Message']
    cat = data['Category']
    mess_train, mess_test, cat_train, cat_test = train_test_split(mess, cat, test_size=0.2, random_state=42)

    vectorizer = CountVectorizer(stop_words='english')
    features_train = vectorizer.fit_transform(mess_train)

    model = MultinomialNB()
    model.fit(features_train, cat_train)

    joblib.dump(model, MODEL_FILE)
    joblib.dump(vectorizer, VECTORIZER_FILE)

else:
    print(f"⚠️ Le fichier {DATA_FILE} est introuvable. Vérifiez son emplacement.")

conn.commit()
conn.close()


def load_model():
    if not os.path.exists(MODEL_FILE):
        raise FileNotFoundError(f"⚠️ Modèle introuvable : {MODEL_FILE}")
    return joblib.load(MODEL_FILE)


def load_vectorizer():
    if not os.path.exists(VECTORIZER_FILE):
        raise FileNotFoundError(f"⚠️ Vectorizer introuvable : {VECTORIZER_FILE}")
    return joblib.load(VECTORIZER_FILE)


def predict_and_save(message):
    model = load_model()  # Charger le modèle
    vectorizer = load_vectorizer()  # Charger le vectorizer

    transformed_message = vectorizer.transform([message])
    prediction = model.predict(transformed_message)[0]

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS predictions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        message TEXT,
        label TEXT
    )
    ''')

    cursor.execute("INSERT INTO predictions (message, label) VALUES (?, ?)", (message, prediction))
    conn.commit()
    conn.close()

    return "Spam" if prediction == "Spam" else "Non Spam"
