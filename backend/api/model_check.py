import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, mean_squared_log_error
from sklearn.metrics import f1_score, roc_auc_score, roc_curve

def rmse(test, pred):
    return np.sqrt(mean_squared_error(test, pred))
reg_check = {
    "Mean Absolute Error": mean_absolute_error,
    "Mean Squared Error": mean_squared_error,
    "Root Mean Squared Error": rmse,
    "R-squared": r2_score,
    "Mean Squared Log Error": mean_squared_log_error
}
bc_check = {
    "F1": f1_score,
    "ROC": [roc_auc_score, roc_curve]
}

def dtr_test(X, y, scoring):
    scoring = reg_check[scoring]
    X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=0,train_size=.80)
    if scoring != r2_score:
        best_score = float('inf')
        best_depth = 1
        for depth in range(1,26):
            reg = DecisionTreeRegressor(max_depth=depth,random_state=0)
            reg.fit(X_train, y_train)
            y_pred = reg.predict(X_test)
            score = scoring(y_test, y_pred)
            if best_score > score:
                best_score = score
                best_depth = depth
        return [repr(DecisionTreeRegressor(max_depth=best_depth,random_state=0)), score]
    else:
        best_score = float('-inf')
        best_depth = 1
        for depth in range(1,26):
            reg = DecisionTreeRegressor(max_depth=depth,random_state=0)
            reg.fit(X_train, y_train)
            y_pred = reg.predict(X_test)
            score = scoring(y_test, y_pred)
            if best_score < score:
                best_score = score
                best_depth = depth
        return [repr(DecisionTreeRegressor(max_depth=best_depth,random_state=0)), score]
def logis_reg_test(X, y, scoring):


mod_check = {
    "DecisionTreeRegressor": dtr_test
}