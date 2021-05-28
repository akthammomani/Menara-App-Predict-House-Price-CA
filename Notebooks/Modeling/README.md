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

|No.|Models| R^2 Score|Adjusted R^2 Score  |  MAE  | RMSE|Variance Score|
|:----:|:----------------------|:-------:|:-------:|:----:|:----:|:----:|
|1|Dummy Regression|0 %|0 %|301148.2119|376306.4570|0 %|
|2|Linear Regression |87.0594 %|86.9199 %|96522.4628|135367.8835|87.0805 %|
|3|Tuned Ridge|87.0763 %|86.9369 %|96489.2726|135279.9288|87.0970 %|
|4|Tuned Lasso|87.0595 %|86.9200 %|96520.8254|135367.3967|87.0806 %|
|5|Tuned Decision Tree|87.4464 %|87.3110 %|92510.0434|133328.6903|87.4864 %|
|6|Tuned ANN|91.0938 %|90.9978 %|76641.2342|112301.3342|91.1308 %|
|7|Tuned Random Forests|92.1982 %|92.1141 %|67886.0897|105107.8895|92.2170 %|
|8|Gradient Boosting   |92.4799 %|92.3988 %|66910.7055|103193.3274|92.4863 %|
|9|Tuned XGBoost   |92.5777 %|92.4977 %|67043.7283|102520.0032|92.5786 %|
|10|Tuned LightGBM|92.6304 %|92.5510 %|66235.3892|102155.1713|92.6406 %|
|11|Baseline Stacking|92.4033 %|92.3214 %|68855.7449|103717.3961|92.4168 %|
|12|**Tuned Stacking - Winner**  |92.7615 %|92.6835 %|65381.7572|101242.5730|92.7760 %|

## 1. Dummy Regression and Linear regression Summary:

Dummy Regression and Linear regression performance summary with Features tuning:

|Features Selection| R^2 Score|Adjusted R^2 Score  |  MAE  | RMSE|Variance Score|
|:----------------------|:-------:|:-------:|:----:|:----:|:----:|
|Dummy Regression - (all features)|0 %|0 %|301148.2119|376306.4570|0 %|
|Linear Regression - Baseline (all features)|87.3432 %|87.1112 %|95909.6995|133875.4717|87.3781 %|
|Linear Regression - Tuned(High Important Features)   |87.0594 %|86.9199 %|96522.4628|135367.8835|87.0805 %|

## 2. Ridge Regression Tuning Summary:

Ridge Regression Model Tunning Summary:
 * Keeping the high important features.
 * Using Regularization to determine best Alpha=15.20975162616059 and solver=sparse_cg.
 * Variance Score has degraded from 87.3653 % (Ridge - baseline) to 87.0970 %

|Features Selection| R^2 Score|Adjusted R^2 Score  |  MAE  | RMSE|Variance Score|
|:----------------------|:-------:|:-------:|:----:|:----:|:----:|
|Baseline (all features)|87.3345 %|87.1024 %|95239.0802|133921.3033|87.3653 %|
|Tuned(High Important Features)   |87.0600 %|86.9205 %|96520.6475|135365.0654|87.0810 %|
|Tuned(High Important Features) + Regularization {'alpha': 15.20975162616059, 'solver': 'sparse_cg'}   |87.0763 %|86.9369 %|96489.2726|135279.9288|87.0970 %|

## 3. Lasso Regression Regression Tuning Summary:

Lasso  Regression Model Tunning Summary:
 * Keeping the high important features.
 * Using Regularization to determine best Alpha=10.
 * Variance Score has degraded from 87.30 % (Lasso - baseline) to 87.0806 %

|Features Selection| R^2 Score|Adjusted R^2 Score  |  MAE  | RMSE|Variance Score|
|:----------------------|:-------:|:-------:|:----:|:----:|:----:|
|Baseline (all features)|87.27 %|87.0356 %|96077.5947|134267.8161|87.30 %|
|Tuned(High Important Features)   |87.0595 %|86.9199 %|96522.2991|135367.8360|87.0805 %|
|Tuned(High Important Features) + Regularization {'alpha': 10'}   |87.0595 %|86.9200 %|96520.8254|135367.3967|87.0806 %|
 
## 4. Decision Tree Regression Tuning Summary:

As we can see below, We managed to improve our Decision Tree Regression Model by:
 * keeping only the most important features: and
 * Hyperparameters Tuning using RandomizedSearchCV to determine best:
   * {'min_samples_split': 28, 'min_samples_leaf': 11, 'max_features': 'auto'} when considering all features.
   * {'min_samples_split': 28, 'min_samples_leaf': 16, 'max_features': 'auto', 'max_depth': 15} when considering only the most important features.
 * Variance Score has improved from 84.5661 % (Decision Tree - baseline) to 87.4864 %.

|Features Selection| R^2 Score|Adjusted R^2 Score  |  MAE  | RMSE|Variance Score|
|:----------------------|:-------:|:-------:|:----:|:----:|:----:|
|Baseline (all features)|84.5454 %|84.3787 %|99336.2012|147934.2861|84.5661 %|
|Baseline (Keeping high important Features)     |85.1269 %|84.9665 %|96266.4337|145124.2649|85.1990 %|
|All Features + RandomizedSearchCV {'min_samples_split': 28, 'min_samples_leaf': 11, 'max_features': 'auto'}|87.1429 %|86.9073 %|92447.3932|134930.5062|87.2065 %|
|High Important Features + RandomizedSearchCV {'min_samples_split': 28, 'min_samples_leaf': 16, 'max_features': 'auto', 'max_depth': 15}|87.4464 %|87.3110 %|92510.0434|133328.6903|87.4864 %|

## 5. Artificial Neural Network (ANN) Regression Tuning Summary:

As we can see below, We managed to improve our Neural Network Regression Model by:
 * Making the Neural Network deeper by using more hidden Layers, and
 * Making the Neural Network wider by using more neurons
   * NN-Model 1 we used 1 Hidden layer with 16 Neurons.
   * NN-Model 2 we used 3 Hidden layer with 16 Neurons.
   * NN-Model 3 we used 5 Hidden layer with 35 Neurons.
 * **Variance Score has improved from 67.0386 % (Neural Network - baseline) to 91.1308 %.**
 
|Neural Network Architecture| R^2 Score|Adjusted R^2 Score  |  MAE  | RMSE|Variance Score|
|:----------------------|:-------:|:-------:|:----:|:----:|:----:|
|Baseline: NN-Model 1 we used 1 Hidden layer with 16 Neurons|65.2787 %|64.9043 %|169664.7498|221736.5273|67.0386 %|
|RandomizedSearchCV{'epochs': 600, 'batch_size': 32}: NN-Model 1 we used 1 Hidden layer with 16 Neurons   |89.0462 %|88.9281 %|86728.7935|124543.6689|89.0688 %|
|RandomizedSearchCV{'epochs': 600, 'batch_size': 32, 'learning_rate': 0.01}: NN-Model 1 we used 1 Hidden layer with 16 Neurons   |91.0938 %|90.9978 %|76641.2342|112301.3342|91.1308 %|
|RandomizedSearchCV{'epochs': 600, 'batch_size': 32, 'learning_rate': 0.001}: NN-Model 2 we used 3 Hidden layer with 16 Neurons  |90.6292 %|90.5281 %|78263.6255|115193.6831|90.6817 %|
|RandomizedSearchCV{'epochs': 600, 'batch_size': 32, 'learning_rate': 0.001}: NN-Model 2 we used 5 Hidden layer with 35 Neurons |90.5898 %|90.4884 %|77239.6853|115435.2556|90.6127 %|
 
## 6. Random Forests Tuning Summary: 

As we can see below, We managed to improve our Random Forests Regression Model by:
 * keeping only the high important features:  and
 * Hyperparameters Tuning using RandomizedSearchCV to determine best:
   * {'n_estimators': 300, 'max_features': 'sqrt', 'max_depth': 20} when considering all features.
   * {'n_estimators': 600, 'min_samples_split': 6, 'max_features': 'log2'} when considering only the highimportant features
 * Variance Score has improved from 91.4562 % (Random Forests - baseline) to 92.2170 %.

|Features Selection| R^2 Score|Adjusted R^2 Score  |  MAE  | RMSE|Variance Score|
|:----------------------|:-------:|:-------:|:----:|:----:|:----:|
|Baseline (all features)|91.4367 %|91.2797 %|71881.2010|110118.6979|91.4562 %|
|Baseline (Keeping high important Features)  |91.4910 %|91.3993 %|72011.8407|109768.5543|91.5134 %|
|All Features + RandomizedSearchCV {'n_estimators': 300, 'max_features': 'sqrt', 'max_depth': 20}|91.9673 %|91.8201 %|68595.6250|106652.1579|91.9863 %|
|High Important Features + RandomizedSearchCV {'n_estimators': 600, 'min_samples_split': 6, 'max_features': 'log2'}	   |92.1982 %|92.1141 %|67886.0897|105107.8895|92.2170 %|

 ## 6. XGBoost Regression Tuning Summary:

As we can see below, We managed to improve our XGBoost Regression Model by:
 * keeping only the high important features: and
 * Hyperparameters Tuning using RandomizedSearchCV to determine best:
   * {'n_estimators': 900, 'min_child_weight': 11, 'max_depth': 10, 'learning_rate': 0.01, 'gamma': 0.3, 'colsample_bytree': 0.4} when considering all features.
   * {'n_estimators': 600, 'min_child_weight': 12, 'max_depth': 16, 'learning_rate': 0.01, 'gamma': 0.3, 'colsample_bytree': 0.6} when considering only the high important features.
 * Variance Score has improved from 90.9428 % (XGBoost - baseline) to 92.5786 %.
 
|Features Selection| R^2 Score|Adjusted R^2 Score  |  MAE  | RMSE|Variance Score|
|:----------------------|:-------:|:-------:|:----:|:----:|:----:|
|Baseline (all features)|90.9334 %|90.7672 %|74685.8334|113308.0568|90.9428 %|
|Baseline (Keeping high important Features)    |91.5418 %|91.4506 %|72408.9447|109440.3965|91.5428 %|
|All Features + RandomizedSearchCV {'n_estimators': 900, 'min_child_weight': 11, 'max_depth': 10, 'learning_rate': 0.01, 'gamma': 0.3, 'colsample_bytree': 0.4}|92.5617 %|92.3162 %|66304.8201|102630.7106|92.5737 %|
|High Important Features + RandomizedSearchCV {'n_estimators': 600, 'min_child_weight': 12, 'max_depth': 16, 'learning_rate': 0.01, 'gamma': 0.3, 'colsample_bytree': 0.6}|92.5777 %|92.4977 %|67043.7283|102520.0032|92.5786 %|

## 7. Gradient Boosting Regression Tuning Summary:

As we can see below, We managed to improve our Gradient Boosting Regression Model by:
 * keeping only the most important features: and
 * Hyperparameters Tuning using RandomizedSearchCV to determine best:
   * {'n_estimators': 1500, 'max_features': 'sqrt', 'max_depth': 8, 'learning_rate': 0.01} when considering all features.
   * {'n_estimators': 800, 'max_features': 'log2', 'max_depth': 6, 'learning_rate': 0.05}  when considering the high important features.
 * Variance Score has improved from 91.1607 % (Gradient Boosting - baseline) to 92.4863 %.
 
|Features Selection| R^2 Score|Adjusted R^2 Score  |  MAE  | RMSE|Variance Score|
|:----------------------|:-------:|:-------:|:----:|:----:|:----:|
|Baseline (all features)|91.1470 %|90.9847 %|77082.4736|111965.8849|91.1607 %|
|Baseline (Keeping high important Features)    |90.8521 %|90.7535 %|78212.3780|113814.8578|90.8621 %|
|All Features + RandomizedSearchCV {'n_estimators': 1500, 'max_features': 'sqrt', 'max_depth': 8, 'learning_rate': 0.01}|92.4545 %|92.3162 %|66219.4133|103367.2310|92.4616 %|
|High Important Features + RandomizedSearchCV {'n_estimators': 800, 'max_features': 'log2', 'max_depth': 6, 'learning_rate': 0.05}	   |92.4799 %|92.3988 %|66910.7055|103193.3274|92.4863 %|

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

## 8. Light GBM Regression Tuning Summary:

As we can see below, We managed to improve our LightGBM Regression Model by:
 * keeping only the high important features: and
 * Hyperparameters Tuning using RandomizedSearchCV to determine best:
   * {'reg_lambda': 0.4, 'reg_alpha': 0.6, 'n_estimators': 1700, 'learning_rate': 0.01, 'colsample_bytree': 0.6, 'max_depth':15, 'num_leaves'= 32767} when considering all features.
   * {'reg_lambda': 0.4, 'reg_alpha': 0.8, 'n_estimators': 1000, 'learning_rate': 0.01, 'colsample_bytree': 0.6, 'max_depth':15, 'num_leaves'= 32767} when considering only the high important features.
 * Variance Score has improved from 91.9935 % (LightGBM - baseline) to 92.6406 %.
 
|Features Selection| R^2 Score|Adjusted R^2 Score  |  MAE  | RMSE|Variance Score|
|:----------------------|:-------:|:-------:|:----:|:----:|:----:|
|Baseline (all features)|91.9853 %|91.8384 %|70644.4765|106532.6116|91.9935 %|
|Baseline (Keeping high important Features)    |92.2960 %|92.2129 %|70316.6721|104447.5214|92.3067 %|
|All Features + RandomizedSearchCV|92.5526 %|92.4160 %|66041.6874|102693.4526|92.5621 %|
|High Important Features + RandomizedSearchCV    |92.6304 %|92.5510 %|66235.3892|102155.1713|92.6406 %|


## 9. Stacking Regression Tuning Summary:

As we can see below, We managed to improve our Stacking Regression Model by **stacking**:
 * Random Forests.
 * Gradient Boosting.
 * LightGBM
 * XGBoost


Variance Score has improved from 92.4168 % (Stacking Regression - baseline) to 92.7760 % and also we managed to get better performance from all base (Tuned) Models as shown below:
 
|Models| R^2 Score|Adjusted R^2 Score  |  MAE  | RMSE|Variance Score|
|:----------------------|:-------:|:-------:|:----:|:----:|:----:|
|Tuned Random Forests|92.1982 %|92.1141 %|67886.0897|105107.8895|92.2170 %|
|Tuned Gradient Boosting   |92.4799 %|92.3988 %|66910.7055|103193.3274|92.4863 %|
|Tuned XGBoost   |92.5777 %|92.4977 %|67043.7283|102520.0032|92.5786 %|
|Tuned LightGBM|92.6304 %|92.5510 %|66235.3892|102155.1713|92.6406 %|
|Baseline Stacking|92.4033 %|92.3214 %|68855.7449|103717.3961|92.4168 %|
|Tuned Stacking  |92.7615 %|92.6835 %|65381.7572|101242.5730|92.7760 %|
 
