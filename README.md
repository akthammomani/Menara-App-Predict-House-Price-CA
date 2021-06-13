# Menara App
First and Only App for House Price Estimation, Forecast and GreatSchools Search

![house_8](https://user-images.githubusercontent.com/67468718/121798164-9ef30300-cbd9-11eb-822f-c4a996e184b7.JPG)

Whether you want to buy, sell, refinance, or even remodel a home, **MENARA** offers many resources, estimates and forecasts to help you make the most informed decision. 
With a user-friendly interface, and offering many resources for buyers, sellers, and landlords alike. **MENARA** offers:

  * The lowest 8.5% margin off error for off- market homes in North California ***(Competitive to the most known Home Estimate Sites e.g., [Redfin](https://www.redfin.com/redfin-estimate))*** by using the most sophisticated Machine learning Alogorithms.

  * A golden opportunity to give you a sneak peek into the future; Up to 14 Months of house price forecast per zipcode 
    by using a new model called **Neural Prophet**.
    
  * A unique access to **[GreatSchools](https://www.greatschools.org/)**; the most trusted source of schools rating for many buyers and not just buyers with children because at **MENARA**  we KNOW that “location, location, location,” means “schools, schools, schools."
 
## **House Price Estimation**

At **MENARA**, since the begining, we made our mind to be unique in approaching this typical supervised machine learning problem, so here are the main reasons why you should trust our app: 

  * Built our dataset from scratch, utilizing multiple reliable sources (e.g., [redfin](https://www.redfin.com/news/data-center/), [realtor](https://www.realtor.com/research/data/), [GreatSchools API](https://www.greatschools.org/),.. etc). For more details, check [Data Wrangling](https://github.com/akthammomani/Capstone-Project-2-Menara-App-Predicting-House-Prices-CA/tree/main/Notebooks/Data_Wrangling).
  * Applied state of the art techniques in feature engineering: integrated Unsupervised Machine Learning - Clustering using K-Means and used Haversine Formula with Python to create crucial features in order to improve our final ML Model. For more details, check [pre_proccessing and Training Data](https://github.com/akthammomani/Menara-App-Predict-House-Price-CA/tree/main/Notebooks/Pre_processing_Training_Data).
  * Selected Stacking Regressor as our final Model because it managed to make predictions that have better performance than any single models we trained. so in Stacking, we used a meta-learning algorithm (Ridge) to learn how to best combine the predictions from Four ML Algorithms (Random Forest, GB, XGBoost and LightGBM).

|No.|Models| R^2 Score|Adjusted R^2 Score  |  MAE  | RMSE|Variance Score|
|:----:|:----------------------|:-------:|:-------:|:----:|:----:|:----:|
|1|[Dummy Regression](https://github.com/akthammomani/Menara-App-Predict-House-Price-CA/blob/main/Notebooks/Modeling/Modeling_Dummy_Linear_Regression.ipynb)|0 %|0 %|301148.2119|376306.4570|0 %|
|2|[Linear Regression](https://github.com/akthammomani/Menara-App-Predict-House-Price-CA/blob/main/Notebooks/Modeling/Modeling_Dummy_Linear_Regression.ipynb) |87.0594 %|86.9199 %|96522.4628|135367.8835|87.0805 %|
|3|[Tuned Ridge](https://github.com/akthammomani/Menara-App-Predict-House-Price-CA/blob/main/Notebooks/Modeling/Modeling_Ridge_Regression_(L2_Regularization).ipynb)|87.0763 %|86.9369 %|96489.2726|135279.9288|87.0970 %|
|4|[Tuned Lasso](https://github.com/akthammomani/Menara-App-Predict-House-Price-CA/blob/main/Notebooks/Modeling/Modeling_Lasso_Regression_(L1_Regularization).ipynb)|87.0595 %|86.9200 %|96520.8254|135367.3967|87.0806 %|
|5|[Tuned Decision Tree](https://github.com/akthammomani/Menara-App-Predict-House-Price-CA/blob/main/Notebooks/Modeling/Modeling_Decision_Tree_Regression.ipynb)|87.4464 %|87.3110 %|92510.0434|133328.6903|87.4864 %|
|6|[Tuned ANN](https://github.com/akthammomani/Menara-App-Predict-House-Price-CA/blob/main/Notebooks/Modeling/Modeling_Neural_Networks_Keras_Tensorflow.ipynb)|91.0938 %|90.9978 %|76641.2342|112301.3342|91.1308 %|
|7|[Tuned Random Forests](https://github.com/akthammomani/Menara-App-Predict-House-Price-CA/blob/main/Notebooks/Modeling/Modeling_Random_Forest_Regression_V1.ipynb)|92.1982 %|92.1141 %|67886.0897|105107.8895|92.2170 %|
|8|[Gradient Boosting]()   |92.4799 %|92.3988 %|66910.7055|103193.3274|92.4863 %|
|9|[Tuned XGBoost](https://github.com/akthammomani/Menara-App-Predict-House-Price-CA/blob/main/Notebooks/Modeling/Modeling_XGBoost_Regression.ipynb)   |92.5777 %|92.4977 %|67043.7283|102520.0032|92.5786 %|
|10|[Tuned LightGBM](https://github.com/akthammomani/Menara-App-Predict-House-Price-CA/blob/main/Notebooks/Modeling/Modeling_LightGBM_Regression.ipynb)|92.6304 %|92.5510 %|66235.3892|102155.1713|92.6406 %|
|11|[Baseline Stacking](https://github.com/akthammomani/Menara-App-Predict-House-Price-CA/blob/main/Notebooks/Modeling/Modeling_Stacking_Regression_Final_APP.ipynb)|92.4033 %|92.3214 %|68855.7449|103717.3961|92.4168 %|
|12|[**Tuned Stacking - Winner** ](https://github.com/akthammomani/Menara-App-Predict-House-Price-CA/blob/main/Notebooks/Modeling/Modeling_Stacking_Regression_Final_APP.ipynb)  |92.7615 %|92.6835 %|65381.7572|101242.5730|92.7760 %|


## **Median House Price Forecast Per Zip Code**

If you're interested in buying or selling a house in 2021/2022, then, **MENARA** is offering a golden opportunity to give you a sneak peek into the future; Up to 14 Months of house price forecast per zipcode by using a new model called **[Neural Prophet](https://github.com/akthammomani/Menara-App-Predict-House-Price-CA/tree/main/Notebooks/Neural-Prophet-Forecast)**. This model is a Neural Network based Time-Series Model, built on top of PyTorch and is heavily inspired by Facebook Prophet and AR-Net libraries **([Neural Prophet Site](http://neuralprophet.com/))**.

For the Data used in **Neural Prophet**, we're utilizing multiple reliable sources **(e.g., [redfin](https://www.redfin.com/news/data-center/) and [realtor](https://www.realtor.com/research/data/))**, because they have direct access to data from local multiple listing services, as well as insight from their real estate agents across the country.

![forecast_example](https://user-images.githubusercontent.com/67468718/121798466-62c0a200-cbdb-11eb-88cd-acc097b86526.JPG)

## **GreatSchools Search**

Most buyers understand that they may not be able to find a home that covers every single item on their wish list, but new survey data from **[realtor](http://wwww.realtor.com)** shows that school districts are an 
area where many buyers aren’t willing to compromise. For many buyers and not just buyers with children, “location, location, location,” means “schools, schools, schools.”

Good schools desire by **78%** of buyers makes **[GreatSchools](https://www.greatschools.org/)** the trusted source of schools rating for many parents and the partner of choice for so many leading real estate websites (e.g., redfin, zillow, realtor) simply because **GreatSchools** are the nation’s leading source of school performance information and offer the most comprehensive set of school data available. Last year,  **GreatSchools** had more than 55 million unique visitors, including over half of American families with school-age children.

Special Thanks to **GreatSchools**, in particular Lindsay Zavala - Partnership Manager for providing a **free API trial key**. REST API access was essential to request GreatSchools Rating of all schools in specific zipcodes/Cities in North California.

![school_example](https://user-images.githubusercontent.com/67468718/121798875-9f8d9880-cbdd-11eb-8af8-a52b07639181.JPG)

