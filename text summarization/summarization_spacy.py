#pip install -U pip setuptools wheel
#pip install -U spacy
#python -m spacy download en_core_web_sm

import spacy
nlp=spacy.load("en_core_web_sm")
text = "This study examines how the identity orientation of founders, i.e., the extent to which they define themselves in terms of their relationships to others and to social groups, is imprinted by their professional logic and influences their ambitions for venture growth. We draw on existing insights regarding the Darwinian, Communitarian, and Missionary orientation of entrepreneurs and on interviews with 29 founders to develop our hypotheses, which we then test in a sample of 58 academic and 113 non-academic founders that participated in a venture competition. We argue that, compared to non-academic institutional logics, academic logics are tied to a stronger Communitarian and Missionary orientation and a weaker Darwinian orientation in founders. A stronger Darwinian orientation values venture growth, whereas a stronger Communitarian orientation appraises the benefit of the technology for a restricted set of people at the expense of such growth ambitions. A stronger Missionary orientation values welfare maximization for society which may to some degree entail higher growth aspirations. We argue and empirically confirm that these identity orientations explain why academic founders hold lower growth aspirations for their start-up than non-academic founders. Our findings can at least partially clarify why academic start-ups do not grow according to expectancies. They theoretically advance our insights in academic entrepreneurship and founders' growth aspirations while also extending the literature on founders' identity orientation. © 2022"
doc=nlp(text=text)
word_dict={}
for word in doc:
    word=word.text.lower()
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1
#print(word_dict)

sentences=[]
sentence_score=0
for i,sentence in enumerate(doc.sents):
    for word in sentence:
        word=word.text.lower()
        sentence_score += word_dict[word]
    
    sentences.append((1,sentence.text.replace("\n"," "),sentence_score/len(sentence)))

#print(sentences)

sorted_sentences = sorted(sentences, key=lambda x: -x[2])

result=sorted(sorted_sentences[:5],key=lambda x: x[0])

summary_text=""

for sentence in result:
    summary_text += sentence[1]+" "

print(summary_text)