# Vector spaces models

## Co-occurence matrix : Word by word and word by doc
Let's define :
- word a = simple
- word b = data
- distance k = 2

Exemple with sentenses :
- I like simple data : a and b have a distance of 1
- I prefer simple raw data : a and b have a distance of 2

### Word by word design
Number of times word `a` and word `b` occur together within a certain distance `k`  

|      | simple | raw  | like | I   |
|------|--------|------|------|-----|
| data | 2      | 1    | 1    | 0   |

### Word by document design
Number of times a word occurs within a certain category

1. Divide the corpus in different categories. Ex : Entertainment, Economy, Science
2. Count the number of time the word appears inside each category

|      | Entertainment | Economy | Science |
|------|---------------|---------|---------|
| data | 500           | 6600    | 9300    |
| film | 9000          | 4000    | 300     |

## Word vector
We can use each array to define word vectors.

With the word by document design, we can define a vector for each category :
- Entertainment = (500, 9000)

Same with the word by word design


## Distances
- Euclidean distance : `np.linalg.norm(a - b)`
- Cosine Similarity : better when corpora are different sizes
