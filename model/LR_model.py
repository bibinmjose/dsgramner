import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from clean import clean_data
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import explained_variance_score
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.decomposition import PCA

# Loading dataset
marks = pd.read_csv('../gramener-usecase-nas/nas-pupil-marks.csv')

# Print the shape of raw data set
print ("Shape of raw Data\t:",marks.shape)

# name of featureset
category = ['State', 'District', 'Gender', 'Age', 'Category',
       'Same language', 'Siblings', 'Handicap', 'Father edu', 'Mother edu',
       'Father occupation', 'Mother occupation', 'Below poverty',
       'Use calculator', 'Use computer', 'Use Internet', 'Use dictionary',
       'Read other books', '# Books', 'Distance', 'Computer use',
       'Library use', 'Like school', 'Subjects', 'Give Lang HW',
       'Give Math HW', 'Give Scie HW', 'Give SoSc HW', 'Correct Lang HW',
       'Correct Math HW', 'Correct Scie HW', 'Correct SocS HW',
       'Help in Study', 'Private tuition', 'English is difficult',
       'Read English', 'Dictionary to learn', 'Answer English WB',
       'Answer English aloud', 'Maths is difficult', 'Solve Maths',
       'Solve Maths in groups', 'Draw geometry', 'Explain answers',
       'SocSci is difficult', 'Historical excursions', 'Participate in SocSci',
       'Small groups in SocSci', 'Express SocSci views',
       'Science is difficult', 'Observe experiments', 'Conduct experiments',
       'Solve science problems', 'Express science views', 'Watch TV',
       'Read magazine', 'Read a book', 'Play games', 'Help in household']

# target variables
target = ['performance','Maths %', 'Reading %', 'Science %', 'Social %']

# a new column "performance" is added to target as  
# average of ('Maths %', 'Reading %', 'Science %', 'Social %')
marks["performance"] = marks[['Maths %', 'Reading %', 'Science %', 'Social %']].mean(axis = 1, skipna = True)

# cleaning data into featureset(X) and target(y)
X,y = clean_data(marks, category, 'performance')

# printing the stats of cleaned data
print ("No. of null values in X:\n",X.isnull().sum())
print ("No. of null values in y:\n",y.isnull().sum())

# Creating a pipeline
pipe = Pipeline(steps  = [
       # ('poly',PolynomialFeatures(degree=2, interaction_only = False)), # Uncomment this line to include extra polynomial features
       # ('selK',SelectKBest(score_func = f_regression, k='all')),
       # ('pca',PCA(n_components = 10)),
       ('regression', LinearRegression(fit_intercept=True, normalize=True))
       ])
pipe.fit(X,y)

# Print the classifier 
print ("Classifier\t:",pipe)

# # features chosen by selectK
# f_chosen = X.columns[pipe.named_steps["selK"].get_support()]
# print("Chosen features\t:\n",f_chosen)

# Predicted values based on the model
y_pred = pipe.predict(X)

# variance explined by the model
print ("Explained Variance %\t:",explained_variance_score(y, y_pred)*100)

fig = plt.figure(figsize=(6,4))
plt.scatter(y,y_pred,alpha= 0.1)
plt.plot([0, 100], [0, 100], lw=4, color="k")
plt.xlabel('Measured Values')
plt.ylabel('Predicted Values')
plt.show()
fig.savefig("Model_Prediction.png")
