# Classificazione

# K-Nearest Neighbor(KNN) Algorithm

KNN works by identifying the K closest data points to a given input and making predictions based on the majority class or average value of those neighbors.

KNN is also called as a lazy learner algorithm because it does not learn from the training set immediately instead it stores the entire dataset and performs computations only at the time of classification.

## What is 'K' in K Nearest Neighbour?
In the KNN algorithm k is just a number that tells the algorithm how many nearby points or neighbors to look at when it makes a decision.
Choosing the right k is important for good results.

## How to choose the best k?
Why you shouldn’t pick k “by eye”
- k too small (e.g., 1): high variance, very sensitive to noise → tends to overfit.
- k too large: high bias, the decision boundary becomes overly smooth → tends to underfit.

## Statistical Methods for Selecting k
- Cross-Validation: Cross-Validation is a good way to find the best value of k is by using k-fold cross-validation. This means dividing the dataset into k parts. The model is trained on some of these parts and tested on the remaining ones. This process is repeated for each part. The k value that gives the highest average accuracy during these tests is usually the best one to use.
- Elbow Method: In Elbow Method we draw a graph showing the error rate or accuracy for different k values. As k increases the error usually drops at first. But after a certain point error stops decreasing quickly. The point where the curve changes direction and looks like an "elbow" is usually the best choice for k.
- Odd Values for k: It’s a good idea to use an odd number for k especially in classification problems. This helps avoid ties when deciding which class is the most common among the neighbors.

## Distance Metrics Used in KNN Algorithm

### Euclidean Distance
![Euclidean](images/euclidean.png)

### Manhattan Distance
![Manhattan](images/manhattan.png)

### Minkowski Distance
![Minkoski](images/minkowski.png)
## Working of KNN algorithm 
4 steps
- step 1: Selecting the optimal value of k
- step 2: Calculating distance
- step 3 : Finding Nearest Neighbors
- step 4: Voting for Classification or Taking Average for Regression




# Multinomial logistic regression 

Multiclass logistic regression is a machine learning method used when the target variable has more than two categories. Unlike binary logistic regression which predicts two outcomes it helps classify data into three or more classes. It works by estimating the probability of each class and selecting the one with the highest probability as the prediction.


## How does it Work
Multiclass logistic regression works by extending binary logistic regression to handle more than two classes.
Instead of just separating two categories it calculates the probability of each class using the softmax function which ensures that the sum of all class probabilities is 1. During training the model learns separate weight vectors for each class.
For a given input it computes a score for each class using dot product of weights and input features then applies softmax to convert these scores into probabilities. The class with the highest probability is chosen as the predicted label.
This method is effective when the data is linearly separable and belongs to one of several mutually exclusive categories.
