# Linear Regression
linear_regression_dict = {}

# Lasso
lasso_dict = {
    'alpha': [0.001, 0.01, 0.1, 1],
    'max_iter': [1000, 2000, 3000]
}

# Ridge
ridge_dict = {
    'alpha': [0.001, 0.01, 0.1, 1],
    'solver': ['auto', 'svd', 'cholesky', 'lsqr', 'sparse_cg', 'sag', 'saga'],
    'max_iter': [1000, 2000, 3000]
}

# K-Neighbors Regressor
k_neighbors_regressor_dict = {
    'n_neighbors': [3, 5, 7, 9],
    'weights': ['uniform', 'distance'],
    'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute']
}

# Random Forest Regressor
random_forest_regressor_dict = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Gradient Boosting Regressor
gradient_boosting_regressor_dict = {
    'n_estimators': [50, 100, 150],
    'learning_rate': [0.01, 0.1, 0.5],
    'max_depth': [3, 5, 7],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# AdaBoost Regressor
adaboost_regressor_dict = {
    'n_estimators': [50, 100, 150],
    'learning_rate': [0.01, 0.1, 0.5],
    'loss': ['linear', 'square', 'exponential']
}

# XGBRegressor
xgb_regressor_dict = {
    'n_estimators': [50, 100, 150],
    'learning_rate': [0.01, 0.1, 0.5],
    'max_depth': [3, 5, 7],
    'min_child_weight': [1, 3, 5],
    'gamma': [0.0, 0.1, 0.2]
}

# CatBoosting Regressor
catboost_regressor_dict = {
    'n_estimators': [50, 100, 150],  
    'max_depth': [3, 5, 7],         
    'learning_rate': [0.01, 0.05, 0.1],  
    'l2_leaf_reg': [0.1, 0.5, 1],        
    'bagging_temperature': [0.5, 1, 2],   
    'subsample': [0.6, 0.8, 1],          
    'random_strength': [0.5, 1]          
}

