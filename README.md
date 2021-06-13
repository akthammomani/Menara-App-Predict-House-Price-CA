# Menara App
First and Only App for House Price Estimation, Forecast and GreatSchools Search

![SF_painted_ladies](https://user-images.githubusercontent.com/67468718/103456623-c483f400-4cac-11eb-8cdb-d508d23d80ba.jpg)

Whether you want to buy, sell, refinance, or even remodel a home, **MENARA** offers many resources, estimates and forecasts to help you make the most informed decision. 
With a user-friendly interface, and offering many resources for buyers, sellers, and landlords alike. **MENARA** offers:

  * The lowest 8.5% margin off error for off- market homes in North California ***(Competitive to the most known Home Estimate Sites e.g., [Redfin](https://www.redfin.com/redfin-estimate))*** by using the most sophisticated Machine learning Alogorithms.

  * A golden opportunity to give you a sneak peek into the future; Up to 14 Months of house price forecast per zipcode 
    by using a new model called **Neural Prophet**.
    
  * A unique access to **[GreatSchools](https://www.greatschools.org/)**; the most trusted source of schools rating for many buyers and not just buyers with children because at **MENARA**  we KNOW that “location, location, location,” means “schools, schools, schools."
 
## **House Price Estimation**

At **MENARA**, since the begining, we made our mind to be unique in approaching this typical supervised machine learning problem, so here are the main reasons why you should trust our app: 

  * Built our dataset from scratch, utilizing multiple reliable sources (e.g., [redfin](https://www.redfin.com/news/data-center/), [realtor](https://www.realtor.com/research/data/), [GreatSchools API](https://www.greatschools.org/),.. etc). For more details [Data Wrangling](https://github.com/akthammomani/Capstone-Project-2-Menara-App-Predicting-House-Prices-CA/tree/main/Notebooks/Data_Wrangling).
  * Applied state of the art techniques in feature engineering: integrated Unsupervised Machine Learning - Clustering using K-Means and used Haversine Formula with Python to create crucial features in order to improve our final ML Model.
  * Selected Stacking Regressor as our final Model because it managed to make predictions that have better performance than any single models we trained. so in Stacking, we used a meta-learning algorithm (Ridge) to learn how to best combine the predictions from Four ML Algorithms (Random Forest, GB, XGBoost and LightGBM).
