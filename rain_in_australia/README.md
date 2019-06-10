## Will it Rain in Australia Tomorrow?

**Objective**
To predict whether or not it will rain anywhere in Australia tomorrow.

**Why do this?**
- Below are some use cases of this information: 
- Planning of irrigation and other farming activities
- Airplane route planning
- Construction activities scheduling 
- Extracurricular activities planning for school children

**The Dataset**
- Data was captured daily from numerous weather stations across Australia between 2007 and 2017.
- Contains 23 independent variables and 142,193 observations.
- There was a sizeable class imbalance, this prompted me to use the AUC ROC metric in model evaluation.

**Areas of Further Improvement**
- Further work could be done around feature engineering. For example, location could be converted into coordinates (i.e. latitude and longitude) of weather stations rather than encoding as dummies.
- Introducing elements of time and trends such as seasonality. For example we could dummify the time of day and the season of the year from when an observation was recorded.
- I could try more advanced models like Neural Networks. 

