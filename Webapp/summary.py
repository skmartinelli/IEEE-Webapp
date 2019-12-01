import requests
from bs4 import BeautifulSoup
import re
#from nltk.corpus import stopwords
#from nltk.stem import PorterStemmer
#from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
nltk.download('punkt')

def getSummary(link):#, slidervalue):
    
    rawText = scrapeText(link)
    
    text = re.sub(r'\[[0-9]*\]', ' ', rawText)
    text = re.sub(r'\s+', ' ', rawText)
    
    formattedText = re.sub('[^a-zA-Z]', ' ', text)
    formattedText = re.sub(r'\s+', ' ', formattedText)
    
    freqs = getFreqs(formattedText)
    
    sents = nltk.sent_tokenize(text)
    
    scores = scoreSentences(sents, freqs)
    print(scores)
    
    threshold = getThreshold(scores)
    
    summary = summarize(sents, scores, threshold)
    
    return summary
    
def scrapeText(link):

    url = link
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'lxml')

    pars = soup.find_all('p')

    text = ""

    for p in pars:
        text += p.text
        
    return text

def getFreqs(text):
    
    nltk.download('stopwords')
    
    stopWords = set(stopwords.words('english'))
    words = nltk.word_tokenize(text)
    ps = nltk.PorterStemmer()
    
    freqs = dict()
    
    for word in words:
        word = ps.stem(word)
        if word not in stopWords:
            if word in freqs:
                freqs[word] += 1
            else:
                freqs[word] = 1
        
        return freqs
        
def scoreSentences(sents, freqs):
    sentVals = dict()
    
    for sent in sents:
        for word in freqs:
            if word in nltk.word_tokenize(sent.lower()):
                if sent[:15] in sentVals:
                    sentVals[sent[:15]] += freqs[word]
                else:
                    sentVals[sent[:15]] = freqs[word]
        #sentVals[sent[:15]] = (sentVals[sent[:15]]) // (len(nltk.word_tokenize(sent)))
        
    return sentVals

def getThreshold(sentVals):
    valSum = 0
    
    for sent in sentVals:
        valSum += sentVals[sent]
        
    return int(valSum/len(sentVals))

def summarize(sents, sentVals, threshold):
    summary = ''
    
    for sent in sents:
        if sent[:15] in sentVals and sentVals[sent[:15]] > threshold:
            summary += "\n\u2022" + sent
            
    return summary
