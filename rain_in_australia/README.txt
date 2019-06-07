WIll it Rain in Australia Tomorrow?  - Machine Learning Project

Objective:
To predict whether or not it will rain anywhere in Australia tomorrow.

Why do this?
Below are some use cases of this information: 
*Planning of irrigation and other farming activities
*Airplane route planning
*Construction activities scheduling 
*Extracurricular activities planning for school children

The Dataset:
*Data was captured daily from numerous weather stations across Australia between 2007 and 2017.
*Contains 23 independent variables and 142,193 observations.
*There was a sizeable class imbalance, this prompted me to use the AUC ROC metric in model evaluation.

Areas of Further Improvement:
*Further work could be done around feature engineering. For example, location could be converted into coordinates(i.e latitude and longitude) of weather stations rather than encoding as dummies.
*Introducing elements of time and trends such as seasonality. For example we could dummify the time of day and the season of the year from when an observation was recorded.
*I could try more advanced models like Neural Networks.


Proposed solution
In this project I will build a multinomial classifier that will be able to detect, give the sizes as well as localize potholes on a road surface. I’m proposing to use the Artificial Neural network Technique. 

Project goals and milestones:
The end goal of the project is to create a model that will be able to detect and localize potholes. The first milestone is create a binary classifier. If that is successful, next I will create a regression model for predicting the upper left and lower right coordinates of bounding boxes around the pothole.

Areas of commercial application
•	Insurance – to aid objective vehicle insurance premium calculation
•	Road network maintenance - government agencies 
•	Autonomous vehicle  vision

Data source
The dataset I’m proposing to use was sourced from an academic research paper in which the author employed colour segmentation to identify road irregularities on road surfaces. That data was made available to the public through a shared google drive folder. 

Data Access: 
I have cloned a copy of the data folder in my google drive from which the model will access the images as well as the annotation files.


