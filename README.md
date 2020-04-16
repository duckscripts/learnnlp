# Starting with spacy

##Installation

```
pip install spacy
```

## Understanding NLP
NLP suits are big beasts and some one new can start heading down rabbit whole and get very lost. These are a few basic 
points before diving in.

### Language Models 
The base of any NLP depends on language models.  What are language Models? In short they are the result of some one 
teaching an algorithm the constructs of a language based on training text.  Once the model has been "trained" it can be 
applied against any text of the same language. 

Spacy comes with pre-train models in meany languages. Since this is an 
this is and English language project, the English models will be disscussed below. There also other languages and they 
can be found on the [spcay models and languages](https://spacy.io/usage/models) page.

#### English Models
Spacy offers three English models that can be downloaded as apart of the library. 

+ en_core_web_sm
+ en_core_web_md
+ en_core_web_log

Currently I do not understand models. However choosing a model to use appears to have a cost verses the benefit of use.
According to to the [English model spacy site](https://spacy.io/models/en#en_core_web_sm) using the sm,md or log models 
will differ in accuracy (the benefit ) but will sacrifice space, time and computing power. 

Before using a model it will have to be downloaded:
```
python -m spacy download en_core_web_sm
```     

#### Tokens
Spacy pulls apart a sentence and breaks it down into it fundamental parts. This is called tokenisation. The spacy 
[API page for tokens](https://spacy.io/api/token) has a list of tokens that words will be defined as. But the below are
the most common ones 

| Token | Description |
|-------|-------------|
| Lemma_| Base form of the token, with no inflectional suffixes.  
| text  |
| pos_  | Coarse-grained part-of-speech.
| tag_  |
| dep_  |
| 

```python
import spacy
spacy.explain()
