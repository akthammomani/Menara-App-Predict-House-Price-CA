# Modeling: 

![Modeling](https://user-images.githubusercontent.com/67468718/111879997-1bbd6a80-8966-11eb-92c1-01c38cbdbe4a.JPG)

## 1. Introduction<a id='1_Introduction'></a>

Here comes the really fun step: modeling! For this step, we'll be:
 * Training multiple Regression algorithms.
 * Apply hyperparameters tuning where applicable to ensure every algorithm will result in best prediction possible.
 * Finally, evaluate these Models.

**Regression Models:**
 * Linear Regression (Baseline Model).
 * Ridge Regression (L2 Regularization)
 * Lasso Regression (L1 Regularization)
 * Decision Trees
 * Random Forests
 * GB
 * XGBoost
 * Stacking
 * Neural networks.

## XGBoost Regression Tuning Summary:

As we can see below, We managed to improve our XGBoost Regression Model by:
 * keeping only the most important features: 2 features ('sqft' and'price_per_sqft'), and
 * Hyperparameters Tuning using RandomizedSearchCV to determine best:
   * {'n_estimators': 350, 'min_child_weight': 1, 'max_depth': 6, 'learning_rate': 0.05, 'gamma': 0.07, 'colsample_bytree': 1} when considering all features.
   * {'n_estimators': 450, 'min_child_weight': 1, 'max_depth': 10, 'learning_rate': 0.05, 'gamma': 0.07, 'colsample_bytree': 1} when considering only the top-2 important features.
   * {'n_estimators': 500, 'min_child_weight': 1, 'max_depth': 9, 'learning_rate': 0.05, 'gamma': 0.7, 'colsample_bytree': 1} when considering only the top-5 important features  
 * Variance Score has improved from 99.3963 % (XGBoost - baseline) to 99.8132 %.
 
|Model Tuning| r2 Score|    MAE  | MSE  | RMSE|Variance Score|
|:----------------------|:-------:|:-------:|:----:|:----:|:----:|
|Baseline (all features)|99.3961 %|18562.6278|892350521.4109|29872.2366|99.3963 %|
|Keeping 2 features (Most Important)    |99.6627 %|12850.6589|498437095.4752|22325.7048|99.6627 %|
|Keeping 4 features    |99.5752 %|14938.3076|627600695.7750|25051.9599|99.5752 %|
|Keeping All features + {'n_estimators': 350, 'max_depth': 6, 'learning_rate': 0.05, 'gamma': 0.07} (RandomizedSearchCV)   |99.6757 %|11941.3109|479239850.7725|21891.5475|99.6757 %|
|Keeping top-2 features + {'n_estimators': 450, 'max_depth': 10, 'learning_rate': 0.05, 'gamma': 0.07} (RandomizedSearchCV) |99.8132 %|7322.9617|276080878.1273|16615.6817|99.8132 %|
|Keeping top-5 features  + {'n_estimators': 500, 'max_depth': 9, 'learning_rate': 0.05, 'gamma': 0.7} (RandomizedSearchCV)|99.7787 %|8626.9765|326958842.8709|18082.0033|99.7787 %|
