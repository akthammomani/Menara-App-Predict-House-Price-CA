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


