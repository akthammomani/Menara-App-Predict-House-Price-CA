# Menara App [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_red.svg)](https://blog.streamlit.io/monthly-rewind-june-2021/)
First and Only App for House Price Estimation, Forecast and GreatSchools Search

![house_8](https://user-images.githubusercontent.com/67468718/121798164-9ef30300-cbd9-11eb-822f-c4a996e184b7.JPG)

## **Introduction**
Whether you want to buy, sell, refinance, or even remodel a home, **MENARA** offers many resources, estimates and forecasts to help you make the most informed decision. 
With a user-friendly interface, and offering many resources for buyers, sellers, and landlords alike. **MENARA** offers:

  * The lowest 8.5% margin off error for off- market homes in North California ***(Competitive to the most known Home Estimate Sites e.g., [Redfin](https://www.redfin.com/redfin-estimate))*** by using the most sophisticated Machine learning Algorithms.

  * A golden opportunity to give you a sneak peek into the future; Up to 14 Months of house price forecast per zipcode 
    by using a new model called **Neural Prophet**.
    
  * A unique access to **[GreatSchools](https://www.greatschools.org/)**; the most trusted source of schools rating for many buyers and not just buyers with children because at **MENARA**  we KNOW that “location, location, location,” means “schools, schools, schools."

## **Menara Web App Deployment**

https://user-images.githubusercontent.com/67468718/122706472-dd597500-d20c-11eb-8834-3780f7cadf05.MP4
    
  * Streamlit Sharing: 

    [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_red.svg)](https://share.streamlit.io/akthammomani/streamlit/main/Menara_App.py/)
  
## **House Price Estimation**

At **MENARA**, since the begining, we made our mind to be unique in approaching this typical supervised machine learning problem, so here are the main reasons why you should trust our app: 

  * Built our dataset from scratch, utilizing multiple reliable sources (e.g., [redfin](https://www.redfin.com/news/data-center/), [realtor](https://www.realtor.com/research/data/), [GreatSchools API](https://www.greatschools.org/),.. etc). For more details, check [Data Wrangling](https://github.com/akthammomani/Capstone-Project-2-Menara-App-Predicting-House-Prices-CA/tree/main/Notebooks/Data_Wrangling).
  * Applied state of the art techniques in feature engineering: integrated Unsupervised Machine Learning - Clustering using K-Means and used Haversine Formula with Python to create crucial features in order to improve our final ML Model. For more details, check [pre_proccessing and Training Data](https://github.com/akthammomani/Menara-App-Predict-House-Price-CA/tree/main/Notebooks/Pre_processing_Training_Data).
  * Selected Stacking Regressor as our final Model because it managed to make predictions that have better performance than any single models we trained. so in Stacking, we used a meta-learning algorithm (Ridge) to learn how to best combine the predictions from Four ML Algorithms (Random Forest, GB, XGBoost and LightGBM).

![ML Models Summary](https://user-images.githubusercontent.com/67468718/122728305-d8a4b900-d22c-11eb-9e3f-781272140586.JPG)



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

