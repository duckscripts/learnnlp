import spacy
nlp = spacy.load("en_core_web_sm")

#doc = nlp("I go. You go. We go. They go. I went. You went. We went. They went")
doc = nlp("I am going to the Apple shop and will eat an apple on the way ")
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha,
          token.is_stop, token.ent_type_)