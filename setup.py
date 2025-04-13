from sklearn.model_selection import train_test_split
import os
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
import joblib


def text2paragraphs(filename, min_size=1):
    """ A text contained in the file 'filename' will be read 
    and chopped into paragraphs.
    Paragraphs with a string length less than min_size will be ignored.
    A list of paragraph strings will be returned"""
    
    txt = open(filename, encoding='utf-8').read()
    paragraphs = [para for para in txt.split("\n\n") if len(para) > min_size]
    return paragraphs

path = '../data/processed/books/'

files = os.listdir(path)
labels = {fname[:2] for fname in files if fname.endswith(".txt")}
labels = sorted(list(labels))

data = []
targets = []

for fname in files:
    if fname.endswith(".txt"):
        paras = text2paragraphs(path + fname, min_size=150)
        data.extend(paras)
        country = fname[:2]
        index = labels.index(country)
        targets += [index] * len(paras)
        


res = train_test_split(data, targets, 
                       train_size=0.8,
                       test_size=0.2,
                       random_state=42)
train_data, test_data, train_targets, test_targets = res 

vectorizer = CountVectorizer()

vectors = vectorizer.fit_transform(train_data)

# creating a classifier
classifier = MultinomialNB(alpha=.01)
classifier.fit(vectors, train_targets)

vectors_test = vectorizer.transform(test_data)

predictions = classifier.predict(vectors_test)
accuracy_score = metrics.accuracy_score(test_targets, 
                                        predictions)
f1_score = metrics.f1_score(test_targets, 
                            predictions, 
                            average='macro')

print("accuracy score: ", accuracy_score)
print("F1-score: ", f1_score)

some_texts = [
    "Mein Name ist Anna. Ich komme aus Österreich und lebe seit drei Jahren in Deutschland. Ich bin 15 Jahre alt und habe zwei Geschwister: Meine Schwester heißt Klara und ist 13 Jahre alt, mein Bruder Michael ist 18 Jahre alt. Wir wohnen mit unseren Eltern in einem Haus in der Nähe von München. Meine Mutter ist Köchin, mein Vater arbeitet in einer Bank.",
    "Maria er 20 år og bor i København. Maria har en hund. Hunden hedder Siko. Maria går tur med Siko, hver morgen. De går en halv time i en park, og et kvarter ved en havn. Efter deres tur, køber Maria en kop kaffe og nyder solen på hendes altan. Siko sover efter turen, fordi han er gammel.",
    "I live in a house near the mountains. I have two brothers and one sister, and I was born last. My father teaches mathematics, and my mother is a nurse at a big hospital. My brothers are very smart and work hard in school. My sister is a nervous girl, but she is very kind. My grandmother also lives with us. She came from Italy when I was two years old. She has grown old, but she is still very strong. She cooks the best food!",
    "Pues...En realidad, no es mucho difícil, no es como mis amigos dicen; dicen que español es taaaaaaaan difícil, son (o están?) equivocado. Si sigue en las clases (que no ellos hacen), la aprendizaje no es un problema.",
    "Mi nueva casa está en una calle ancha que tiene muchos árboles. El piso de arriba de mi casa tiene tres dormitorios y un despacho para trabajar. El piso de abajo tiene una cocina muy grande, un comedor con una mesa y seis sillas, un salón con dos sofás verdes, una televisión y cortinas. Además, tiene una pequeña terraza con piscina donde puedo tomar el sol en verano.",
    "Je m’appelle Jessica. Je suis une fille, je suis française et j’ai treize ans. Je vais à l’école à Nice, mais j’habite à Cagnes-Sur-Mer. J’ai deux frères. Le premier s’appelle Thomas, il a quatorze ans. Le second s’appelle Yann et il a neuf ans. Mon papa est italien et il est fleuriste. Ma mère est allemande et est avocate. Mes frères et moi parlons français, italien et allemand à la maison. Nous avons une grande maison avec un chien, un poisson et deux chats.",
    "Quando torno a casa studio e faccio i compiti, ma mi diverto anche giocando al computer e suonando la mia chitarra. Ceno alle 19:00 con la mia famiglia, composta da mia mamma, mio papà e i miei tre fratelli. Alle 22:30 circa vado a letto a leggere alcuni libri prima di dormire.",
    "Het leren van de Nederlandse taal gaat goed. Alleen de grammatica vind ik lastig. Ik heb al veel nieuwe woorden geleerd. Hoe gaat het bij jou in Duitsland? Hoe gaat het op je nieuwe school?",
    "Jag heter Simon och jag är fjorton år. Jag bor tillsammans med min mamma, min pappa och mina två systrar. Min mamma heter Annika. Hon arbetar som läkare på ett sjukhus. Min pappa heter Josef. Han arbetar inte längre eftersom han är pensionär. Förut arbetade han som målare."
]

vtest = vectorizer.transform(some_texts)
predictions = classifier.predict(vtest)
for label in predictions:
    print(label, labels[label])
    
joblib.dump(classifier, "../models/language_classifier.pkl")

loaded_classifier = joblib.load("../models/language_classifier.pkl")

vtest = vectorizer.transform(some_texts)
predictions = loaded_classifier.predict(vtest)
for label in predictions:
    print(label, labels[label])

joblib.dump(vectorizer, "../models/vectorizer.pkl")