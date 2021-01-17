# Exploratory Data Analysis: Predicting House Prices in North California

## Introduction

Now that we’ve obtained, cleaned, and wrangled our dataset into a form that's ready for analysis, it’s time to perform exploratory data analysis (EDA).

![EDA_1](https://user-images.githubusercontent.com/67468718/104575188-b8ccf180-560b-11eb-8037-d5b75029eb31.JPG)

## Objective

   * To get familiar with the features in our dataset.
   * Generally understand the core characteristics of our cleaned dataset. 
   * Explore the data relationships of all the features and understand how the features compare to the response variable.
   * Let's be creative and think about interesting figures and all the plots that can be created to help deepen our understanding of the data.
   
 
## Initial Statistics Summary

| <code>Stats</code> |  <code>Summary</code>|
|:--- |:--- |
|Avg Houses Price |1,058,497 USD|
|Std|948,060.35 |
|Min House Price |1.600 USD|
|Q1 |607,000 USD|
|Median House Price |835,000 USD|
|Q3 |1,250,000 USD |
|Max House Price|39,988,000 USD |
|House Count |8918 |

## Dataset Summary and Objective (Final Modifications)

  * <code>**Missing Values (NANs)**</code>: There's no NANs in the df.
  * <code>**Concatenate columns**</code>: Some of the columns need to be merged togethor for better visibility.
  * <code>**Insignificant Columns**</code>: Check if all columns are significant, otherwise let's drop them.  
  * <code>**Duplicates**</code>: Explore the columns to make sure no duplicates.  
  * <code>**Renaming Columns**</code>: Some of the column's Labels need to be modified to correctly represent the underlined information.
  * <code>**Wrong Values**</code>: Check if all our data is valid even though during Data Wrangling there was extensive process to impute wrong values either by correcting the values or dropping the rows.  
  * <code>**price**</code>: Check for any outliers so we can eliminate to better analyze the data. 
  
 ## Main Features:
 
   * **Numerical Variables:** <code>'price'</code>, <code>'sqft'</code>, <code>'price_per_sqft'</code>, <code>'lot_size'</code>, <code>'hoa_month'</code> and <code>'property_age'</code>
   * **Categorical Variables:** <code>'beds'</code>, <code>'baths'</code>, <code>'school_rating'</code>, <code>'school_count'</code>, <code>'median_income'</code>, <code>'malls_count'</code> and <code>'universities_count'</code>
   * Please note we'll be using a scatterplot to investigate **Numerical Variables** and will be using a combination of **scatterplot, boxplot and stripplot.** to investigate **Categorical Variables**
   * Please find below the main features before and after dealing with outliers in the Dataset ( Outliers were eliminated by imputing with correct values or using mean() or median() or dropping them):
   
 ### <code>'price'</code>:
   * Before:
![price_1](https://user-images.githubusercontent.com/67468718/104831551-e2219380-583e-11eb-8d47-2cfbd22df1e1.JPG)   
   * After: 
![price_2](https://user-images.githubusercontent.com/67468718/104831552-e2219380-583e-11eb-9793-02d9fc506321.JPG)  

 ### <code>'sqft'</code>:
   * No Outliers: We see clear positive correlation between <code>'price'</code> & <code>'sqft'</code>:
![sqft](https://user-images.githubusercontent.com/67468718/104831557-e352c080-583e-11eb-95fb-943fec5a8c9a.JPG)

 ### <code>'price_per_sqft'</code>:
   * Before:
![price_sqft_1](https://user-images.githubusercontent.com/67468718/104831554-e2ba2a00-583e-11eb-9099-2d99dfdf7540.JPG)
   * After: We see clear positive correlation between <code>'price'</code> & <code>'price_per_sqft'</code>:
![price_sqft_2](https://user-images.githubusercontent.com/67468718/104831555-e352c080-583e-11eb-8d41-13b166765702.JPG)

 ### <code>'lot_size'</code>:
   * Before:
![lot_size_1](https://user-images.githubusercontent.com/67468718/104831546-e0f06680-583e-11eb-89f6-51316be34757.JPG)
   * After:  We see clear positive correlation between <code>'price'</code> & <code>'lot_size'</code>:
![lot_size_2](https://user-images.githubusercontent.com/67468718/104831547-e188fd00-583e-11eb-8e46-4f42790ac6b3.JPG)

### <code>'hoa_month'</code>:
   * Before:
![hoa_per_month_1](https://user-images.githubusercontent.com/67468718/104831544-e0f06680-583e-11eb-8f74-dd09d6e0d369.JPG)
   * After: We see clear negative correlation between <code>'price'</code> & <code>'lot_size'</code>:
![hoa_per_month_2](https://user-images.githubusercontent.com/67468718/104831545-e0f06680-583e-11eb-9c16-5ece6ef35fc5.JPG)

 ### <code>'beds'</code>:
   * Before:
![beds_1](https://user-images.githubusercontent.com/67468718/104831535-de8e0c80-583e-11eb-9589-b39f97faeb3c.JPG)
   * After: We see clear positive correlation between <code>'price'</code> & <code>'beds'</code>:
![beds_2](https://user-images.githubusercontent.com/67468718/104831537-df26a300-583e-11eb-868f-7ae00328a721.JPG)

 ### <code>'baths'</code>:
   * No Outliers: We see clear positive correlation between <code>'price'</code> & <code>'baths'</code>:
![baths_1](https://user-images.githubusercontent.com/67468718/104831534-ddf57600-583e-11eb-9c25-1346773f8c97.JPG)

 ### <code>'school_rating'</code>:
   * No Outliers: We see clear positive correlation between <code>'price'</code> & <code>'school_rating'</code>:
![school_rating](https://user-images.githubusercontent.com/67468718/104831556-e352c080-583e-11eb-96af-2ceb10abe826.JPG)

 ### <code>'median_income'</code>:
   * No Outliers: We see clear positive correlation between <code>'price'</code> & <code>'median_income'</code>:
![median_income](https://user-images.githubusercontent.com/67468718/104831550-e2219380-583e-11eb-87b7-a794270193eb.JPG)

 ### <code>'malls_count'</code>:
   * No Outliers: We see some correlation between <code>'price'</code> & <code>'malls_count'</code>:
![malls_count](https://user-images.githubusercontent.com/67468718/104831548-e188fd00-583e-11eb-8032-dacd32674442.JPG)

 ### <code>'university_count'</code>:
   * No Outliers: We see clear positive correlation between <code>'price'</code> & <code>'university_count'</code>:
![university_count](https://user-images.githubusercontent.com/67468718/104831558-e3eb5700-583e-11eb-847a-797a901bc463.JPG)


 ## Main Features:
 
   * **Pairplot:** let's use pairplot from seaborn to plot our dependant variable **'price'** against the main features:
**'beds'**, **'property_type'**, **'baths'**, **'sqft'**, **'school_rating'**, **'school_count'**, **'bart_count', **''median_income'**, **''lot_size'**, **''hoa_month'**, **'malls_count'**, **'university_count'** per **'property_type'**.

![corr_per_property_type](https://user-images.githubusercontent.com/67468718/104831540-dfbf3980-583e-11eb-8d08-99d1cfd057ad.JPG)

   * **Heatmap:** let's use heatmap from seaborn to Check the correlation between our dependant variable **'price'** against the main features:
**'beds'**, **'property_type'**, **'baths'**, **'sqft'**, **'school_rating'**, **'school_count'**, **'bart_count', **''median_income'**, **''lot_size'**, **''hoa_month'**, **'malls_count'**, **'university_count'** per **'property_type'**.

![heatmap](https://user-images.githubusercontent.com/67468718/104831542-e057d000-583e-11eb-9b50-19f36f2cb191.JPG)


   
 ### Price: Our dependent variable:

   * Original Data was having 8917 Observations and 26 variables (Output from Data Wrangling Part).
   * There was modifications in the dataframe which focused mainly in eliminating the outliers as much as possible:
    - <code>**Missing Values (NANs)**</code>: There's no NANs in the df.
    - <code>**Concatenate columns**</code>: For better visibility, we merged <code>**'address'**</code>, <code>**'city'**</code> , <code>**'state'**</code>, and <code>**'zipcode'**</code> into one column called <code>**'address'**</code>.
    - <code>**Insignificant Columns**</code>: We dropped <code>**'address'**</code>, <code>**'city'**</code> , <code>**'state'**</code>, <code>**'year_built'**</code>, <code>**'address_m'**</code> and <code>**'year_built'**</code> column was transformed into column <code>'property_age'</code>.
    - <code>**Duplicates**</code>: We removed 567 complete duplicates (Observations having the same variables) from <code>**'address'**</code>
    - <code>**Renaming Columns**</code>: We renamed all columns to improve visibility.
    - <code>**Wrong Values**</code>: We divided the variables into 2 categories: Numerical and categorical as below:
      * **Numerical Variables:** <code>'price'</code>, <code>'sqft'</code>, <code>'price_per_sqft'</code>, <code>'lot_size'</code>, <code>'hoa_month'</code> and <code>'property_age'</code>
      * **Categorical Variables:** <code>'beds'</code>, <code>'baths'</code>, <code>'school_rating'</code>, <code>'school_count'</code>, <code>'median_income'</code>, <code>'malls_count'</code> and <code>'universities_count'</code>
      * We used scatterplot to investigate **Numerical Variables** and a combination of **scatterplot, boxplot and stripplot.** to investigate **Categorical Variables**
      * Main target of this section was to eliminate outliers and impute and fix wrong values.
      * We reduced <code>**'property_type'**</code> from 5 to 3 and we focused mainly in **Single Family Residential**, **Condo/Co-op** and **Townhouse** anything else was dropped (165 rows).
      * We dropped 11 rows associated with <code>**'Beds'**</code> >30 and <code>**'Beds'**</code>=0 (wrong values). also we fixed 5 houses after we imputed the correct values (source: http://www.zillow.com).
      * We found 1 outlier at <code>**'price_per_sqft''**</code> and we imputed the correct values (source: http://www.zillow.com) 593 USD instead of 592,692 USD.
      * We found 163 outliers at <code>**'lot_size'**</code> and we imputed the median values=5,760 Sq. Ft. (all values at these rows initially were wrong >40,000 Sq. Ft).
      * We found 7 outliers at <code>**'hoa_month'**</code> and we imputed the mean values=115.92 USD (all values at these rows initially were wrong >1,500 USD).
    - <code>**'price'**</code>: This was the main focus in imputing wrong values and elimintaing outliers:
      * We dropped **7 houses > 14M USD**
      * We fixed one wrong house price from 1,600 USD to 794,126 USD
      * Pairplot and heatmap revealed that we have strong correlation between <code>**'price'**</code> and <code>**'beds'**</code>, <code>**'baths'**</code> , <code>**'sqft'**</code>, <code>**'lot_size'**</code>, <code>**'price_per_sqft'**</code>, <code>**'school_rating'**</code>, <code>**'median_income'**</code> and <code>**'university_count'**</code>.
      * Further fine tuning in term of house price ranges revleaed that when we keep only houses with price tag between 300K USD and 2M USD we see the highest correlation between  <code>**'price'**</code> and the above features (775 Houses were dropped) as shown below:
       - **House Prices between 80K USD - 8M USD**: 8171 Houses
       - **House Prices between 80K USD - 4M USD**: 8081 Houses (dropped 90 houses)
       - **House Prices between 300K USD - 4M USD**: 7964 Houses (dropped 117 houses) 
       - **House Prices between 300K USD - 2M USD**: 7396 Houses (dropped 568 houses) 
       - We're highlighting the correlation between difference house price ranges against all the possible features:
        * <font color=green>Green</font>: Correlation > 0.4
        * <font color=blue>Blue</font>: 0 < Correlation < 0.4
        * <font color=red>Red</font>:  Correlation < 0


