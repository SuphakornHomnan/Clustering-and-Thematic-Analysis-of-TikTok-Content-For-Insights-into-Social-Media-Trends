import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.corpus import words
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# Download tokenization packages
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('words')

from nltk.corpus import stopwords
stopwords = stopwords.words('english')
# Stemming and Lemmatization
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
# Create a set of English words
english_words = set(words.words())

# Filtering function
def filtering(description):
    words = nltk.word_tokenize(description)
    words = [w for w in words if w.lower() not in stopwords]
    # Apply stemming and lemmatization
    processed_words = [stemmer.stem(lemmatizer.lemmatize(word)) for word in words]
    
    return ' '.join(processed_words)

def remove_emoji(text):
    emoji_pattern = re.compile("["
                                u"\U0001F600-\U0001F64F"  # emoticons
                                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                u"\U00002702-\U000027B0"  # dingbats
                                u"\U000024C2-\U0001F251"  # enclosed characters
                                u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
                                u"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
                                u"\U0001F700-\U0001F77F"  # Alchemical Symbols
                                u"\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
                                u"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
                                u"\U0001FA00-\U0001FA6F"  # Chess Symbols
                                u"\U00002700-\U000027BF"  # Dingbats
                                u"\U0001F1E6-\U0001F1FF"  # Regional Indicator Symbols
                                u"\U0001F004"             # Mahjong Tile Red Dragon
                                u"\U0001F0CF"             # Playing Card Black Joker
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

def remove_non_english_words(text):
    # Tokenize the text into words
    word_list = re.findall(r'\b\w+\b', text)
    # Filter out non-English words
    filtered_words = [word for word in word_list if word.lower() in english_words]
    # Join the filtered words back into a single string
    filtered_text = ' '.join(filtered_words)
    
    return filtered_text


def text_preprocess (df):
    # Remove punctuations from the Description column
    punctuations = '''()-[]{};:"\,<>./?@#$%^&*£!~'''
    text_list = []
    for text in df['description']:
        sentence = ""
        # Text preprocessing
        for char in text:
            if (char not in punctuations):
                sentence = sentence + char
        # Removing number
        pattern = r'\d+'
        sentence = re.sub(pattern, '', sentence)
        # Removing emoji
        sentence = remove_emoji(sentence)
        sentence = remove_non_english_words(sentence)

        # Mutuating the text cleaning column as sentence
        text_list.append(sentence)
    # Apply the function to the Description column and create the Tokens column
    df['sentence'] = text_list
    df['sentence'] = df['sentence'].apply(filtering)
