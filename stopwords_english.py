# import the nltk library
import nltk

# desde nltk descargar stopwords
from nltk.corpus import stopwords
nltk.download('stopwords')

lista_stopwords = stopwords.words('english')

# imprimir las stopwords
print(lista_stopwords)