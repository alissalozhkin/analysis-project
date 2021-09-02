"""Trying to implement multiple linear regression.
Note that the code in this function is largely for testing purposes
and may not play nicely with the data we end up using. Note that
I'm assuming the data from the datasets has been put into Dataframes with pandas."""
from typing import Dict, List
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from download_data import get_temperature_data


def multiple_lin_reg(data: Dict[int, float]) -> None:
    """ Perform multiple linear regression on the given data
    and prints coefficients, intercept, predicted y-values,
    and summary of results.

    Preconditions:
        - data has the columns 'Sea Levels', 'CO2 Levels', 'Temperatures',
            and 'Glacier Melt'
    """
    df = pd.DataFrame(data=data)

    # separating features and target
    y = df['Sea Levels']
    x = df[['CO2 Levels', 'Temperatures', 'Glacier Melt']]

    # defining the multiple linear regression model
    lin_reg = LinearRegression()

    # 'training' the model
    model = lin_reg.fit(x, y)

    print('Coefficients: ' + model.coef_)
    print('Intercept: ' + model.intercept_)

    # predicting sea levels (?)
    y_pred = lin_reg.predict(x)
    print('Predicted Values: ' + y_pred)
    model.summary()
