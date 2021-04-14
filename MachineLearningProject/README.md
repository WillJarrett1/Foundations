# Machine learning project | News articles and anger
### 06/04/2021

I analyzed a dataset of news organization Facebook posts, trying to see which words in the post and the comments led to an angry reaction to the news (measured in the proportion of 'angry reacts' compared to all other reactions).

I used the dataset posted here: https://github.com/jbencina/facebook-news.

#### Angriness and post words
I labelled the data by marking any news story with 30% or more angry reacts as 'angry'. Then I used I used TfidfVectorizer to see if the words of the post could be used to predict which stories are angry and which aren't. Using a RandomForestClassifier, this led to an accuracy of 0.97 and a decent-looking confusion matrix. to see if the words of the post could be used to predict which stories are angry and which aren't. Using a RandomForestClassifier, this led to an accuracy of 0.97 and a decent-looking confusion matrix.

The results show (perhaps unsurprisingly) that "trump", "republican", and "president" were in the top ten words for predicting an angry reaction to a news story. "Health care", "epa", and "cuts" were also high up on the list, suggesting that political issues lead to some of the angriest reactions. However, the uncertainty of some of these features is higher than its weight, so they are not all brilliant predictors.

#### Angriness and comments
I aggregated all the comments on each post and then fed them into the TfidfVectorizer. That way, we can see what people are talking about when they are angry about news stories. Accuracy was 0.98 and the confusion matrix looked very good.

The top twenty words here include "administration", "wrong", "greedy", "despicable", "voters", "traitors", "police", "tax break", and "democracy". Again, it seems that political issues are the biggest predictor of an angry reaction to news. But this time around, every feature has a higher uncertainty than weight. I think a larger sample size is needed to prove that this pattern holds more generally.

NOTE: Source files seemed to be too big to commit via Github Desktop.

### UPDATE 14/04/2021
Jupyter notebook now includes classifications of angry comments/posts from MSNBC and Fox News, to see what kind of news makes people react angrily from different sides of the political spectrum.