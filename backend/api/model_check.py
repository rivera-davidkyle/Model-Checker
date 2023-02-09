import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV


def dtr_test(X, y):
    reg = DecisionTreeRegressor(random_state=0)
    param_grid = {
        'max_depth': range(1,25),
        'min_samples_split': range(2,11,2),
        'min_samples_leaf': range(1,10)
                }
    grid_search = RandomizedSearchCV(reg, param_grid, cv=5, n_jobs=-1)
    grid_search.fit(X, y)
    return [repr(DecisionTreeRegressor(**grid_search.best_params_)), grid_search.best_score_]

def linear_test(X,y):
    reg = LinearRegression()
    param_grid = {'fit_intercept': [True,False]
                }
    grid_search = GridSearchCV(reg, param_grid, cv=5, n_jobs=-1)
    grid_search.fit(X, y)
    return [repr(LinearRegression(**grid_search.best_params_)), grid_search.best_score_]

def svr_test(X,y):
    y = np.ravel(y)
    reg = SVR()
    param_grid = {
        'gamma': [1e-7,1e-3,1e1],
        'C': [0.001, 100.0, 100000.0]
                }
    grid_search = RandomizedSearchCV(reg, param_grid, cv=5, n_jobs=-1)
    grid_search.fit(X, y)
    return [repr(SVR(**grid_search.best_params_)), grid_search.best_score_]