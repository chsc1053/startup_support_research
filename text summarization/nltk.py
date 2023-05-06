import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from heapq import nlargest

#nltk.download('punkt')
#nltk.download('stopwords')
def summarize(text, n):
    # Tokenize the text into sentences and words
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    
    # Remove stop words and punctuation
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.lower() not in stop_words and word.isalnum()]
    
    # Calculate the frequency of each word
    freq_dist = nltk.FreqDist(words)
    
    # Calculate the score for each sentence based on the frequency of its words
    sentence_scores = {}
    for i, sentence in enumerate(sentences):
        sentence_words = word_tokenize(sentence)
        sentence_score = 0
        for word in sentence_words:
            if word.lower() in freq_dist:
                sentence_score += freq_dist[word.lower()]
        sentence_scores[i] = sentence_score
    
    # Get the top n sentences with the highest scores
    top_sentences = nlargest(n, sentence_scores, key=sentence_scores.get)
    
    # Sort the top sentences in their original order
    summary = ' '.join([sentences[i] for i in sorted(top_sentences)])
    return summary

text = "This study examines how the identity orientation of founders, i.e., the extent to which they define themselves in terms of their relationships to others and to social groups, is imprinted by their professional logic and influences their ambitions for venture growth. We draw on existing insights regarding the Darwinian, Communitarian, and Missionary orientation of entrepreneurs and on interviews with 29 founders to develop our hypotheses, which we then test in a sample of 58 academic and 113 non-academic founders that participated in a venture competition. We argue that, compared to non-academic institutional logics, academic logics are tied to a stronger Communitarian and Missionary orientation and a weaker Darwinian orientation in founders. A stronger Darwinian orientation values venture growth, whereas a stronger Communitarian orientation appraises the benefit of the technology for a restricted set of people at the expense of such growth ambitions. A stronger Missionary orientation values welfare maximization for society which may to some degree entail higher growth aspirations. We argue and empirically confirm that these identity orientations explain why academic founders hold lower growth aspirations for their start-up than non-academic founders. Our findings can at least partially clarify why academic start-ups do not grow according to expectancies. They theoretically advance our insights in academic entrepreneurship and founders' growth aspirations while also extending the literature on founders' identity orientation. © 2022"

summary = summarize(text, 3)
print("--------------------------------Summary------------------------------")
print(summary)
