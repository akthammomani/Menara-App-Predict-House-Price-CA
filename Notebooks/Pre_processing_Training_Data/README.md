
# Pre-processing and Training Data Development: Predicting House Prices in North California

![_pre_proc](https://user-images.githubusercontent.com/67468718/111041698-64b57200-83ee-11eb-96ff-b64c11a36c04.JPG)

## 1. Introduction

The pre-processing and Training data is considered as the final step for data manipulation, where we can make sure that: 

 * No Outliers
 * No missing data
 * Features Engineering: 
   * Engineer New Features
   * Drop Features
   * Change features structure
   * Encode Features
   * Train and test split the data set


## 2. Removing Outliers:
  #### 2.1 Target Variable "price" Visualization with Outliers boundaries using Quantile and Standrad Deviation:
  ![standard_price](https://user-images.githubusercontent.com/67468718/111862529-21d62b80-8913-11eb-9369-0dfb1449fe9d.JPG)
  ![quant_price](https://user-images.githubusercontent.com/67468718/111862528-213d9500-8913-11eb-802e-918ee468b391.JPG)
 
  #### 2.2 Visualization all difference datasets based on multiple outliers method: Target Variable "price" Visualization using different datasets:
  ![datasets](https://user-images.githubusercontent.com/67468718/111862562-5ba73200-8913-11eb-8fa4-e503f47f647c.JPG)

  #### 2.3 Datasets comparison using statistics summary: 
  
  According to the below table, std_df is showig the best, mean, std by eliminating all data greater than 1.2 standard deviation from the mean and at the same we managed only to lose 687 outliers.
  ![stat_sum](https://user-images.githubusercontent.com/67468718/111862620-96a96580-8913-11eb-8115-fc35fb887f40.JPG)
 
  #### 2.4 Datasets comparision using Correlation and Applying conditional formatting: 
  
  According to the below datasets, std_df is again showig the best correlation between our target variable (price) and all other features when we compare all datasets.
  ![corr](https://user-images.githubusercontent.com/67468718/111862703-3ebf2e80-8914-11eb-9c60-31ed974224df.JPG)

  #### 2.5 Visualizing House Sales vs Median Income and School Rating using Plotly and Mapbox:
  ![plotly_sales](https://user-images.githubusercontent.com/67468718/111863038-44b60f00-8916-11eb-809b-2b8ac518bbca.JPG)
  
## 3. Features Engineering:
  #### 3.1 Introducing New Features
   * Let's create New 3 categorical  features (boolean variables): 
       * barts: 1 yes barts and 0 no barts 
       * malls: 1 yes malls and 0 no malls
       * universities: 1 yes universities and 0 no Universities 
   * Beds_Baths_tradeoff (bedBath) = beds * baths
   * AvgRoomSize = sqft / (beds + baths)

  #### 3.2 Dropping and encoding Features
   * Let's drop 'address', 'malls_count', 'bart_count', 'lat', 'long'
   * After we drop the above columns, that means we still have one column with 'object' datatype which is 'property_type', so let's encode it manually:
       * Single Family Residential == 0
       * Condo/Co-op == 1
       * Townhouse == 2
  #### 3.3 Final Visualization of our Target Variable 'price':
  ![final_price_mean](https://user-images.githubusercontent.com/67468718/111863365-657f6400-8918-11eb-84dc-b28dc3d61988.JPG)
  
## 4. Linear Regression:

Making a Linear Regression model: our first baseline model. Sklearn has a LinearRegression() function built into the linear_model module. We'll be using that to make our first regression model.

  #### 4.1 Linear Regression: Residuals Visualization
  
  As we can see below by visualizing the residual we can see that is normally distributed which is a good indication that we're having a linear relationship with our dependent variable 'price'.
  ![resid](https://user-images.githubusercontent.com/67468718/111863615-e9861b80-8919-11eb-8d24-e5272016fc90.JPG)
  
  #### 4.2 Linear Regression Model Evaluation
  
  As we can see, the value of **root mean squared error (RMSE) is 98397.45**, which is slightly larger than 10% of the mean value of the Sales Price i.e.  $887,769.19. also, we have **very good variance score at 93.5%. This means that our initial algorithm is working and we're in the right track.**
  
  |<code>**Metrics**</code>|<code>**Score**</code>|
  |:-----------------------|:--------------------:|
  |Linear Regression - r2 |93.45 %|
  |Linear Regression - MAE|69515.8128|
  |Linear Regression - MSE|9682059380.4424|
  |Linear Regression - RMSE|98397.4562|
  |Linear Regression - Variance|93.45 %|
  
  #### 4.3 Linear Regression model: predictions vs. the actual values
  
  ![actual_pred](https://user-images.githubusercontent.com/67468718/111864397-db39fe80-891d-11eb-83c7-8a7e6b397585.JPG)
  
## 5. Models next step:

Now, after building our base Model: Linear regression, let's see if we can further improve our prediction using below algorithms:

 * Ridge Regression (L2 Regularization)
 * Lasso Regression (L1 Regularization)
 * Decision Trees
 * Random Forests
 * GB
 * XGBoost
 * Stacking
 * Neural networks.

