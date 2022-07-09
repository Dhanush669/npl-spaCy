import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp('I got a slowly red candy and an interesting and big book.')
noun_adv = []
for chunk in doc.noun_chunks:
    adj = []
    noun = ""
    for tok in chunk:
        if tok.pos_ == "NOUN":
            noun_adv.append(tok.text)
        if tok.pos_ == "ADV":
            noun_adv.append(tok.text)
# expected output
print(noun_adv)