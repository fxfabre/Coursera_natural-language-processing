# Machine translation

1. Find a corpus of french documents. And a corpus with similar documents in english.
2. Select a list of words in french and their translation in english
3. Compute word vector for each of this words, on their corpus
4. Create a matrix of french words containing the word vector in french. One word vector on each line.  
   And do the same in english
5. Let's call :
   - `X` the matrix of english word vector
   - `Y` the matrix of french word vector
   - `R` the translation matrix we want to compute, to solve `X.R = Y`
6. We use the frobenius norm to minimize (X.R - Y)


Why this way ?
No need to collect all french and english words to do this. 
Only a subset of the words is enough.
