# Modeling: 

![Modeling](https://user-images.githubusercontent.com/67468718/111879997-1bbd6a80-8966-11eb-92c1-01c38cbdbe4a.JPG)

## Introduction<a id='1_Introduction'></a>

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

As we can see below, We managed to improve our Neural Network Regressio Regression Model by:
 * Making the Neural Network deeper by using more hidden Layers, and
 * Making the Neural Network wider by using more neurons
   * NN-Model 1 we used 1 Hidden layer with 22 Neurons.
   * NN-Model 2 we used 3 Hidden layer with 22 Neurons.
   * NN-Model 3 we used 5 Hidden layer with 40 Neurons.
 * **Variance Score has improved from 79.3446 % (XGBoost - baseline) to 99.3254 %.**
 
|Neural Network Architecture| r2 Score|    MAE  | MSE  | RMSE|Variance Score|
|:----------------------|:-------:|:-------:|:----:|:----:|:----:|
|NN-Model 1: 1 Hidden layer with 22 Neurons|79.1614 %|129672.4510|30790164793.7299|175471.2649|79.3446 %|
|NN-Model 2: 3 Hidden layer with 22 Neurons|96.2795 %|52197.7063|5497273121.1486|74143.5980|96.3320 %|
|NN-Model 3: 5 Hidden layer with 40 Neurons|99.3142 %|21473.0534|1013285921.8239|31832.1523|99.3254 %|
 
