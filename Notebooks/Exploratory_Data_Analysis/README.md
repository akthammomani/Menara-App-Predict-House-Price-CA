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
   
<code>**'price'**</code>: 
Before
![price_1](https://user-images.githubusercontent.com/67468718/104831551-e2219380-583e-11eb-8d47-2cfbd22df1e1.JPG)
After
![price_2](https://user-images.githubusercontent.com/67468718/104831552-e2219380-583e-11eb-9793-02d9fc506321.JPG)

<code>**'sqft'**</code>



   
   

