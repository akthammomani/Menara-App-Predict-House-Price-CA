# Modeling: 

![Modeling](https://user-images.githubusercontent.com/67468718/111879997-1bbd6a80-8966-11eb-92c1-01c38cbdbe4a.JPG)

## Introduction<a id='1_Introduction'></a>

Here comes the really fun step: modeling! For this step, we'll be:
 * Training multiple Regression algorithms.
 * Apply hyperparameters tuning where applicable to ensure every algorithm will result in best prediction possible.
 * Finally, evaluate these Models.

**Regression Models:**
 * Dummy Regression (Baseline Model)
 * Linear Regression
 * Ridge Regression (L2 Regularization)
 * Lasso Regression (L1 Regularization)
 * Decision Trees
 * Random Forests
 * GB
 * XGBoost
 * Light GBM
 * Artificial Neural networks (ANN).
 * Stacking:
   * Base Models:
     * Random Forests
     * GB
     * XGBoost
     * Light GBM
   * Meta Model:
     * Ridge

## Regression Models Performance Summary:

|Models| R^2 Score|Adjusted R^2 Score  |  MAE  | RMSE|Variance Score|
|:----------------------|:-------:|:-------:|:----:|:----:|:----:|
|Dummy Regression|0 %|0 %|301148.2119|376306.4570|0 %|
|Linear Regression |87.0594 %|86.9199 %|96522.4628|135367.8835|87.0805 %|
|Tuned Ridge|87.0763 %|86.9369 %|96489.2726|135279.9288|87.0970 %|
|Tuned Lasso|87.0595 %|86.9200 %|96520.8254|135367.3967|87.0806 %|
|Tuned Decision Tree|87.4464 %|87.3110 %|92510.0434|133328.6903|87.4864 %|
|Tuned ANN|91.0938 %|90.9978 %|76641.2342|112301.3342|91.1308 %|
|Tuned Random Forests|92.1982 %|92.1141 %|67886.0897|105107.8895|92.2170 %|
|Gradient Boosting   |92.4799 %|92.3988 %|66910.7055|103193.3274|92.4863 %|
|Tuned XGBoost   |92.5777 %|92.4977 %|67043.7283|102520.0032|92.5786 %|
|Tuned LightGBM|92.6304 %|92.5510 %|66235.3892|102155.1713|92.6406 %|
|Baseline Stacking|92.4033 %|92.3214 %|68855.7449|103717.3961|92.4168 %|
|Tuned Stacking  |92.7615 %|92.6835 %|65381.7572|101242.5730|92.7760 %|

## 1. XGBoost Regression Tuning Summary:

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

## 2. Gradient Boosting Regression Tuning Summary:

As we can see below, We managed to improve our Gradient Boosting Regression Model by:
 * keeping only the most important features: 2 features ('sqft' and'price_per_sqft'), and
 * Hyperparameters Tuning using RandomizedSearchCV to determine best:
   * {'n_estimators': 450, 'max_features': 'auto', 'max_depth': 5, 'learning_rate': 0.1, 'alpha': 0.9} when considering all features.
   * {'n_estimators': 400, 'max_depth': 5, 'learning_rate': 0.1, 'alpha': 0.1}  when considering only the top-2 important features.
   * {'n_estimators': 300, 'max_depth': 5, 'learning_rate': 0.1, 'alpha': 0.9} when considering only the top-5 important features  
 * Variance Score has improved from 99.1037 % (Gradient Boosting - baseline) to 99.7975 %.
 
|Model Tuning| r2 Score|    MAE  | MSE  | RMSE|Variance Score|
|:----------------------|:-------:|:-------:|:----:|:----:|:----:|
|Baseline (all features)|99.1028 %|25714.0701|1325687350.4870|36409.9897|99.1037 %|
|Keeping 2 features (Most Important)    |99.2931 %|21855.3031|1044412302.2215|32317.3684|99.2935 %|
|Keeping 5 features    |99.1526 %|25045.7896|1252130275.5254|35385.4529|99.1534 %|
|Keeping All features + {'n_estimators': 450, 'max_depth': 5, 'learning_rate': 0.1, 'alpha': 0.9} (RandomizedSearchCV)   |99.6818 %|11633.3820|470161172.4308|21683.2002|99.6820 %|
|Keeping top-2 features + {'n_estimators': 400, 'max_depth': 5, 'learning_rate': 0.1, 'alpha': 0.1} (RandomizedSearchCV) |99.7970 %|8819.2568|299917983.5644|17318.1403|99.7975 %|
|Keeping top-5 features  + {'n_estimators': 300, 'max_depth': 5, 'learning_rate': 0.1, 'alpha': 0.9} (RandomizedSearchCV)|99.7780 %|10175.0694|328029686.2094|18111.5898|99.7783 %|

**Learning rate Summary**:
 * The lower the learning rate, the slower the model learns. 
 * The advantage of slower learning rate is that the model becomes more robust and generalized (In statistical learning, models that learn slowly perform better).
 * Learning slowly comes at a cost. It takes more time to train the model which brings us to the other significant hyperparameter.
 
 
**n_estimator Summary**:
 * n_estimator is the number of trees used in the model. 
 * If the learning rate is low, we need more trees to train the model.
 * We need to be very careful at selecting the number of trees. It creates a high risk of overfitting to use too many trees.
 
**Random Forests vs Gradient Boosting**: 
 * One key difference between random forests and gradient boosting decision trees is the number of trees used in the model.
   * Increasing the number of trees in random forests does not cause overfitting.
   * The number of trees in gradient boosting decision trees is very critical in terms of overfitting. Adding too many trees will cause overfitting so it is important to stop adding trees at some point.

## 3. Random Forests Regression Tuning Summary:

As we can see below, We managed to improve our Random Forests Regression Model by:
 * keeping only the most important features: 2 features ('sqft' and'price_per_sqft'), and
 * Hyperparameters Tuning using RandomizedSearchCV to determine best:
   * {'n_estimators': 500, 'min_samples_split': 2, 'min_samples_leaf': 1, 'max_depth': 30} when considering all features.
   * {'n_estimators': 450, 'min_samples_split': 2, 'min_samples_leaf': 1, 'max_depth': 16} when considering only the top-2 important features
   * {'n_estimators': 500, 'min_samples_split': 2, 'min_samples_leaf': 1, 'max_depth': 26} when considering only the top-5 important features 
 * Variance Score has improved from 99.6789  % (Random Forests - baseline) to 99.8214 %

|Model Tuning| r2 Score|    MAE  | MSE  | RMSE|Variance Score|
|:----------------------|:-------:|:-------:|:----:|:----:|:----:|
|Baseline (all features)|99.6786 %|9767.2155|474838904.0747|21790.7986|99.6789 %|
|Keeping 2 features (Most Important)    |99.8165 %|6530.7833|271089597.6564|16464.7987|99.8168 %|
|Keeping 5 features    |99.7714  %|17679.2312|337800382.4367|18379.3466|99.7718 %|
|Keeping All features + {'n_estimators': 500, 'max_depth': 30} (RandomizedSearchCV)  |99.6824 %|9620.5996|469264404.6720|21662.5115|99.6826 %|
|Keeping top-2 features + {'n_estimators': 450, 'max_depth': 16} (RandomizedSearchCV)|99.8210 %|6302.4739|264445019.5696|16261.7656|99.8214 %|
|Keeping top-5 features + {'n_estimators': 500, 'max_depth': 26} (RandomizedSearchCV)|99.7865 %|7353.4259|315470893.2504|17761.5003|99.7866 %|
 
## 4. Neural Network Regression Tuning Summary:

As we can see below, We managed to improve our Neural Network Regression Model by:
 * Making the Neural Network deeper by using more hidden Layers, and
 * Making the Neural Network wider by using more neurons
   * NN-Model 1 we used 1 Hidden layer with 22 Neurons.
   * NN-Model 2 we used 3 Hidden layer with 22 Neurons.
   * NN-Model 3 we used 5 Hidden layer with 40 Neurons.
 * **Variance Score has improved from 79.3446 % (Neural Network - baseline) to 99.3254 %.**
 
|Neural Network Architecture| r2 Score|    MAE  | MSE  | RMSE|Variance Score|
|:----------------------|:-------:|:-------:|:----:|:----:|:----:|
|NN-Model 1: 1 Hidden layer with 22 Neurons|79.1614 %|129672.4510|30790164793.7299|175471.2649|79.3446 %|
|NN-Model 2: 3 Hidden layer with 22 Neurons|96.2795 %|52197.7063|5497273121.1486|74143.5980|96.3320 %|
|NN-Model 3: 5 Hidden layer with 40 Neurons|99.3142 %|21473.0534|1013285921.8239|31832.1523|99.3254 %|

## 5. Decision Tree Regression Tuning Summary:

As we can see below, We managed to improve our Decision Tree Regression Model by:
 * keeping only the most important features: 2 features ('sqft' and'price_per_sqft'), and
 * Hyperparameters Tuning using RandomizedSearchCV to determine best:
   * {'splitter': 'best', 'min_samples_split': 6, 'min_samples_leaf': 6, 'max_depth': None} when considering all features.
   * {'splitter': 'best', 'min_samples_split': 2, 'min_samples_leaf': 1, 'max_depth': 20} when considering only the most important features.
 * Variance Score has improved from 98.7780 % (Decision Tree - baseline) to 99.2365 %.

|Model Tuning| r2 Score|    MAE  | MSE  | RMSE|Variance Score|
|:----------------------|:-------:|:-------:|:----:|:----:|:----:|
|Baseline (all features)|98.7776 %|22497.1309|1806197855.0123|42499.3865|98.7780 %|
|Keeping 2 features (Most Important)    |99.2406 %|15058.3533|1122033204.6526|33496.7641|99.2412 %|
|Keeping 5 features                     |98.7992 %|19343.5318|1774295512.9909|42122.3873|98.7997 %|
|All features + {'min_samples_split': 6, 'min_samples_leaf': 6} (RandomizedSearchCV)|98.9881 %|23113.4753|1495079820.6304|38666.2620|98.9881 %|
|Keeping Top-2 features + {max_depth=20} (RandomizedSearchCV) |99.2356 %|15092.9610|1129397345.5981|33606.5075|99.2365 %|
 
## 6. Linear Regression Tuning Summary: 

As we can see below, when we're dropping 2 features ('malls', 'university_count'): we're seeing the best Result for Linear regression: 

|Features Selection| r2 Score|    MAE  | MSE  | RMSE|Variance Score|
|:----------------------|:-------:|:-------:|:----:|:----:|:----:|
|Baseline (all features)|93.4472 %|69515.8128|9682059380.4426|98397.4562|93.4490 %|
|Dropping 2 features    |93.4513 %|69477.6024|9676046249.8131|98366.8961|93.4530 %|
|Dropping 3 Features    |93.4452 %|69372.9557|9685059694.4905|98412.7009|93.4466 %|
|Dropping 5 Features    |93.4136 %|69435.2387|9731797948.3080|98649.8756|93.4154 %|

 ## 6. Ridge Regression Tuning Summary:

As we can see below, We managed to improve our Ridge Regression Model by:
 * Dropping 2 features ('malls', 'university_count'), and
 * Using Regularization to determine best Alpha=0.00018374437246107268
 * Variance Score has improved from 93.4414 % (Ridge - baseline) to 93.4594 %

|Model Tuning| r2 Score|    MAE  | MSE  | RMSE|Variance Score|
|:----------------------|:-------:|:-------:|:----:|:----:|:----:|
|Baseline (all features + Alpha=1 (Default))|93.4394 %|69557.6932|9693635442.7628|98456.2616|93.4414 %|
|Dropping 2 features    |93.4446 %|69518.8784|9685945307.3284|98417.2003|93.4466 %|
|Dropping 2 features + Regularization II (Alpha =0.00018374437246107268)  |93.4576 %|69427.9988|9666812279.1121|98319.9485|93.4594 %|

## 7. Lasso Regression Tuning Summary:

As we can see below, We managed to improve our Lasso Regression Model by:
 * Dropping 2 features ('malls', 'university_count'), and
 * Variance Score has improved from 93.4418 % (Lasso - baseline) to 93.4470 %
 
However, Lasso Model degraded slightly after we applied regularization L1 as shown below: 


|Model Tuning| r2 Score|    MAE  | MSE  | RMSE|Variance Score|
|:----------------------|:-------:|:-------:|:----:|:----:|:----:|
|Baseline  (all features + Alpha=1 (Default))|93.4398 %|69554.3493|9693079224.7295|98453.4368|93.4418 %|
|Dropping 2 features    |93.4450 %|69516.0097|9685389213.4795|98414.3750|93.4470 %|
|Dropping 2 features + Regularization I (Alpha =10)  |93.4446 %|69511.4134|9685988690.4620|98417.4207|93.4466 %|
