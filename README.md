# Starting with spacy

## Installation

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

| Token | Description From Spacy                                                                                                                                                                                     |  Example |                            
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------- |
| Lemma_| Base form of the token, with no inflectional suffixes. To understand lemmatisation see the [Wikipedia article](https://en.wikipedia.org/wiki/Lemmatisation).                                     | The lemma for going, went, gone is "go" |  
| text  | Raw text                                                                                                                                                                                         | The raw text of the token |
| pos_  | Coarse-grained part-of-speech.                                                                                                                                                                   | The Coarse grain tag for Apple is "NOUN" |
| tag_  | Fine-grained part-of-speech.                                                                                                                                                                     | The fine grained tag for apple is "NN" this means "noun, singular or mass"|
| dep_  | Syntactic dependency. See the [wikipedia artical](https://en.wikipedia.org/wiki/Dependency_grammar#Syntactic_dependencies) |
| is_alpha | Does the token consist of alphabetic characters? | Characters of the token must within the alphabet. No numbers, operators or punctuation will the matched | 
| is_stop | Is the token part of a “stop list”? | Word that have no impact on a sentence like "I, a, was, not"|
| ent_type | Named entity type| Spacy has Named Entity Recognition (NER) and will attemped to determin the entity based ont he context of the sentence. IE Apple could be a organisation based on the context  |
### Understanding Tokens 
The pos_, tag_ and dep_ produce a lot shortened "codes" that are called annotations. These annotations  are documented on the [Spacy annotations](https://spacy.io/api/annotation).
Another way of finding what an annotation means is use the python console: 

```python
>>>import spacy 
>>>spacy.explain("NN")
'noun, singular or mass'
```
 Ofcourse one now need to understand what a 'noun, singular or mass' is

## Example 1

The code in example on does the following 
- Imports the spacy library 
```python
import spacy
```
- Load's the core English web SM model and creates the object "nlp"
```python
nlp = spacy.load("en_core_web_sm")
```
- Define the text to process by calling the "nlp" object and assigning the results to "doc"

```python
doc = nlp("I am going to the Apple shop and I will eat an apple on the way ")
```
- With a for loop reiterate over the object "doc" printing out the doc attributes 
```python 
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.is_alpha,
          token.is_stop, token.ent_type_)
```

The out put of example-1.py will be:
```
I -PRON- PRON PRP nsubj True True 
am be AUX VBP aux True True 
going go VERB VBG ROOT True False 
to to ADP IN prep True True 
the the DET DT det True True 
Apple Apple PROPN NNP compound True False ORG
shop shop NOUN NN pobj True False 
and and CCONJ CC cc True True 
will will AUX MD aux True True 
eat eat VERB VB conj True False 
an an DET DT det True True 
apple apple NOUN NN dobj True False 
on on ADP IN prep True True 
the the DET DT det True True 
way way NOUN NN pobj True False 
```

## Example 2 

Went learning a new langauge, learning how verbs are used and constructed is fundamental. I am going to take this 
approach with learning spacy and see if it works. 

### Finding the verb 

There are two ways that I found to to discover a verb using spacy and this is using the  Coarse-grained part-of-speech 
(pos_) token and the  Fine-grained part-of-speech (tag_) token and both are using for different reasons.

#### Coarse-grained part-of-speech

THe following line of code should be added to the for loop in example 1.  

```python
if token.pos_ == "VERB":
```

The above if statement will pull out any pos_ token that matches the value "VERB", a verb. The out put the the following:
```
going go VERB VBG ROOT True False 
eat eat VERB VB conj True False 
```

Two verbs are discovered with in the document; "going" and "eat". While this is a good start it will be impossible to 
understand the types of verbs, this is where the Fine-grained part-of-speech token comes in to play.

#### Fine-grained part-of-speech

The output of example 2 contains the values of tag_ these are the following "VB" for the ver eat and VBG for the verb going.
Using spacy.explain we can identify that the tags mean: 

VBG
```python
spacy.explain("VBG")
'verb, gerund or present participle'
```

This is where understanding of grammar becomes more important and will influence how you code. I will not go into detail
on grammar as I am not very good. At a high level a gerund is a noun acting as a verb and  a participle verb that is 
used to indicate a past or ongoing action and the present participle ushalling has an "ing" at the end of the verb 
indicating a progressive tenses. Google these terms to find out more 

VB
```python
spacy.explain("VB")
'verb, base form'
```