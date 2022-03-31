# Natural Language Processing with Classification and Vector
https://www.coursera.org/learn/classification-vector-spaces-in-nlp#syllabus

## Chapter 1 : Sentiment Analysis with Logistic Regression


#### Vectoriser une phrase :
Solution 1 : définir un vocabulaire avec tous les mots possibles.  
- Vocabulaire V de taille |V| = nombre de mots w différents  
- Une phrase est représentée par un vecteur [0, 1, 0, 0, ..., 1, 0] avec des 1 à la position des mots qui sont dans la phrase
- Problème : Beaucoup de paramètres &theta; à entrainer : 1 par mot.

#### Solution 2 : Pour un problème de classification de sentiments (+/-) : 2 classes possibles 0 (négatif) ou 1 (positif)  
- Vecteur de dimension 3 par phrase : [1, X, Y]
  On calcule d'abord le nombre d'occurences
- Pour un mot w, PosFreq(w) = nombre d'occurences du mot w dans l'ensemble des documents positifs (classs 1)
- Idem pour NegFreq, avec la classe négative (classe 0)
- On utilise ces (PosFreq, NegFreq) établis sur la base d'apprentissage pour classer une nouvelle phrase.  
  1. On tokenise la phrase pour obtenir les words.
  2. On supprime les doublons (on garde un set des mots)
  3. On calcule les sommes sur ce set, avec w un mot :
     X = &Sigma;<sub>w</sub> PosFreq(w)  
     Y = &Sigma;<sub>w</sub> NegFreq(w)

#### Pré-processing
- Tokenize
- Suppression des "stop words" : mots de liaison, ne comportenant généralement pas de sens  
  Exemple : et, ou, ...  
- Suppression de la ponctuation  
  Attention, un point d'exclamation peut être utile à garder pour analyser le sentiment  
- Lowercase  
- Lemmatisation / Stemming  
