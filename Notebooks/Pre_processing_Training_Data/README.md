
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

  #### 2.3 Datasets comparison using statistics summary: According to the below table, std_df is showig the best, mean, std by eliminating all data greater than 1.2 standard deviation from the mean and at the same we managed only to lose 687 outliers.
  ![stat_sum](https://user-images.githubusercontent.com/67468718/111862620-96a96580-8913-11eb-8115-fc35fb887f40.JPG)
 
